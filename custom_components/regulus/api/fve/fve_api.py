from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass

from ...schema import deviceSensor
from .fve_schemas import FveResponseSchema
from ...service.abstract_api import AbstractApi


class FveApi(AbstractApi[FveResponseSchema]):
    """Photovoltaic (FVE) schema page: grid wattmeter and heat pump power readings."""

    page = "/zd_f_sch.xml"
    key = "fve"
    name = "FVE"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> FveResponseSchema:

        return FveResponseSchema(
            gridPowerL1 = deviceSensor("Grid Power L1", "fveGridPowerL1", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerL2 = deviceSensor("Grid Power L2", "fveGridPowerL2", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerL3 = deviceSensor("Grid Power L3", "fveGridPowerL3", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerTotal = deviceSensor("Grid Power Total", "fveGridPowerTotal", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                          Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpPowerL1 = deviceSensor("Heat Pump Power L1", "fveHeatPumpPowerL1", "W", SensorDeviceClass.POWER, "mdi:heat-pump",
                                           Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpPowerL2 = deviceSensor("Heat Pump Power L2", "fveHeatPumpPowerL2", "W", SensorDeviceClass.POWER, "mdi:heat-pump",
                                           Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpPowerL3 = deviceSensor("Heat Pump Power L3", "fveHeatPumpPowerL3", "W", SensorDeviceClass.POWER, "mdi:heat-pump",
                                           Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpCompressorSpeed = deviceSensor("Heat Pump Compressor Speed", "fveHeatPumpCompressorSpeed", "rps", None, "mdi:speedometer",
                                                   Platform.SENSOR, schema_xml_map, registry_mapper),
        )
