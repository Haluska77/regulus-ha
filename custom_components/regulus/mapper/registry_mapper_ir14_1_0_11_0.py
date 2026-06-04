# Mapper for Regulus IR 14, firmware 1.0.11.0 (RegulusBOX, TECO Foxtrot,
# local web login uzivatel/uzivatel). This firmware's PLC register bank does
# not overlap any shipped mapper (0/54 vs 12_04_10, 14_1_0_5_0, 14_1_0_10_0),
# so all entities read "unknown" without it. Reverse-engineered from the
# controller's XSL label geometry + live values, and cross-validated against
# the Regulus IR Client app's labelled readings.
#
# Status: iteration 2 — temperatures, states, timers, and the full heat-pump
# statistics block, all validated live on HA. Remaining: zone/water/aku on-off
# states, comfort/setback schedule temps, solar, dashboard status bits.
#
# NOTE: dashboard-section keys MUST reference registers present on /1_sch.xml.
REGISTRY_MAPPER = {
  # --- dashboard (page /1_sch.xml) ---
  "outdoorTemperature": "__R10416_REAL_.1f",                 # VENKOVNÍ TEPLOTA
  "heatPumpOutletTemperature": "__R14324_INT_-4.1d",         # VÝSTUPNÍ TEPLOTA (~50.6, outlet)
  "heatPumpInletTemperature": "__R14322_INT_-4.1d",          # VSTUPNÍ TEPLOTA (~44.6, inlet)
  "zone1HeatingWaterTemperature": "__R10392_REAL_.1f",       # TEPLOTA OTOPNÉ VODY z1
  "zone2HeatingWaterTemperature": "__R10396_REAL_.1f",       # TEPLOTA OTOPNÉ VODY z2
  "akuTopTemperature": "__R10238_REAL_.1f",                  # TEPLOTA AKUMULAČNÍ NÁDRŽE (=0.0, no tank)

  # --- heat pump (page /zd_t.xml) --- validated vs IR Client "CELKOVÉ STATISTIKY" / "TEPLÁ VODA"
  "hpRunningTime": "__R33994_TIME_Thh:mm:ss",                # TČ BĚŽÍ JIŽ
  "hpIdleTime": "__R34006_TIME_Thh:mm:ss",                   # TČ STOJÍ JIŽ
  "overallTotalHours": "__R33968_UDINT_u",                   # CELKEM hours (3166)
  "overallTotalStarts": "__R33978_UINT_u",                   # CELKEM POČET STARTŮ (3395)
  "overallTodayHours": "__R33940_USINT_u",                   # DNEŠNÍ DEN hours (0)
  "overallTodayMinutes": "__R33941_UINT_u",                  # DNEŠNÍ DEN minutes (53)
  "overallTodayStarts": "__R33980_USINT_u",                  # DNEŠNÍ DEN starts (3)
  "overallYesterdayHours": "__R33962_USINT_u",               # VČEREJŠÍ DEN hours (1)
  "overallYesterdayMinutes": "__R33963_UINT_u",              # VČEREJŠÍ DEN minutes (45)
  "overallYesterdayStarts": "__R33981_USINT_u",              # VČEREJŠÍ DEN starts (4)
  "hotWaterTotalHours": "__R33972_UDINT_u",                  # TEPLÁ VODA CELKEM hours (834)
  "hotWaterTotalStarts": "__R33982_UINT_u",                  # TEPLÁ VODA starts (1930)
  "hotWaterTodayHours": "__R33947_USINT_u",                  # TV DNEŠNÍ hours (0)
  "hotWaterTodayMinutes": "__R33948_UINT_u",                 # TV DNEŠNÍ minutes (53)
  "hotWaterTodayStarts": "__R33984_USINT_u",                 # TV DNEŠNÍ starts (3)
  "hotWaterYesterdayHours": "__R33965_USINT_u",              # TV VČEREJŠÍ hours (1)
  "hotWaterYesterdayMinutes": "__R33966_UINT_u",             # TV VČEREJŠÍ minutes (45)
  "hotWaterYesterdayStarts": "__R33985_USINT_u",             # TV VČEREJŠÍ starts (4)

  # --- water (page /tv_tc.xml) ---
  "waterSwitchingSensorTemperature": "__R10290_REAL_.1f",    # TEPLOTA TV (live)
  "waterRequiredTemperature": "__R10468_INT_d",              # TEPLOTA TV required (=49)
  "waterComfortTemperature": "__R29526_REAL_.0f",            # comfort setpoint (=50)

  # --- zone1 (page /zo_z1.xml) ---
  "zone1State": "__R20806.0_BOOL_i",                         # STAV ZÓNY
  "zone1Temperature": "__R20836_REAL_.1f",                   # POKOJOVÁ TEPLOTA (=-1.0, likely no room sensor)
  "zone1DesiredTemperature": "__R20808_REAL_.1f",            # POŽADOVANÁ TEPLOTA (=22.0)

  # --- zone2 (page /zo_z2.xml) ---
  "zone2Temperature": "__R24181_REAL_.1f",                   # POKOJOVÁ TEPLOTA (=-2.0, likely no room sensor)
  "zone2DesiredTemperature": "__R24153_REAL_.1f",            # POŽADOVANÁ TEPLOTA (=22.0)
}
