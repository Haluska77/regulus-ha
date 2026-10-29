from pydantic import BaseModel

from ..schema import DeviceSchema

class WaterResponseSchema(BaseModel):
    state: DeviceSchema
    serviceEnabled: DeviceSchema
    comfortTemperature: DeviceSchema
    setbackTemperature: DeviceSchema
    oneTimeHeatingState: DeviceSchema
    oneTimeHeatingTemperature: DeviceSchema
    temperature: DeviceSchema
    desiredSetbackTemperature: DeviceSchema
    setTemperature: DeviceSchema
    decreasedSetbackTemperature: DeviceSchema
