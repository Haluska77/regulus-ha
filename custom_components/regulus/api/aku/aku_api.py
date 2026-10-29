from typing import Dict
from ..util import is_version_lower_than, is_version_higher_or_equal_than
from homeassistant.const import Platform
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ..schema import deviceSensor
from .aku_schemas import AkuResponseSchema
from ...service.abstract_api import AbstractApi

class AkuApi(AbstractApi[AkuResponseSchema]):
    page = "/zo_aku.xml"
    key = "aku"
    name = "Aku"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> AkuResponseSchema:

        return AkuResponseSchema(
            state = deviceSensor("State", "akuState", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            serviceEnabled = deviceSensor("Service Enabled", "akuServiceEnabled", "", "none", "mdi:check-circle", 
                                            Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            # for versions < IR14 1.0.11
            comfortTemperature = deviceSensor("Comfort Temperature", "akuComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_lower_than(version, "14_1_0_11_0")),
            # for versions < IR14 1.0.11
            setbackTemperature = deviceSensor("Setback Temperature", "akuSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_lower_than(version, "14_1_0_11_0")),
            # for versions >= IR14 1.0.11
            setTemperature = deviceSensor("Set Temperature", "akuComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),
            # for versions >= IR14 1.0.11
            decreasedSetbackTemperature = deviceSensor("Decreased Setback Temperature", "akuSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                     Platform.NUMBER, schema_xml_map, registry_mapper, step=1, filter=lambda version: is_version_higher_or_equal_than(version, "14_1_0_11_0")),

        )
