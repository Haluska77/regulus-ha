from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone2_schemas import Zone2ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone2Api(AbstractApi[Zone2ResponseSchema]):
    page = "/zo_z2.xml"
    key = "zone2"
    name = "Zone 2"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone2ResponseSchema:

        return Zone2ResponseSchema(
            zone2State = deviceSensor("Zone 2 State", "zone2State", "", BinarySensorDeviceClass.RUNNING, "mdi:heating-coil",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone2Temperature = deviceSensor("Zone 2 Temperature", "zone2Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone2DesiredTemperature = deviceSensor("Zone 2 Desired Temperature", "zone2DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer", 
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
