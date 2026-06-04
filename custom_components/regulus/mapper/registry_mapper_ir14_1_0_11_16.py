REGISTRY_MAPPER = {
    # dashboard / schema
    "outdoorTemperature": "__R4060_REAL_.1f",
    "rcTariff": "__R8190.0_BOOL_i",
    "holiday": "__R20305.0_BOOL_i",

    "circulationRunningStatus": "__R8180.0_BOOL_i",

    "zone1RunningStatus": "__R16645_USINT_u",
    "zone1RequiredTemperature": "__R4246_REAL_.1f",
    "zone1HeatingWaterTemperature": "__R4222_REAL_.1f",
    "zone1RequiredHeatingWaterTemperature": "__R111174_REAL_.1f",

    "zone2RunningStatus": "__R19959_USINT_u",
    "zone2Temperature": "__R4124_REAL_.1f",
    "zone2RequiredTemperature": "__R4250_REAL_.1f",
    "zone2HeatingWaterTemperature": "__R4226_REAL_.1f",
    "zone2RequiredHeatingWaterTemperature": "__R111196_REAL_.1f",

    "akuTopTemperature": "__R4068_REAL_.1f",
    "akuBottomTemperature": "__R8181_REAL_.1f",
    "akuRequiredTemperature": "__R4210_REAL_.1f",
    "akuRunningStatusFromHeatPump": "__R8220.1_BOOL_i",

    "solarPanelTemperature": "__R4194_REAL_.1f",
    "solarRunningStatus": "__Y794.0_BOOL_i",

    # heat pump / ZD_T.XML
    "hpRunningTime": "__R30079_TIME_Thh:mm:ss",
    "hpIdleTime": "__R30091_TIME_Thh:mm:ss",

    "overallTotalHours": "__R30053_UDINT_u",
    "overallTotalStarts": "__R30063_UINT_u",

    "overallTodayHours": "__R30025_USINT_u",
    "overallTodayMinutes": "__R30026_UINT_u",
    "overallTodayStarts": "__R30065_USINT_u",

    "overallYesterdayHours": "__R30047_USINT_u",
    "overallYesterdayMinutes": "__R30048_UINT_u",
    "overallYesterdayStarts": "__R30066_USINT_u",

    "hotWaterTotalHours": "__R30057_UDINT_u",
    "hotWaterTotalStarts": "__R30067_UINT_u",

    "hotWaterTodayHours": "__R30032_USINT_u",
    "hotWaterTodayMinutes": "__R30033_UINT_u",
    "hotWaterTodayStarts": "__R30069_USINT_u",

    "hotWaterYesterdayHours": "__R30050_USINT_u",
    "hotWaterYesterdayMinutes": "__R30051_UINT_u",
    "hotWaterYesterdayStarts": "__R30070_USINT_u",

    "hpRunningStatus": "__R29512.0_BOOL_i",
    "hpCompressorSpeed": "__R29712_INT_-5.1d",
    "hpStatusText": "__R26948_STRING[20]_s",
    "hpOutletTemperature": "__R29480_INT_-5.1d",
    "hpInletTemperature": "__R29476_INT_-5.1d",

    # home
    "zone1SummerMode": "__R25321.1_BOOL_i",
    "zone2SummerMode": "__R25424.1_BOOL_i",

    # water / dashboard + TV_TC
    "waterState": "__R25144.0_BOOL_i",
    "waterSwitchingSensorTemperature": "__R4120_REAL_.1f",
    "waterRequiredTemperature": "__R4298_INT_d",
    "waterComfortTemperature": "__R4298_INT_d",
    "waterSetbackTemperature": "__R25169_SINT_d",
    "waterOneTimeHeatingTemperature": "__R25183_SINT_d",
    "waterOneTimeHeatingState": "__R25184.0_BOOL_i",

    # zone1 / ZO_Z1.XML + schema
    "zone1State": "__R16592.1_BOOL_i",
    "zone1Temperature": "__R4116_REAL_.1f",
    "zone1DesiredTemperature": "__R4246_REAL_.1f",

    # zone2 / ZO_Z2.XML + schema
    "zone2State": "__R19906.1_BOOL_i",
    "zone2Temperature": "__R4124_REAL_.1f",
    "zone2DesiredTemperature": "__R4250_REAL_.1f",

    # aku
    "akuState": "__R8220.1_BOOL_i",
    "akuComfortTemperature": "__R4298_INT_d",
    "akuSetbackTemperature": "__R25169_SINT_d",
}