from typing import Dict
from ..util import latin_to_cp1250_converter
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass


from ..schema import deviceSensor
from .heatPump_schemas import HeatPumpResponseSchema
from ...service.abstract_api import AbstractApi

class HeatPumpApi(AbstractApi[HeatPumpResponseSchema]):
    page = "/zd_t.xml"
    key = "heatPump"
    name = "Heat Pump"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> HeatPumpResponseSchema:

        return HeatPumpResponseSchema(
            state = deviceSensor("State", "hpState", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            serviceEnabled = deviceSensor("Service Enabled", "hpServiceEnabled", "", "none", "mdi:check-circle", 
                                            Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            status = deviceSensor("Status", "hpStatus", None, None, "mdi:heat-pump",
                                  Platform.SENSOR, schema_xml_map, registry_mapper, converter=latin_to_cp1250_converter),
            compressorSpeed = deviceSensor("Compressor Speed", "hpCompressorSpeed", "rps", None, "mdi:speedometer",
                                           Platform.SENSOR, schema_xml_map, registry_mapper),
            runningTime = deviceSensor("Running Time", "hpRunningTime", None, None, "mdi:clock-outline", 
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            idleTime = deviceSensor("Idle Time", "hpIdleTime", None, None, "mdi:clock-outline", 
                                      Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTotalHours = deviceSensor("Overall Total Hours", "overallTotalHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTotalStarts = deviceSensor("Overall Total Starts", "overallTotalStarts", None, None, "mdi:chart-box-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayHours = deviceSensor("Overall Today Hours", "overallTodayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                      Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayMinutes = deviceSensor("Overall Today Minutes", "overallTodayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsTodayStarts = deviceSensor("Overall Today Starts", "overallTodayStarts", None, None, "mdi:chart-box-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayHours = deviceSensor("Overall Yesterday Hours", "overallYesterdayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayMinutes = deviceSensor("Overall Yesterday Minutes", "overallYesterdayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            overallStatisticsYesterdayStarts = deviceSensor("Overall Yesterday Starts", "overallYesterdayStarts", None, None, "mdi:chart-box-outline", 
                                                            Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTotalHours = deviceSensor("Hot Water Total Hours", "hotWaterTotalHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTotalStarts = deviceSensor("Hot Water Total Starts", "hotWaterTotalStarts", None, None, "mdi:chart-box-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayHours = deviceSensor("Hot Water Today Hours", "hotWaterTodayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayMinutes = deviceSensor("Hot Water Today Minutes", "hotWaterTodayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                          Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsTodayStarts = deviceSensor("Hot Water Today Starts", "hotWaterTodayStarts", None, None, "mdi:chart-box-outline", 
                                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayHours = deviceSensor("Hot Water Yesterday Hours", "hotWaterYesterdayHours", "h", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                            Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayMinutes = deviceSensor("Hot Water Yesterday Minutes", "hotWaterYesterdayMinutes", "min", SensorDeviceClass.DURATION, "mdi:timer-outline", 
                                                              Platform.SENSOR, schema_xml_map, registry_mapper),
            hotWaterStatisticsYesterdayStarts = deviceSensor("Hot Water Yesterday Starts", "hotWaterYesterdayStarts", None, None, "mdi:chart-box-outline", 
                                                             Platform.SENSOR, schema_xml_map, registry_mapper),
        )
