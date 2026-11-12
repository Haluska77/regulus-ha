# Mapper for Regulus IR14RTC, firmware 1.0.11.30 (10.10.2026), TECO platform,
# local web login with a user-level account. Register bank differs from every shipped
# mapper (1.0.11.16: 4/93 names present, 1.0.11.4: 1/61, 1.0.11.0: 0/32);
# analog temperatures are mostly shifted by +54 against 1.0.11.16.
#
# Derived from the page descriptors served at /DESC/<PAGE>.XMD (UTF-8, request
# header "x-tecomat: data"): every field carries its register in `_f` plus X/Y
# coordinates, so each register was paired with the label on the same row,
# then checked against live XML values and the controller display.
#
# With a user-level account the controller strips some fields from the
# descriptors and XML: heat pump statistics (zd_t.xml exposes only 3 bits),
# water on/off and water comfort/setback. Those keys, and status bits that
# could not be identified with confidence, are intentionally omitted.
REGISTRY_MAPPER = {
  # dashboard
  "outdoorTemperature": "__R4114_REAL_.1f",
  "holiday": "__R4113.1_BOOL_i",
  "heatPumpOutletTemperature": "__R9258_INT_-4.1d",
  "heatPumpInletTemperature": "__R9256_INT_-4.1d",
  "circulationRunningStatus": "__R29179.0_BOOL_i",
  "zone1RequiredTemperature": "__R4300_REAL_.1f",
  "zone1HeatingWaterTemperature": "__R4170_REAL_.1f",
  "zone1RequiredHeatingWaterTemperature": "__R4276_REAL_.1f",
  "zone2RequiredTemperature": "__R4304_REAL_.1f",
  "zone2HeatingWaterTemperature": "__R4178_REAL_.1f",
  "zone2RequiredHeatingWaterTemperature": "__R4280_REAL_.1f",
  "akuTopTemperature": "__R4122_REAL_.1f",
  "akuBottomTemperature": "__R4236_REAL_.1f",
  "akuRequiredTemperature": "__R4264_REAL_.1f",

  # water
  "waterSwitchingSensorTemperature": "__R4174_REAL_.1f",
  "waterRequiredTemperature": "__R4352_INT_d",

  # zone1
  "zone1State": "__R25121.0_BOOL_i",
  "zone1ServiceEnabled": "__R25121.1_BOOL_i",
  "zone1Temperature": "__R109786_REAL_.1f",
  "zone1DesiredTemperature": "__R25125_REAL_.1f",
  "zone1Humidity": "__R109794_REAL_.1f",

  # zone2
  "zone2State": "__R28690.0_BOOL_i",
  "zone2ServiceEnabled": "__R28690.1_BOOL_i",
  "zone2Temperature": "__R109808_REAL_.1f",
  "zone2DesiredTemperature": "__R28694_REAL_.1f",

  # aku
  "akuState": "__R28646.0_BOOL_i",
  "akuServiceEnabled": "__R28646.1_BOOL_i",
  "akuComfortTemperature": "__R28647_SINT_d",
  "akuSetbackTemperature": "__R28650_SINT_d",
}
