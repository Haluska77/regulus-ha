from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone1_schemas import Zone1ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone1Api(AbstractApi[Zone1ResponseSchema]):
    page = "/zo_z1.xml"
    key = "zone1"
    name = "Zone 1"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone1ResponseSchema:

        return Zone1ResponseSchema(
            zone1State = deviceSensor("Zone 1 State", "zone1State", "", BinarySensorDeviceClass.RUNNING, "mdi:heating-coil", 
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone1Temperature = deviceSensor("Zone 1 Temperature", "zone1Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone1DesiredTemperature = deviceSensor("Zone 1 Desired Temperature", "zone1DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
