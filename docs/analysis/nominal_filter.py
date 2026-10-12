"""Nominal Rev A low-pass analysis; ideal buffer, no measured data.

Dependencies: numpy, scipy, matplotlib.
Run this file to regenerate the response figure and numerical results.
The model describes the shared ADC/DAC three-pole RC/active network.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
R1, R2, R3 = 6800.0, 22000.0, 12000.0
C1, C2, C3 = 1e-9, 1e-9, 150e-12
A1 = C1*R1+C3*(R1+R2+R3)
A2 = C1*C3*R1*(R2+R3)+C2*C3*R3*(R1+R2)
A3 = C1*C2*C3*R1*R2*R3

def transfer(frequency):
    s = 2j*np.pi*np.asarray(frequency)
    return 1/(1+A1*s+A2*s*s+A3*s*s*s)

def nodal_transfer(frequency):
    s = 2j*np.pi*frequency
    g1, g2, g3 = 1/R1, 1/R2, 1/R3
    matrix = np.array([[g1+g2+s*C1,-g2,0],
                       [-g2,g2+g3+s*C2,-g3-s*C2],
                       [0,-g3,g3+s*C3]],complex)
    return np.linalg.solve(matrix,np.array([g1,0,0]))[2]

def main():
    # Compare the reduced transfer function with independent node equations.
    for f in [0,20,1000,10000,20000,50000,100000]:
        assert abs(transfer(f)-nodal_transfer(f)) < 1e-10
    cutoff = brentq(lambda f:abs(transfer(f))-1/np.sqrt(2),1,1e6)
    samples = [20,1000,10000,20000,40000,50000,100000]
    results = dict(
        model='Current Rev A three-pole low-pass, ideal unity-gain buffer; analytical, not measured',
        resistors_ohms=[R1,R2,R3],capacitors_farads=[C1,C2,C3],
        denominator_coefficients_seconds=[1,A1,A2,A3],minus_3_db_hz=cutoff,
        points=[dict(frequency_hz=f,gain_v_per_v=float(abs(transfer(f))),
                     gain_db=float(20*np.log10(abs(transfer(f))))) for f in samples],
        first_order_estimates_hz=dict(input_rf=1/(2*np.pi*1000*150e-12),
            low_source_impedance_input_coupling=1/(2*np.pi*2.2e6*100e-9),
            adc_reference_input_supply_filter=1/(2*np.pi*49.9*10e-6),
            analog_regulator_input_filter=1/(2*np.pi*10*22e-6),
            adc_differential_input_pair=1/(2*np.pi*2000*150e-12),
            midpoint_divider_filter=1/(2*np.pi*500*22e-6)))
    (ROOT/'nominal_filter_results.json').write_text(json.dumps(results,indent=2)+'\n')
    f=np.logspace(np.log10(10),np.log10(300000),1000)
    h=transfer(f)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                         'axes.labelcolor':'#243449','text.color':'#243449',
                         'xtick.color':'#425367','ytick.color':'#425367',
                         'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(2,1,figsize=(11,6.6),sharex=True,
                          gridspec_kw={'height_ratios':[1.65,1]},layout='constrained')
    fig.patch.set_facecolor('white')
    for ax in axes:
        ax.axvspan(20,20000,color='#1a6376',alpha=.07)
        ax.set_xscale('log')
        ax.grid(which='major',alpha=.20)
        ax.grid(which='minor',alpha=.055)
        ax.axvline(cutoff,color='#a86c24',ls='--',lw=1.2)
    axes[0].plot(f,20*np.log10(np.abs(h)),color='#183e60',lw=2.4,
                 label='One ADC/DAC low-pass stage — ideal buffer')
    axes[0].axhline(-3.0103,color='#687786',ls=':',lw=1)
    axes[0].scatter([20000],[20*np.log10(abs(transfer(20000)))],s=36,color='#1a6376',zorder=5)
    axes[0].annotate('20 kHz: −1.21 dB',xy=(20000,-1.2075),xytext=(1700,-16),
                    arrowprops={'arrowstyle':'-','color':'#1a6376'},color='#1a6376')
    axes[0].text(1.04*cutoff,-30,f'−3 dB at {cutoff/1000:.2f} kHz',color='#8d5b1e')
    axes[0].set_ylim(-70,4)
    axes[0].set_ylabel('Magnitude (dB)')
    axes[0].legend(loc='lower left',frameon=False)
    axes[1].plot(f,np.unwrap(np.angle(h))*180/np.pi,color='#1a6376',lw=2)
    axes[1].set_ylabel('Phase (degrees)')
    axes[1].set_xlabel('Frequency (Hz)')
    axes[1].set_xlim(10,300000)
    fig.suptitle('SPECTRA MX-1 · Rev A nominal low-pass response',fontsize=17,fontweight='bold')
    axes[0].set_title('Calculated from PCB values; shaded band = 20 Hz–20 kHz target',fontsize=10,loc='left',pad=9)
    destination=ROOT.parent/'media/nominal-filter-response.svg'
    fig.savefig(destination)
    plt.close(fig)
    print('Verified nodal/polynomial agreement. −3 dB:',round(cutoff,3),'Hz.')
    print('Wrote',destination.name,'and nominal_filter_results.json.')

if __name__=='__main__':
    main()
