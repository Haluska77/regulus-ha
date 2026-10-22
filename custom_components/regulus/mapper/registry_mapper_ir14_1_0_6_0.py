# IR RegulusBOX CTC v1.0.6.0 (07.10.2022)
# Verified on a live unit (hydraulic scheme 3: heat pump + DHW tank + 1 heating zone, no AKU/solar/zone 2)
# by toggling each function in the controller web UI and diffing all registry values.
# Same "__T" registry naming as 1.0.5.0, but several registries differ:
#  - zone1Temperature is the room temperature (1.0.5.0 maps it to the heating water temperature)
#  - zone1HeatingWaterTemperature / zone1RequiredHeatingWaterTemperature are actual / required heating water
#  - zone1RunningStatus is __TC92DBF6B (1.0.5.0 maps this registry to zone 2)
#  - holiday / rcTariff taken from the registries the scheme page (3_SCH.XSL) uses for PRAZDNINY / HDO TARIF
#  - waterState is the DHW on/off form field (__TBFA4BBB4), 1.0.5.0's __T326B0D57 stays 0 while DHW is on
# Not available in this firmware: water one-time heating.
# Not mapped (no hardware to verify): zone 2, AKU, solar, fireplace, zone2SummerMode.
REGISTRY_MAPPER = {
    # dashboard (/1_sch.xml)
    "outdoorTemperature": "__TD9939790_REAL_.1f",
    "rcTariff": "__TD13A3D01_BOOL_i",
    "holiday": "__T73B9F794_BOOL_i",

    "heatPumpOutletTemperature": "__TB483374B_INT_-4.1d",
    "heatPumpInletTemperature": "__T017CD4D4_INT_-4.1d",
    "source1HeatingDemandTemperature": "__TA629D846_REAL_.1f",

    "heatPumpRunningStatus": "__TF4121779_BOOL_i",
    "waterRunningStatusFromHeatPump": "__T0E319FDD_BOOL_i",
    "circulationRunningStatus": "__TDCC7F5B7_BOOL_i",

    # zone 1 (dashboard + /zo_z1.xml)
    "zone1RunningStatus": "__TC92DBF6B_USINT_u",
    "zone1State": "__T70EB7FD7_BOOL_i",
    "zone1Temperature": "__T0D2D20BE_REAL_.1f",
    "zone1RequiredTemperature": "__TAB57C719_REAL_.1f",
    "zone1DesiredTemperature": "__TA267F5A5_REAL_.1f",
    "zone1HeatingWaterTemperature": "__T023DCDC1_REAL_.1f",
    "zone1RequiredHeatingWaterTemperature": "__TEFD93FC9_REAL_.1f",

    # home (/home.xml)
    "zone1SummerMode": "__T8DFD1D45_BOOL_i",

    # water (dashboard + /tv_tc.xml)
    "waterState": "__TBFA4BBB4_BOOL_i",
    "waterSwitchingSensorTemperature": "__T29E0FB9B_REAL_.1f",
    "waterRequiredTemperature": "__T8C9AFCC2_INT_d",
    "waterComfortTemperature": "__T4AB99A35_REAL_.0f",
    "waterSetbackTemperature": "__T5A4C89A5_REAL_.0f",

    # heat pump statistics (/zd_t.xml)
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
