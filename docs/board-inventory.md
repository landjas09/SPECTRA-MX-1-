# Rev A board inventory

Extracted from MixedSignal_Analyzer_Generator.kicad_pcb. This is a **draft board inventory**, not a finalized procurement BOM. Nominal values and imported manufacturer/order-code fields are preserved without selecting replacement parts.

The source has 110 electrical positions, four mounting-hole footprints and two artwork footprints. C106 is labeled DNP in its value while its PCB attributes omit the DNP flag. The PCB provides 45 capacitor, 36 resistor, four inductor/choke, nine diode/LED, 11 IC, four connector and one crystal positions.

Manufacturer fields were normalized from Manufacturer, Manufacturer_Name, MF and MANUFACTURER. Ordering fields were normalized from Manufacturer Part Number, Manufacturer_Part_Number and MP. A dash means no populated source field was available; a named value may still identify a device family or part.

| Reference | Value in PCB | Footprint identifier | Imported manufacturer | Imported part field | Population indication |
| --- | --- | --- | --- | --- | --- |
| C100 | 1u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C101 | 1u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C102 | 22u | Capacitor_SMD:C_0805_2012Metric | — | — | No DNP flag |
| C103 | 22u | Capacitor_SMD:C_0805_2012Metric | — | — | No DNP flag |
| C104 | 22u | Capacitor_SMD:C_0805_2012Metric | — | — | No DNP flag |
| C105 | 22u | Capacitor_SMD:C_0805_2012Metric | — | — | No DNP flag |
| C106 | DNP | Capacitor_SMD:C_0402_1005Metric | — | — | DNP value; flag absent |
| C107 | 22u | Capacitor_SMD:C_0805_2012Metric | — | — | No DNP flag |
| C108 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C200 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C201 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C202 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C203 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C204 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C205 | 10n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C206 | 1u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C207 | 1u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C208 | 10p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C209 | 10p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C210 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C211 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C212 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C300 | 150p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C301 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C302 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C303 | 1n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C304 | 150p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C305 | 1n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C306 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C307 | 150p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C308 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C309 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C310 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C311 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C312 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C313 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C314 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C315 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C400 | 10u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C401 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C402 | 1u | Capacitor_SMD:C_0603_1608Metric | — | — | No DNP flag |
| C403 | 1n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C404 | 150p | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C405 | 100n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| C406 | 1n | Capacitor_SMD:C_0402_1005Metric | — | — | No DNP flag |
| D100 | GREEN | LED_SMD:LED_0603_1608Metric | — | — | No DNP flag |
| D200 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D201 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D203 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D204 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D205 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D206 | LED_ARGB | LED_SMD:LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100 | — | — | No DNP flag |
| D300 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| D400 | CDSOD323-T03C | Footprints:SOD2513X114N | Bourns | CDSOD323-T03C | No DNP flag |
| J200 | Conn_02x05_Odd_Even | Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical | — | — | No DNP flag |
| J201 | USB_C_Receptacle_USB2.0_16P | Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal | — | — | No DNP flag |
| J300 | Conn_Coaxial | Connector_Coaxial:BNC_Amphenol_B6252HB-NPP3G-50_Horizontal | — | — | No DNP flag |
| J400 | Conn_Coaxial | Connector_Coaxial:BNC_Amphenol_B6252HB-NPP3G-50_Horizontal | — | — | No DNP flag |
| L100 | 100n | Inductor_SMD:L_0402_1005Metric | — | — | No DNP flag |
| L101 | MWSA0603S-150MT | Footprints:INDM7066X300N | Shenzhen Sunlord Electronics Co., Ltd. | MWSA0603S-150MT | No DNP flag |
| L200 | CMF3216F-900-2P-T | Footprints:CMC-1206 | — | — | No DNP flag |
| L201 | 10n | Inductor_SMD:L_0402_1005Metric | — | — | No DNP flag |
| R100 | 10R | Resistor_SMD:R_0805_2012Metric | — | — | No DNP flag |
| R101 | 100k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R102 | 22k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R103 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R104 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R105 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R200 | 10k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R201 | 0R | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R202 | 10k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R203 | 10k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R204 | 1k5 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R205 | 5k1 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R206 | 5k1 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R207 | 1K | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R208 | 1K | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R209 | 1K | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R210 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R211 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R212 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R213 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R300 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R301 | 2M2 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R302 | 2M2 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R303 | 6k8 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R304 | 22k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R305 | 12k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R306 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R307 | 1k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R308 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R309 | 0R | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R400 | 0R | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R401 | 6k8 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R402 | 10k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R403 | 22k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R404 | 12k | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| R405 | 49R9 | Resistor_SMD:R_0402_1005Metric | — | — | No DNP flag |
| U100 | TLV62569DBVR | Footprints:TLV-SOT95P280X145-5N | Texas Instruments | TLV62569DBVR | No DNP flag |
| U101 | HT7533-1 | Footprints:LDO-SOT89 | UMW | HT7533-1 | No DNP flag |
| U102 | MCP6001U | Package_TO_SOT_SMD:SOT-23-5 | — | — | No DNP flag |
| U200 | STM32F103CBTx | Footprints:STM-LQFP-48_7x7mm_P0.5mm | STMicroelectronics | STM32F103CBT6 | No DNP flag |
| U201 | USBLC6-2SC6 | Package_TO_SOT_SMD:SOT-23-6 | — | — | No DNP flag |
| U300 | MCP6001U | Package_TO_SOT_SMD:SOT-23-5 | — | — | No DNP flag |
| U301 | MCP6001U | Package_TO_SOT_SMD:SOT-23-5 | — | — | No DNP flag |
| U302 | ADC141S626CIMM/NOPB | Footprints:SOIC-10-adc141s626 | — | — | No DNP flag |
| U303 | REF3033 | Package_TO_SOT_SMD:SOT-23 | — | — | No DNP flag |
| U400 | DAC7563SDGSR | Footprints:SOIC-10-adc141s626 | — | — | No DNP flag |
| U401 | MCP6001U | Package_TO_SOT_SMD:SOT-23-5 | — | — | No DNP flag |
| Y200 | 16Mhz | Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm | — | — | No DNP flag |

## Mechanical and artwork records

| Reference / identifier | Source footprint | Purpose |
| --- | --- | --- |
| M04 | MountingHole:MountingHole_3.2mm_M3 | Non-plated mounting hole |
| M02 | MountingHole:MountingHole_3.2mm_M3 | Non-plated mounting hole |
| M03 | MountingHole:MountingHole_3.2mm_M3 | Non-plated mounting hole |
| M01 | MountingHole:MountingHole_3.2mm_M3 | Non-plated mounting hole |
| landjas09_QR_GitHub_16mm_WhiteSilk | Footprints:landjas09_QR_GitHub_16mm_WhiteSilk | Silkscreen artwork |
| SPECTRA_MX1_20mm | Footprints:SPECTRA_MX1_20mm | Silkscreen artwork |

Before assembly, complete exact manufacturer/order codes, electrical ratings, tolerances, quantity/population controls and procurement fields. Generic source values do not guarantee a particular component is suitable for the circuit.
