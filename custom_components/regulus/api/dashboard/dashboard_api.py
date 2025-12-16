from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass

from ...schema import deviceSensor
from .dashboard_schemas import DashboardResponseSchema
from ...service.abstract_api import AbstractApi

class DashboardApi(AbstractApi[DashboardResponseSchema]):
    page = "/1_sch.xml"
    key = "dashboard"
    name = "Dashboard"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> DashboardResponseSchema:

        return DashboardResponseSchema(
            outdoorTemperature = deviceSensor("Outdoor Temperature", "outdoorTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                              "mdi:sun-thermometer-outline", Platform.SENSOR, schema_xml_map, registry_mapper),
            rcTariff = deviceSensor("RC Tariff", "rcTariff", "", "none", "mdi:cash-clock", 
                                    Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
            holiday = deviceSensor("Holiday", "holiday", "", "none", "mdi:beach", 
                                   Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
            heatPumpRunningStatus= deviceSensor("Heat Pump Running Status", "heatPumpRunningStatus", "", BinarySensorDeviceClass.RUNNING, 
                                                "mdi:fan", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            heatPumpOutletTemperature = deviceSensor("Heat Pump Outlet Temperature", "heatPumpOutletTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                                     "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpInletTemperature = deviceSensor("Heat Pump Inlet Temperature", "heatPumpInletTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                                   "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone1Status = deviceSensor("Zone 1 Running Status", "zone1RunningStatus", "", BinarySensorDeviceClass.RUNNING, 
                                      "mdi:heating-coil", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone1ActualTemperature = deviceSensor("Zone 1 Actual Temperature", "zone1Temperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                                 "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone1RequiredTemperature = deviceSensor("Zone 1 Required Temperature", "zone1RequiredTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                      "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone1ActualHeatingWaterTemperature = deviceSensor("Zone 1 Heating Water Temperature", "zone1HeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                      "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone1RequiredHeatingWaterTemperature = deviceSensor("Zone 1 Required Heating Water Temperature", "zone1RequiredHeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                      "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone2Status = deviceSensor("Zone 2 Running Status", "zone2RunningStatus", "", BinarySensorDeviceClass.RUNNING, 
                                      "mdi:radiator", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone2ActualTemperature = deviceSensor("Zone 2 Actual Temperature", "zone2Temperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                                 "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone2RequiredTemperature = deviceSensor("Zone 2 Required Temperature", "zone2RequiredTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                      "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone2ActualHeatingWaterTemperature = deviceSensor("Zone 2 Heating Water Temperature", "zone2HeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, 
                                      "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            zone2RequiredHeatingWaterTemperature = deviceSensor("Zone 2 Required Heating Water Temperature", "zone2RequiredHeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                                                Platform.SENSOR, schema_xml_map, registry_mapper),
            akuStatus = deviceSensor("Aku Running Status", "akuRunningStatusFromHeatPump", "", BinarySensorDeviceClass.RUNNING, "mdi:water-boiler", 
                                     Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
            akuTopTemperature = deviceSensor("Aku Top Temperature", "akuTopTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                             Platform.SENSOR, schema_xml_map, registry_mapper),
            akuBottomTemperature = deviceSensor("Aku Bottom Temperature", "akuBottomTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                                Platform.SENSOR, schema_xml_map, registry_mapper),
            akuRequiredTemperature = deviceSensor("Aku Required Temperature", "akuRequiredTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                                  Platform.SENSOR, schema_xml_map, registry_mapper),
            waterStatus = deviceSensor("Water Running Status", "waterRunningStatusFromHeatPump", "", BinarySensorDeviceClass.RUNNING, "mdi:water-outline", 
                                       Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
            waterActualTemperature = deviceSensor("Water Actual Temperature", "waterSwitchingSensorTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:water-thermometer-outline", 
                                                  Platform.SENSOR, schema_xml_map, registry_mapper),
            waterRequiredTemperature = deviceSensor("Water Required Temperature", "waterRequiredTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:water-thermometer-outline", 
                                                    Platform.SENSOR, schema_xml_map, registry_mapper),
            solarStatus = deviceSensor("Solar Running Status", "solarRunningStatus", "", BinarySensorDeviceClass.RUNNING, "mdi:solar-panel", 
                                       Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
            solarPanelTemperature = deviceSensor("Solar Panel Temperature", "solarPanelTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                                 Platform.SENSOR, schema_xml_map, registry_mapper),
            circulationStatus = deviceSensor("Circulation Running Status", "circulationRunningStatus", "", BinarySensorDeviceClass.RUNNING, "mdi:sync", 
                                            Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v == "1"),
        )
