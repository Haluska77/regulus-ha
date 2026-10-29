from pydantic import BaseModel

from ..schema import DeviceSchema

class AkuResponseSchema(BaseModel):
    state: DeviceSchema
    serviceEnabled: DeviceSchema
    comfortTemperature: DeviceSchema
    setbackTemperature: DeviceSchema
    setTemperature: DeviceSchema
    decreasedSetbackTemperature: DeviceSchema
