from typing import Dict
from ..util import is_version_lower_than, is_version_higher_or_equal_than
from homeassistant.const import Platform
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.sensor import SensorDeviceClass


from ..schema import deviceSensor
from .water_schemas import WaterResponseSchema
from ...service.abstract_api import AbstractApi

class WaterApi(AbstractApi[WaterResponseSchema]):
    page = "/tv_tc.xml"
    key = "water"
    name = "Water"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> WaterResponseSchema:

        return WaterResponseSchema(
            state = deviceSensor("State", "waterState", "", BinarySensorDeviceClass.RUNNING, "mdi:power", 
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            serviceEnabled = deviceSensor("Service Enabled", "waterServiceEnabled", "", "none", "mdi:check-circle", 
                                            Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            # for versions < IR14 1.0.11
            comfortTemperature = deviceSensor("Comfort Temperature", "waterComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_lower_than(version, "14_1_0_11_0")),
            # for versions < IR14 1.0.11
            setbackTemperature = deviceSensor("Setback Temperature", "waterSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_lower_than(version, "14_1_0_11_0")),
            # for versions >= IR14 1.0.11
            oneTimeHeatingState = deviceSensor("One-Time Heating State", "waterOneTimeHeatingState", "", BinarySensorDeviceClass.RUNNING, "mdi:power", 
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0", filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),
            # for versions >= IR14 1.0.11
            oneTimeHeatingTemperature = deviceSensor("One-Time Heating Temperature", "waterOneTimeHeatingTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),
            temperature = deviceSensor("Temperature", "waterSwitchingSensorTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.SENSOR, schema_xml_map, registry_mapper),
            desiredSetbackTemperature = deviceSensor("Desired Setback Temperature", "waterRequiredTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.SENSOR, schema_xml_map, registry_mapper),
            # for versions >= IR14 1.0.11
            setTemperature = deviceSensor("Set Temperature", "waterComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),
            # for versions >= IR14 1.0.11
            decreasedSetbackTemperature = deviceSensor("Decreased Setback Temperature", "waterSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),
        )
