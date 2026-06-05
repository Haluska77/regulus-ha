REGISTRY_MAPPER = {
    # dashboard / schema
    "outdoorTemperature": "__R3620_REAL_.1f",

    # dashboard aliases / heat pump
    # These registers are available on /1_sch.xml.
    "heatPumpRunningStatus": "__R7720.0_BOOL_i",
    "heatPumpOutletTemperature": "__R7714_INT_-4.1d",
    "heatPumpInletTemperature": "__R7712_INT_-4.1d",

    "rcTariff": "__R3928.1_BOOL_i",
    "holiday": "__R3928.4_BOOL_i",

    # Dashboard circulation/status candidate.
    "circulationRunningStatus": "__R18489.0_BOOL_i",

    # zone1 / dashboard + ZO_Z1.XML
    "zone1RunningStatus": "__R7720.3_BOOL_i",
    "zone1RequiredTemperature": "__R126378_REAL_.1f",
    "zone1HeatingWaterTemperature": "__R3676_REAL_.1f",
    "zone1RequiredHeatingWaterTemperature": "__R3782_REAL_.1f",

    # zone2 / dashboard + ZO_Z2.XML
    "zone2RunningStatus": "__R7720.1_BOOL_i",
    "zone2Temperature": "__R3810_REAL_.1f",
    "zone2RequiredTemperature": "__R126400_REAL_.1f",
    "zone2HeatingWaterTemperature": "__R3684_REAL_.1f",
    "zone2RequiredHeatingWaterTemperature": "__R3786_REAL_.1f",

    # aku / buffer
    "akuTopTemperature": "__R3628_REAL_.1f",
    "akuBottomTemperature": "__R3742_REAL_.1f",
    "akuRequiredTemperature": "__R18049_SINT_d",
    "akuRunningStatusFromHeatPump": "__R5434.0_BOOL_i",

    # solar
    "solarPanelTemperature": "__R10014_REAL_.1f",
    "solarRunningStatus": "__Y794.0_BOOL_i",

    # heat pump / ZD_T.XML
    "hpRunningTime": "__R28020_TIME_Thh:mm:ss",
    "hpIdleTime": "__R28032_TIME_Thh:mm:ss",

    "overallTotalHours": "__R27994_UDINT_u",
    "overallTotalStarts": "__R28004_UINT_u",

    "overallTodayHours": "__R27966_USINT_u",
    "overallTodayMinutes": "__R27967_UINT_u",
    "overallTodayStarts": "__R28006_USINT_u",

    "overallYesterdayHours": "__R27988_USINT_u",
    "overallYesterdayMinutes": "__R27989_UINT_u",
    "overallYesterdayStarts": "__R28007_USINT_u",

    "hotWaterTotalHours": "__R27998_UDINT_u",
    "hotWaterTotalStarts": "__R28008_UINT_u",

    "hotWaterTodayHours": "__R27973_USINT_u",
    "hotWaterTodayMinutes": "__R27974_UINT_u",
    "hotWaterTodayStarts": "__R28010_USINT_u",

    "hotWaterYesterdayHours": "__R27991_USINT_u",
    "hotWaterYesterdayMinutes": "__R27992_UINT_u",
    "hotWaterYesterdayStarts": "__R28011_USINT_u",

    "hpRunningStatus": "__R29284.0_BOOL_i",
    "hpCompressorSpeed": "__R27682_INT_-5.1d",
    "hpStatusText": "__R25147_STRING[20]_s",
    "hpOutletTemperature": "__R27450_INT_-5.1d",
    "hpInletTemperature": "__R27446_INT_-5.1d",

    # home
    "zone1SummerMode": "__R15008.0_BOOL_i",
    "zone2SummerMode": "__R18312.0_BOOL_i",

    # water / dashboard + TV_TC.XML
    "waterState": "__R23439.0_BOOL_i",
    "waterRunningStatusFromHeatPump": "__R18489.0_BOOL_i",
    "waterSwitchingSensorTemperature": "__R3680_REAL_.1f",
    "waterRequiredTemperature": "__R23460_REAL_.0f",
    "waterComfortTemperature": "__R23478_SINT_d",
    "waterSetbackTemperature": "__R23464_SINT_d",

    "waterOneTimeHeatingTemperature": "__R3858_INT_d",
    "waterOneTimeHeatingState": "__R23479.0_BOOL_i",

    # zone1 / ZO_Z1.XML + schema
    "zone1State": "__R14788.0_BOOL_i",
    "zone1Temperature": "__R3806_REAL_.1f",
    "zone1DesiredTemperature": "__R14802_REAL_.1f",

    # zone2 / ZO_Z2.XML + schema
    "zone2State": "__R18092.0_BOOL_i",
    "zone2Temperature": "__R3810_REAL_.1f",
    "zone2DesiredTemperature": "__R18106_REAL_.1f",

    # aku
    "akuState": "__R18048.0_BOOL_i",
    "akuComfortTemperature": "__R18049_SINT_d",
    "akuSetbackTemperature": "__R18052_SINT_d",
}
