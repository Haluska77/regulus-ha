from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass

from custom_components.regulus.schema import sensor
from .dashboard_schemas import DashboardResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map

class DashboardApi(AbstractApi[DashboardResponseSchema]):
    page = "/1_sch.xml"

    def generate_response(self, schema_xml_map: Dict[str, str]) -> DashboardResponseSchema:
        print("Successfully fetched `/dashboard` data")
        version = self.config["ir_version"]

        return DashboardResponseSchema(
            outdoorTemperature = sensor("Outdoor Temperature", 
                                        get_value_from_map(schema_xml_map, "outdoorTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:sun-thermometer-outline", Platform.SENSOR),
            rcTariff = sensor("RC Tariff", 
                                          get_value_from_map(schema_xml_map, "rcTariff", version, converter=lambda v: v == "1"),
                                          "", "none", "mdi:cash-clock", Platform.BINARY_SENSOR),
            holiday = sensor("Holiday", 
                                          get_value_from_map(schema_xml_map, "holiday", version, converter=lambda v: v == "1"),
                                          "", "none", "mdi:beach", Platform.BINARY_SENSOR),
            heatPumpRunningStatus= sensor("Heat Pump Running Status", 
                                          get_value_from_map(schema_xml_map, "heatPumpRunningStatus", version, converter=lambda v: v != "0"),
                                          "", BinarySensorDeviceClass.RUNNING, "mdi:fan", Platform.BINARY_SENSOR),
            heatPumpOutletTemperature = sensor("Heat Pump Outlet Temperature", 
                                        get_value_from_map(schema_xml_map, "heatPumpOutletTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            heatPumpInletTemperature = sensor("Heat Pump Inlet Temperature", 
                                        get_value_from_map(schema_xml_map, "heatPumpInletTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone1Status = sensor("Zone 1 Running Status", 
                                          get_value_from_map(schema_xml_map, "zone1RunningStatus", version, converter=lambda v: v != "0"),
                                          "", BinarySensorDeviceClass.RUNNING, "mdi:heating-coil", Platform.BINARY_SENSOR),
            zone1ActualTemperature = sensor("Zone 1 Actual Temperature", 
                                        get_value_from_map(schema_xml_map, "zone1Temperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone1RequiredTemperature = sensor("Zone 1 Required Temperature", 
                                        get_value_from_map(schema_xml_map, "zone1RequiredTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone1ActualHeatingWaterTemperature = sensor("Zone 1 Heating Water Temperature", 
                                        get_value_from_map(schema_xml_map, "zone1HeatingWaterTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone1RequiredHeatingWaterTemperature = sensor("Zone 1 Required Heating Water Temperature", 
                                        get_value_from_map(schema_xml_map, "zone1RequiredHeatingWaterTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone2Status = sensor("Zone 2 Running Status", 
                                          get_value_from_map(schema_xml_map, "zone2RunningStatus", version, converter=lambda v: v != "0"),
                                          "", BinarySensorDeviceClass.RUNNING, "mdi:radiator", Platform.BINARY_SENSOR),
            zone2ActualTemperature = sensor("Zone 2 Actual Temperature", 
                                        get_value_from_map(schema_xml_map, "zone2Temperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone2RequiredTemperature = sensor("Zone 2 Required Temperature", 
                                        get_value_from_map(schema_xml_map, "zone2RequiredTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone2ActualHeatingWaterTemperature = sensor("Zone 2 Heating Water Temperature", 
                                        get_value_from_map(schema_xml_map, "zone2HeatingWaterTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            zone2RequiredHeatingWaterTemperature = sensor("Zone 2 Required Heating Water Temperature", 
                                        get_value_from_map(schema_xml_map, "zone2RequiredHeatingWaterTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            akuStatus = sensor("Aku Running Status", 
                                          get_value_from_map(schema_xml_map, "akuRunningStatusFromHeatPump", version, converter=lambda v: v == "1"),
                                          "", BinarySensorDeviceClass.RUNNING, "mdi:water-boiler", Platform.BINARY_SENSOR),
            akuTopTemperature = sensor("Aku Top Temperature", 
                                        get_value_from_map(schema_xml_map, "akuTopTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            akuBottomTemperature = sensor("Aku Bottom Temperature", 
                                        get_value_from_map(schema_xml_map, "akuBottomTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            akuRequiredTemperature = sensor("Aku Required Temperature", 
                                        get_value_from_map(schema_xml_map, "akuRequiredTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            waterStatus = sensor("Water Running Status", 
                                          get_value_from_map(schema_xml_map, "waterRunningStatusFromHeatPump", version, converter=lambda v: v == "1"),
                                          "", BinarySensorDeviceClass.RUNNING, "mdi:water-outline", Platform.BINARY_SENSOR),
            waterActualTemperature = sensor("Water Actual Temperature", 
                                        get_value_from_map(schema_xml_map, "waterSwitchingSensorTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:water-thermometer-outline", Platform.SENSOR),
            waterRequiredTemperature = sensor("Water Required Temperature", 
                                        get_value_from_map(schema_xml_map, "waterRequiredTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:water-thermometer-outline", Platform.SENSOR),
            solarStatus = sensor("Solar Running Status", 
                                        get_value_from_map(schema_xml_map, "solarRunningStatus", version, converter=lambda v: v == "1"), 
                                      "", BinarySensorDeviceClass.RUNNING, "mdi:solar-panel", Platform.BINARY_SENSOR),
            solarPanelTemperature = sensor("Solar Panel Temperature", 
                                        get_value_from_map(schema_xml_map, "solarPanelTemperature", version), 
                                      "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR),
            circulationStatus = sensor("Circulation Running Status", 
                                        get_value_from_map(schema_xml_map, "circulationRunningStatus", version, converter=lambda v: v == "1"), 
                                      "", BinarySensorDeviceClass.RUNNING, "mdi:sync", Platform.BINARY_SENSOR),
        )
