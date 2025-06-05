from typing import Dict, List
from homeassistant.const import Platform

from custom_components.regulus.schema import sensor
from .dashboard_schemas import DashboardResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map

class DashboardApi(AbstractApi[DashboardResponseSchema]):
    page = "/1_sch.xml"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: List[str]) -> DashboardResponseSchema:
        print("Successfully fetched `/dashboard` data")

        return DashboardResponseSchema(
            outdoorTemperature = sensor("Outdoor temperature", 
                                        get_value_from_map(schema_xml_map, "outdoorTemperature", registry_errors), 
                                      "°C", "temperature", "mdi:thermometer", Platform.SENSOR),
            # rcTariff="LOW" if get_value_from_map(schema_xml_map, "rcTariff", registry_errors) == "1" else "HIGH",
            # holiday="ON" if get_value_from_map(schema_xml_map, "holiday", registry_errors) == "1" else "OFF",
            heatPumpRunningStatus= sensor("Heat Pump Running Status", 
                                          get_value_from_map(schema_xml_map, "heatPumpRunningStatus", registry_errors) != "0",
                                          "", "running", "mdi:fan", Platform.BINARY_SENSOR),
            # heatPumpOutletTemperature=get_value_from_map(schema_xml_map, "heatPumpOutletTemperature", registry_errors),
            # heatPumpInletTemperature=get_value_from_map(schema_xml_map, "heatPumpInletTemperature", registry_errors),
            # zone1Status=get_value_from_map(schema_xml_map, "zone1RunningStatus", registry_errors) != "0",
            # zone1ActualTemperature=get_value_from_map(schema_xml_map, "zone1Temperature", registry_errors),
            # zone1RequiredTemperature=get_value_from_map(schema_xml_map, "zone1RequiredTemperature", registry_errors),
            # zone1ActualHeatingWaterTemperature=get_value_from_map(schema_xml_map, "zone1HeatingWaterTemperature", registry_errors),
            # zone1RequiredHeatingWaterTemperature=get_value_from_map(schema_xml_map, "zone1RequiredHeatingWaterTemperature", registry_errors),
            # zone2Status=get_value_from_map(schema_xml_map, "zone2RunningStatus", registry_errors) != "0",
            # zone2ActualTemperature=get_value_from_map(schema_xml_map, "zone2Temperature", registry_errors),
            # zone2RequiredTemperature=get_value_from_map(schema_xml_map, "zone2RequiredTemperature", registry_errors),
            # zone2ActualHeatingWaterTemperature=get_value_from_map(schema_xml_map, "zone2HeatingWaterTemperature", registry_errors),
            # zone2RequiredHeatingWaterTemperature=get_value_from_map(schema_xml_map, "zone2RequiredHeatingWaterTemperature", registry_errors),
            # akuStatus=get_value_from_map(schema_xml_map, "akuRunningStatusFromHeatPump", registry_errors) == "1",
            # akuTopTemperature=get_value_from_map(schema_xml_map, "akuTopTemperature", registry_errors),
            # akuBottomTemperature=get_value_from_map(schema_xml_map, "akuBottomTemperature", registry_errors),
            # akuRequiredTemperature=get_value_from_map(schema_xml_map, "akuRequiredTemperature", registry_errors),
            # waterStatus=get_value_from_map(schema_xml_map, "waterRunningStatusFromHeatPump", registry_errors) == "1",
            # waterActualTemperature=get_value_from_map(schema_xml_map, "waterSwitchingSensorTemperature", registry_errors),
            # waterRequiredTemperature=get_value_from_map(schema_xml_map, "waterRequiredTemperature", registry_errors),
            # solarStatus=get_value_from_map(schema_xml_map, "solarRunningStatus", registry_errors) == "1",
            # solarPanelTemperature=get_value_from_map(schema_xml_map, "solarPanelTemperature", registry_errors),
            # circulationStatus=get_value_from_map(schema_xml_map, "circulationRunningStatus", registry_errors) == "1"
        )
