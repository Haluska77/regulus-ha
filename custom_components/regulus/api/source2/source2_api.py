from typing import Dict

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import Platform

from ..schema import deviceSensor
from ...service.abstract_api import AbstractApi
from .source2_schemas import Source2ResponseSchema

class Source2Api(AbstractApi[Source2ResponseSchema]):
    page = "/zd_s2.xml"
    key = "source2"
    name = "On/Off Source 2"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Source2ResponseSchema:
        return Source2ResponseSchema(
            state = deviceSensor("State", "source2State", "", BinarySensorDeviceClass.RUNNING, "mdi:power", 
                                 Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            serviceEnabled = deviceSensor("Service Enabled", "source2ServiceEnabled", "", "none", "mdi:check-circle", 
                                            Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda value: value != "0"),
            heatingDemandTemperature = deviceSensor("Heating Demand Temperature", "source2HeatingDemandTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                                    Platform.SENSOR, schema_xml_map, registry_mapper),
        )
