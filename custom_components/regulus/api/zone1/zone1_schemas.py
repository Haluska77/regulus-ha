from pydantic import BaseModel

from ..schema import DeviceSchema

class Zone1ResponseSchema(BaseModel):
    state: DeviceSchema
    temperature: DeviceSchema
    desiredTemperature: DeviceSchema
    humidity: DeviceSchema
