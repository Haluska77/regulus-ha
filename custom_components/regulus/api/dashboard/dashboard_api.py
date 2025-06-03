from typing import Dict, List
from .dashboard_schemas import DashboardResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map

class DashboardApi(AbstractApi[DashboardResponseSchema]):
    page = "/1_sch.xml"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: List[str]) -> DashboardResponseSchema:
        print("Successfully fetched `/dashboard` data")

        return DashboardResponseSchema(
            outdoorTemperature=get_value_from_map(schema_xml_map, "outdoorTemperature", registry_errors),
            rcTariff="LOW" if get_value_from_map(schema_xml_map, "rcTariff", registry_errors) == "1" else "HIGH",
            holiday="ON" if get_value_from_map(schema_xml_map, "holiday", registry_errors) == "1" else "OFF",
            heatPump={
                "runningStatus": get_value_from_map(schema_xml_map, "heatPumpRunningStatus", registry_errors) != "0",
                "outletTemperature": get_value_from_map(schema_xml_map, "heatPumpOutletTemperature", registry_errors),
                "inletTemperature": get_value_from_map(schema_xml_map, "heatPumpInletTemperature", registry_errors),
            },
            zone1={
                "status": get_value_from_map(schema_xml_map, "zone1RunningStatus", registry_errors) != "0",
                "actualTemperature": get_value_from_map(schema_xml_map, "zone1Temperature", registry_errors),
                "requiredTemperature": get_value_from_map(schema_xml_map, "zone1RequiredTemperature", registry_errors),
                "actualHeatingWaterTemperature": get_value_from_map(schema_xml_map, "zone1HeatingWaterTemperature", registry_errors),
                "requiredHeatingWaterTemperature": get_value_from_map(schema_xml_map, "zone1RequiredHeatingWaterTemperature", registry_errors),
            },
            zone2={
                "status": get_value_from_map(schema_xml_map, "zone2RunningStatus", registry_errors) != "0",
                "actualTemperature": get_value_from_map(schema_xml_map, "zone2Temperature", registry_errors),
                "requiredTemperature": get_value_from_map(schema_xml_map, "zone2RequiredTemperature", registry_errors),
                "actualHeatingWaterTemperature": get_value_from_map(schema_xml_map, "zone2HeatingWaterTemperature", registry_errors),
                "requiredHeatingWaterTemperature": get_value_from_map(schema_xml_map, "zone2RequiredHeatingWaterTemperature", registry_errors),
            },
            aku={
                "status": get_value_from_map(schema_xml_map, "akuRunningStatusFromHeatPump", registry_errors) == "1",
                "topTemperature": get_value_from_map(schema_xml_map, "akuTopTemperature", registry_errors),
                "bottomTemperature": get_value_from_map(schema_xml_map, "akuBottomTemperature", registry_errors),
                "requiredTemperature": get_value_from_map(schema_xml_map, "akuRequiredTemperature", registry_errors),
            },
            water={
                "status": get_value_from_map(schema_xml_map, "waterRunningStatusFromHeatPump", registry_errors) == "1",
                "actualTemperature": get_value_from_map(schema_xml_map, "waterSwitchingSensorTemperature", registry_errors),
                "requiredTemperature": get_value_from_map(schema_xml_map, "waterRequiredTemperature", registry_errors),
            },
            solar={
                "status": get_value_from_map(schema_xml_map, "solarRunningStatus", registry_errors) == "1",
                "panelTemperature": get_value_from_map(schema_xml_map, "solarPanelTemperature", registry_errors),
            },
            circulation={
                "status": get_value_from_map(schema_xml_map, "circulationRunningStatus", registry_errors) == "1"
            }
        )
