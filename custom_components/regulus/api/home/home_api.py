from typing import Dict
from homeassistant.const import Platform

from ...schema import deviceSensor
from .home_schemas import HomeResponseSchema
from ...service.abstract_api import AbstractApi

class HomeApi(AbstractApi[HomeResponseSchema]):
    page = "/home.xml"
    key = "home"
    name = "Home"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> HomeResponseSchema:

        return HomeResponseSchema(
            zone1SummerMode = deviceSensor("Zone 1 Summer Mode", "zone1SummerMode", None, None, "mdi:sun-snowflake-variant", 
                                           Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone2SummerMode = deviceSensor("Zone 2 Summer Mode", "zone2SummerMode", None, None, "mdi:sun-snowflake-variant", 
                                           Platform.BINARY_SENSOR, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
        )
