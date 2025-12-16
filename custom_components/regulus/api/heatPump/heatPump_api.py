from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass

from ...schema import deviceSensor
from .heatPump_schemas import HeatPumpResponseSchema
from ...service.abstract_api import AbstractApi

class HeatPumpApi(AbstractApi[HeatPumpResponseSchema]):
    page = "/zd_t.xml"
    key = "heatPump"
    name = "Heat Pump"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> HeatPumpResponseSchema:

        return HeatPumpResponseSchema(
            runningTime = deviceSensor("Heat Pump Running Time", "hpRunningTime", None, None, "mdi:clock-outline", 
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            idleTime = deviceSensor("Heat Pump Idle Time", "hpIdleTime", None, None, "mdi:clock-outline", 
                                      Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTotalHours = deviceSensor("Heat Pump Overall Total Hours", "overallTotalHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTotalStarts = deviceSensor("Heat Pump Overall Total Starts", "overallTotalStarts", None, None, "mdi:chart-box-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayHours = deviceSensor("Heat Pump Overall Today Hours", "overallTodayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                      Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayMinutes = deviceSensor("Heat Pump Overall Today Minutes", "overallTodayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayStarts = deviceSensor("Heat Pump Overall Today Starts", "overallTodayStarts", None, None, "mdi:chart-box-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayHours = deviceSensor("Heat Pump Overall Yesterday Hours", "overallYesterdayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayMinutes = deviceSensor("Heat Pump Overall Yesterday Minutes", "overallYesterdayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayStarts = deviceSensor("Heat Pump Overall Yesterday Starts", "overallYesterdayStarts", None, None, "mdi:chart-box-outline", 
                                                            Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTotalHours = deviceSensor("Heat Pump Hot Water Total Hours", "hotWaterTotalHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTotalStarts = deviceSensor("Heat Pump Hot Water Total Starts", "hotWaterTotalStarts", None, None, "mdi:chart-box-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayHours = deviceSensor("Heat Pump Hot Water Today Hours", "hotWaterTodayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayMinutes = deviceSensor("Heat Pump Hot Water Today Minutes", "hotWaterTodayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                          Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayStarts = deviceSensor("Heat Pump Hot Water Today Starts", "hotWaterTodayStarts", None, None, "mdi:chart-box-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayHours = deviceSensor("Heat Pump Hot Water Yesterday Hours", "hotWaterYesterdayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                            Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayMinutes = deviceSensor("Heat Pump Hot Water Yesterday Minutes", "hotWaterYesterdayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                              Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayStarts = deviceSensor("Heat Pump Hot Water Yesterday Starts", "hotWaterYesterdayStarts", None, None, "mdi:chart-box-outline", 
                                                             Platform.SENSOR, schema_xml_map, registry_mapper),
        )
