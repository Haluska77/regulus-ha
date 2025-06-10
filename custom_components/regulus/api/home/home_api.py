from typing import Dict, List
from homeassistant.const import Platform

from custom_components.regulus.schema import sensor
from .home_schemas import HomeResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map

class HomeApi(AbstractApi[HomeResponseSchema]):
    page = "/home.xml"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: List[str]) -> HomeResponseSchema:
        print("Successfully fetched `/home` data")
        version = self.config["ir_version"]

        return HomeResponseSchema(
            zone1SummerMode = sensor("Zone 1 Summer Mode", 
                                          get_value_from_map(schema_xml_map, "zone1SummerMode", registry_errors, version) != "0",
                                          "", "none", "mdi:sun-snowflake-variant", Platform.BINARY_SENSOR),
            zone2SummerMode = sensor("Zone 2 Summer Mode", 
                                          get_value_from_map(schema_xml_map, "zone2SummerMode", registry_errors, version) != "0",
                                          "", "none", "mdi:sun-snowflake-variant", Platform.BINARY_SENSOR),
        )
