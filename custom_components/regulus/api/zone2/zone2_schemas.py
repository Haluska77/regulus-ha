from pydantic import BaseModel

from ..schema import DeviceSchema

class Zone2ResponseSchema(BaseModel):
    state: DeviceSchema
    temperature: DeviceSchema
    desiredTemperature: DeviceSchema