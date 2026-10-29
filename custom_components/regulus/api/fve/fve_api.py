from typing import Dict, Optional, Tuple
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass

from ..schema import DeviceSchema, deviceSensor
from .fve_schemas import FveResponseSchema
from ...service.abstract_api import AbstractApi
from ...service.xml_parser_service import get_value_from_map
from ...const import REGISTRY_MAPPERS

PHASES = ("L1", "L2", "L3")


def grid_flow(schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Tuple[Optional[int], Optional[int], Optional[str]]:
    """Split the wattmeter readings into grid import and export power (W).

    The wattmeter reports unsigned power per phase; the direction comes from a separate
    bit per phase (1 = consumption from the grid, 0 = export) - the one the IR web UI uses
    to draw the flow arrows red or green. Phases are summed separately, so import on one
    phase and export on another do not cancel out (phase-wise metering, as Czech LV meters do).
    """
    imported = exported = 0
    for phase in PHASES:
        power = get_value_from_map(schema_xml_map, f"fveGridPower{phase}", registry_mapper)
        direction = get_value_from_map(schema_xml_map, f"fveGridImport{phase}", registry_mapper)
        error = power.error or direction.error
        if error:
            return None, None, error
        try:
            watts = abs(int(float(power.value)))
        except (TypeError, ValueError, OverflowError):
            return None, None, f"Invalid grid power {power.value!r} on {phase}"
        if direction.value not in ("0", "1"):
            return None, None, f"Invalid grid direction {direction.value!r} on {phase}"
        if direction.value == "0":
            exported += watts
        else:
            imported += watts
    return imported, exported, None


def computedPowerSensor(name: str, value: Optional[int], icon: str, error: Optional[str]) -> DeviceSchema:
    return DeviceSchema(
        name=name,
        value=None if value is None else str(value),
        registryKey=None,
        unit="W",
        deviceClass=SensorDeviceClass.POWER,
        icon=icon,
        platform=Platform.SENSOR,
        error=error,
    )


class FveApi(AbstractApi[FveResponseSchema]):
    """Photovoltaic (FVE) schema page: grid wattmeter, electric heater and heat pump readings."""

    page = "/zd_f_sch.xml"
    key = "fve"
    name = "FVE"
    supported_ir_versions = ["14_1_0_10_107"]

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> FveResponseSchema:
        imported, exported, flow_error = grid_flow(schema_xml_map, registry_mapper)
        net = None if flow_error else imported - exported

        return FveResponseSchema(
            gridPowerL1 = deviceSensor("Grid Power L1", "fveGridPowerL1", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerL2 = deviceSensor("Grid Power L2", "fveGridPowerL2", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerL3 = deviceSensor("Grid Power L3", "fveGridPowerL3", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                       Platform.SENSOR, schema_xml_map, registry_mapper),
            gridPowerTotal = deviceSensor("Grid Power Total", "fveGridPowerTotal", "W", SensorDeviceClass.POWER, "mdi:transmission-tower",
                                          Platform.SENSOR, schema_xml_map, registry_mapper),
            gridImportPower = computedPowerSensor("Grid Import Power", imported, "mdi:transmission-tower-import", flow_error),
            gridExportPower = computedPowerSensor("Grid Export Power", exported, "mdi:transmission-tower-export", flow_error),
            gridPowerNet = computedPowerSensor("Grid Power Net", net, "mdi:transmission-tower", flow_error),
            heaterPowerL1 = deviceSensor("Heater Power L1", "fveHeaterPowerL1", "W", SensorDeviceClass.POWER, "mdi:heating-coil",
                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            heaterPowerL2 = deviceSensor("Heater Power L2", "fveHeaterPowerL2", "W", SensorDeviceClass.POWER, "mdi:heating-coil",
                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            heaterPowerL3 = deviceSensor("Heater Power L3", "fveHeaterPowerL3", "W", SensorDeviceClass.POWER, "mdi:heating-coil",
                                         Platform.SENSOR, schema_xml_map, registry_mapper),
            heatPumpCompressorSpeed = deviceSensor("Heat Pump Compressor Speed", "fveHeatPumpCompressorSpeed", "rps", None, "mdi:speedometer",
                                                   Platform.SENSOR, schema_xml_map, registry_mapper),
        )
