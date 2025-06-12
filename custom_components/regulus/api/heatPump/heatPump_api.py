from typing import Dict, List
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass

from custom_components.regulus.schema import sensor
from .heatPump_schemas import HeatPumpResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map

class HeatPumpApi(AbstractApi[HeatPumpResponseSchema]):
    page = "/zd_t.xml"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: List[str]) -> HeatPumpResponseSchema:
        print("Successfully fetched `/heatPump` data")
        version = self.config["ir_version"]

        return HeatPumpResponseSchema(
            runningTime = sensor("Heat Pump Running Time", 
                                        get_value_from_map(schema_xml_map, "hpRunningTime", registry_errors, version), 
                                      None, None, "mdi:clock-outline", Platform.SENSOR),
            idleTime = sensor("Heat Pump Idle Time", 
                                        get_value_from_map(schema_xml_map, "hpIdleTime", registry_errors, version), 
                                      None, None, "mdi:clock-outline", Platform.SENSOR),
            overallStatisticsTotalHours = sensor("Heat Pump Overall Total Hours", 
                                        get_value_from_map(schema_xml_map, "overallTotalHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            overallStatisticsTotalStarts = sensor("Heat Pump Overall Total Starts", 
                                        get_value_from_map(schema_xml_map, "overallTotalStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
            overallStatisticsTodayHours = sensor("Heat Pump Overall Today Hours", 
                                        get_value_from_map(schema_xml_map, "overallTodayHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            overallStatisticsTodayMinutes = sensor("Heat Pump Overall Today Minutes", 
                                        get_value_from_map(schema_xml_map, "overallTodayMinutes", registry_errors, version), 
                                      "min", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            overallStatisticsTodayStarts = sensor("Heat Pump Overall Today Starts", 
                                        get_value_from_map(schema_xml_map, "overallTodayStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
            overallStatisticsYesterdayHours = sensor("Heat Pump Overall Yesterday Hours", 
                                        get_value_from_map(schema_xml_map, "overallYesterdayHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            overallStatisticsYesterdayMinutes = sensor("Heat Pump Overall Yesterday Minutes", 
                                        get_value_from_map(schema_xml_map, "overallYesterdayMinutes", registry_errors, version), 
                                      "min", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            overallStatisticsYesterdayStarts = sensor("Heat Pump Overall Yesterday Starts", 
                                        get_value_from_map(schema_xml_map, "overallYesterdayStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
            hotWaterStatisticsTotalHours = sensor("Heat Pump Hot Water Total Hours", 
                                        get_value_from_map(schema_xml_map, "hotWaterTotalHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            hotWaterStatisticsTotalStarts = sensor("Heat Pump Hot Water Total Starts", 
                                        get_value_from_map(schema_xml_map, "hotWaterTotalStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
            hotWaterStatisticsTodayHours = sensor("Heat Pump Hot Water Today Hours", 
                                        get_value_from_map(schema_xml_map, "hotWaterTodayHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            hotWaterStatisticsTodayMinutes = sensor("Heat Pump Hot Water Today Minutes", 
                                        get_value_from_map(schema_xml_map, "hotWaterTodayMinutes", registry_errors, version), 
                                      "min", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            hotWaterStatisticsTodayStarts = sensor("Heat Pump Hot Water Today Starts", 
                                        get_value_from_map(schema_xml_map, "hotWaterTodayStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
            hotWaterStatisticsYesterdayHours = sensor("Heat Pump Hot Water Yesterday Hours", 
                                        get_value_from_map(schema_xml_map, "hotWaterYesterdayHours", registry_errors, version), 
                                      "h", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            hotWaterStatisticsYesterdayMinutes = sensor("Heat Pump Hot Water Yesterday Minutes", 
                                        get_value_from_map(schema_xml_map, "hotWaterYesterdayMinutes", registry_errors, version), 
                                      "min", SensorDeviceClass.DURATION, "mdi:timer-outline", Platform.SENSOR),
            hotWaterStatisticsYesterdayStarts = sensor("Heat Pump Hot Water Yesterday Starts", 
                                        get_value_from_map(schema_xml_map, "hotWaterYesterdayStarts", registry_errors, version), 
                                      "", "none", "mdi:chart-box-outline", Platform.SENSOR),
        )
