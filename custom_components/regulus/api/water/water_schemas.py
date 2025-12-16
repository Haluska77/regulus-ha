from pydantic import BaseModel

from ...schema import DeviceSchema

class WaterResponseSchema(BaseModel):
    waterState: DeviceSchema
    waterComfortTemperature: DeviceSchema
    waterSetbackTemperature: DeviceSchema
