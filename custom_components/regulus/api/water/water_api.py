from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .water_schemas import WaterResponseSchema
from ...service.abstract_api import AbstractApi

class WaterApi(AbstractApi[WaterResponseSchema]):
    page = "/tv_tc.xml"
    key = "water"
    name = "Water"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> WaterResponseSchema:

        return WaterResponseSchema(
            waterState = deviceSensor("Water State", "waterState", "", BinarySensorDeviceClass.RUNNING, "mdi:sun-snowflake-variant", 
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            waterComfortTemperature = deviceSensor("Comfort Temperature", "waterComfortTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
            waterSetbackTemperature = deviceSensor("Setback Temperature", "waterSetbackTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
