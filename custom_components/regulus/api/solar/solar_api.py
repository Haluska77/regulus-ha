from typing import Dict

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import Platform

from ..schema import deviceSensor
from ...service.abstract_api import AbstractApi
from .solar_schemas import SolarResponseSchema


class SolarApi(AbstractApi[SolarResponseSchema]):
    page = "/ZD_SOL.XML"
    key = "solar"
    name = "Solar"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> SolarResponseSchema:

        return SolarResponseSchema(

            pumpPower=deviceSensor("Pump Power", "solarPumpPower", "%", SensorDeviceClass.POWER_FACTOR, "mdi:solar-power", Platform.SENSOR, schema_xml_map, registry_mapper),
            status=deviceSensor("Pump Status", "solarRunningStatus", "", BinarySensorDeviceClass.RUNNING, "mdi:solar-panel", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value == "1"),
            panelTemperature=deviceSensor("Panel Temperature", "solarPanelTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            
            consumer1state = deviceSensor("Consumer 1 State", "solarConsumer1State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            consumer1Enabled=deviceSensor("Consumer 1 Enabled", "solarConsumer1ServiceEnabled", "", "none", "mdi:check-circle", Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer1Heating=deviceSensor("Consumer 1 Heating", "solarConsumer1Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer1Temperature=deviceSensor("Consumer 1 Temperature", "solarConsumer1Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            consumer1Demand=deviceSensor("Consumer 1 Demand", "solarConsumer1Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            consumer1MaximumTemperature=deviceSensor("Consumer 1 Maximum Temperature", "solarConsumer1MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
            
            consumer2state = deviceSensor("Consumer 2 State", "solarConsumer2State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            consumer2Enabled=deviceSensor("Consumer 2 Enabled", "solarConsumer2ServiceEnabled", "", "none", "mdi:check-circle", Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer2Heating=deviceSensor("Consumer 2 Heating", "solarConsumer2Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer2Temperature=deviceSensor("Consumer 2 Temperature", "solarConsumer2Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            consumer2Demand=deviceSensor("Consumer 2 Demand", "solarConsumer2Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            consumer2MaximumTemperature=deviceSensor("Consumer 2 Maximum Temperature", "solarConsumer2MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
            
            consumer3state = deviceSensor("Consumer 3 State", "solarConsumer3State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            consumer3Enabled=deviceSensor("Consumer 3 Enabled", "solarConsumer3ServiceEnabled", "", "none", "mdi:check-circle", Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer3Heating=deviceSensor("Consumer 3 Heating", "solarConsumer3Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            consumer3Temperature=deviceSensor("Consumer 3 Temperature", "solarConsumer3Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            consumer3Demand=deviceSensor("Consumer 3 Demand", "solarConsumer3Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            consumer3MaximumTemperature=deviceSensor("Consumer 3 Maximum Temperature", "solarConsumer3MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
        )