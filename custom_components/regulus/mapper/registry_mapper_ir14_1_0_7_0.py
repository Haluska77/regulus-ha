# IR RegulusBOX CTC, firmware v1.0.7.0 (18.11.2022)
# Based on 14_1_0_5_0; registers verified against live XML pages and their XSL layout.
REGISTRY_MAPPER = {
    # dashboard (1_sch.xml)
    "outdoorTemperature": "__TD9939790_REAL_.1f",
    "rcTariff": "__TD13A3D01_BOOL_i",                         # HDO TARIF: 1 = NÍZKÝ, 0 = VYSOKÝ
    "holiday": "__T73B9F794_BOOL_i",                          # PRÁZDNINY: 1 = ZAPNUTO

    "heatPumpOutletTemperature": "__TB483374B_INT_-4.1d",
    "heatPumpInletTemperature": "__T017CD4D4_INT_-4.1d",

    "heatPumpRunningStatus": "__TDD6C3C33_BOOL_i",                # compressor running (CHODTC animation)
    "waterRunningStatusFromHeatPump": "__T079D123F_BOOL_i",       # heat pump heating hot water
    # circulationRunningStatus: no reliable register found on this page (left unmapped)

    # source 1 = electric heater box next to zones ("38.5 (21.2)" in schema)
    "source1HeatingDemandTemperature": "__TA0930ABD_REAL_.1f",
    "source1Temperature": "__TA92B3DFB_REAL_.1f",
    "systemPressure": "__T0769CFB6_REAL_.1f",                  # TLAK V ÚT [bar]
    "waterElectricRequiredTemperature": "__T164E9E3A_REAL_.1f",  # TV required for el. heater
    "akuElectricRequiredTemperature": "__T3C9A6C6F_REAL_.1f",    # AKU required for el. heater

    # zone 1 (zo_z1.xml + 1_sch.xml)
    "zone1State": "__T70EB7FD7_BOOL_i",                       # STAV ZÓNY toggle
    "zone1RunningStatus": "__TC92DBF6B_USINT_u",           # zone 1 pump (CERPTE animation)
    "zone1Temperature": "__T0D2D20BE_REAL_.1f",               # room temperature
    "zone1DesiredTemperature": "__TAB57C719_REAL_.1f",        # required room temperature
    "zone1RequiredTemperature": "__TAB57C719_REAL_.1f",
    "zone1HeatingWaterTemperature": "__T023DCDC1_REAL_.1f",   # heating water actual
    "zone1RequiredHeatingWaterTemperature": "__TEFD93FC9_REAL_.1f",
    "zone1Humidity": "__T99E98E2F_REAL_.1f",                   # RELATIVNÍ VLHKOST (room unit, zo_z1.xml)

    # zone 2 (zo_z2.xml + 1_sch.xml)
    "zone2State": "__T223EFAE9_BOOL_i",                       # STAV ZÓNY toggle
    "zone2RunningStatus": "__T9BF89A03_USINT_u",           # zone 2 pump (CERPTE animation)
    "zone2Temperature": "__TCE6F726B_REAL_.1f",               # room temperature
    "zone2DesiredTemperature": "__T8E3F09A9_REAL_.1f",        # required room temperature
    "zone2RequiredTemperature": "__T8E3F09A9_REAL_.1f",
    "zone2HeatingWaterTemperature": "__T50E8CD1A_REAL_.1f",   # heating water actual
    "zone2RequiredHeatingWaterTemperature": "__TC7F7F179_REAL_.1f",

    # AKU (1_sch.xml)
    "akuTopTemperature": "__T0E597DEC_REAL_.1f",
    "akuBottomTemperature": "__T4C9005EA_REAL_.1f",           # 0.0 when no bottom sensor is installed
    "akuRequiredTemperature": "__TA629D846_REAL_.1f",
    "akuRunningStatusFromHeatPump": "__T4A0762FD_BOOL_i",       # heat pump heating AKU / heating circuit
    # AKU zone (zo_aku.xml)
    "akuState": "__TF08F905B_BOOL_i",                         # STAV ZÓNY toggle
    "akuComfortTemperature": "__TD188ECEF_USINT_u",
    "akuSetbackTemperature": "__T6A04C910_USINT_u",

    # NOTE: no solar on this firmware layout. __T0769CFB6 (mapped as solar in 1.0.5.0)
    # is system pressure, __T42B96F25 is the "pressure sensor present" flag.

    # water (tv_tc.xml + 1_sch.xml)
    "waterState": "__T326B0D57_BOOL_i",
    "waterSwitchingSensorTemperature": "__T29E0FB9B_REAL_.1f",
    "waterRequiredTemperature": "__T8C9AFCC2_INT_d",
    "waterComfortTemperature": "__T4AB99A35_REAL_.0f",
    "waterSetbackTemperature": "__T5A4C89A5_REAL_.0f",

    # heat pump statistics (zd_t.xml)
    "hpRunningTime": "__T7E09363F_TIME_Thh:mm:ss",
    "hpIdleTime": "__TCCDFB758_TIME_Thh:mm:ss",
    "overallTotalHours": "__T2FC939AD_UDINT_u",
    "overallTotalStarts": "__T0502AE4E_UINT_u",
    "overallTodayHours": "__T93D9B267_USINT_u",
    "overallTodayMinutes": "__T3E2DE708_UINT_u",
    "overallTodayStarts": "__T884463DE_USINT_u",
    "overallYesterdayHours": "__T0583680F_USINT_u",
    "overallYesterdayMinutes": "__TA87722EF_UINT_u",
    "overallYesterdayStarts": "__T5F43F9C4_USINT_u",
    "hotWaterTotalHours": "__T56A73D11_UDINT_u",
    "hotWaterTotalStarts": "__T99AE3B59_UINT_u",
    "hotWaterTodayHours": "__T1F554C11_USINT_u",
    "hotWaterTodayMinutes": "__TB2A1ECA9_UINT_u",
    "hotWaterTodayStarts": "__TF12A2D8E_USINT_u",
    "hotWaterYesterdayHours": "__T992F531F_USINT_u",
    "hotWaterYesterdayMinutes": "__T34DBF26F_UINT_u",
    "hotWaterYesterdayStarts": "__T13391633_USINT_u",
}
