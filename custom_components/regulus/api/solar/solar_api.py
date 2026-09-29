from typing import Dict

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import Platform

from ...schema import deviceSensor
from ...service.abstract_api import AbstractApi
from .solar_schemas import SolarResponseSchema


class SolarApi(AbstractApi[SolarResponseSchema]):
    page = "/ZD_SOL.XML"
    key = "solar"
    name = "Solar"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> SolarResponseSchema:
        consumer1_service_registry = registry_mapper.get("solarConsumer1ServiceEnabled")
        consumer2_service_registry = registry_mapper.get("solarConsumer2ServiceEnabled")
        consumer3_service_registry = registry_mapper.get("solarConsumer3ServiceEnabled")
        consumer1_enabled = consumer1_service_registry is None or schema_xml_map.get(consumer1_service_registry) == "1"
        consumer2_enabled = consumer2_service_registry is None or schema_xml_map.get(consumer2_service_registry) == "1"
        consumer3_enabled = consumer3_service_registry is None or schema_xml_map.get(consumer3_service_registry) == "1"

        return SolarResponseSchema(
            solarPumpPower=deviceSensor("Solar Pump Power", "solarPumpPower", "%", SensorDeviceClass.POWER_FACTOR, "mdi:solar-power", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarStatus=deviceSensor("Solar Pump Status", "solarRunningStatus", "", BinarySensorDeviceClass.RUNNING, "mdi:solar-panel", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value == "1"),
            solarPanelTemperature=deviceSensor("Solar Panel Temperature", "solarPanelTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer1Heating=deviceSensor("Solar Consumer 1 Heating", "solarConsumer1Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: consumer1_enabled and value != "0"),
            solarConsumer1Enabled=deviceSensor("Solar Consumer 1 Enabled", "solarConsumer1ServiceEnabled", "", "none", "mdi:check-circle", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value == "1"),
            solarConsumer1Temperature=deviceSensor("Solar Consumer 1 Temperature", "solarConsumer1Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer1Demand=deviceSensor("Solar Consumer 1 Demand", "solarConsumer1Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            solarConsumer1MaximumTemperature=deviceSensor("Solar Consumer 1 Maximum Temperature", "solarConsumer1MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer2Heating=deviceSensor("Solar Consumer 2 Heating", "solarConsumer2Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: consumer2_enabled and value != "0"),
            solarConsumer2Enabled=deviceSensor("Solar Consumer 2 Enabled", "solarConsumer2ServiceEnabled", "", "none", "mdi:check-circle", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value == "1"),
            solarConsumer2Temperature=deviceSensor("Solar Consumer 2 Temperature", "solarConsumer2Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer2Demand=deviceSensor("Solar Consumer 2 Demand", "solarConsumer2Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            solarConsumer2MaximumTemperature=deviceSensor("Solar Consumer 2 Maximum Temperature", "solarConsumer2MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer3Heating=deviceSensor("Solar Consumer 3 Heating", "solarConsumer3Heating", "", BinarySensorDeviceClass.HEAT, "mdi:heat-wave", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: consumer3_enabled and value != "0"),
            solarConsumer3Enabled=deviceSensor("Solar Consumer 3 Enabled", "solarConsumer3ServiceEnabled", "", "none", "mdi:check-circle", Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda value: value == "1"),
            solarConsumer3Temperature=deviceSensor("Solar Consumer 3 Temperature", "solarConsumer3Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", Platform.SENSOR, schema_xml_map, registry_mapper),
            solarConsumer3Demand=deviceSensor("Solar Consumer 3 Demand", "solarConsumer3Demand", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer-plus", Platform.NUMBER, schema_xml_map, registry_mapper),
            solarConsumer3MaximumTemperature=deviceSensor("Solar Consumer 3 Maximum Temperature", "solarConsumer3MaximumTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer-alert", Platform.SENSOR, schema_xml_map, registry_mapper),
        )