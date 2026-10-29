from pydantic import BaseModel

from ..schema import DeviceSchema

class AkuResponseSchema(BaseModel):
    state: DeviceSchema
    comfortTemperature: DeviceSchema
    setbackTemperature: DeviceSchema
