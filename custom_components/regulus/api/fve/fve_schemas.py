from pydantic import BaseModel

from ...schema import DeviceSchema

class FveResponseSchema(BaseModel):
    gridPowerL1: DeviceSchema
    gridPowerL2: DeviceSchema
    gridPowerL3: DeviceSchema
    gridPowerTotal: DeviceSchema
    heatPumpPowerL1: DeviceSchema
    heatPumpPowerL2: DeviceSchema
    heatPumpPowerL3: DeviceSchema
    heatPumpCompressorSpeed: DeviceSchema
