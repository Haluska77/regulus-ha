from pydantic import BaseModel

from ...schema import DeviceSchema

class FveResponseSchema(BaseModel):
    gridPowerL1: DeviceSchema
    gridPowerL2: DeviceSchema
    gridPowerL3: DeviceSchema
    gridPowerTotal: DeviceSchema
    gridImportPower: DeviceSchema
    gridExportPower: DeviceSchema
    gridPowerNet: DeviceSchema
    heaterPowerL1: DeviceSchema
    heaterPowerL2: DeviceSchema
    heaterPowerL3: DeviceSchema
    heatPumpCompressorSpeed: DeviceSchema
