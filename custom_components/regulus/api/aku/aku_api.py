from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .aku_schemas import AkuResponseSchema
from ...service.abstract_api import AbstractApi

class AkuApi(AbstractApi[AkuResponseSchema]):
    page = "/zo_aku.xml"
    key = "aku"
    name = "Aku"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> AkuResponseSchema:

        return AkuResponseSchema(
            akuState = deviceSensor("Aku State", "akuState", "", BinarySensorDeviceClass.RUNNING, "mdi:sun-snowflake-variant",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            akuComfortTemperature = deviceSensor("Comfort Temperature", "akuComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
            akuSetbackTemperature = deviceSensor("Setback Temperature", "akuSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
