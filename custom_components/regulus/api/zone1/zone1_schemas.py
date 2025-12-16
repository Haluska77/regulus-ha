from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone1ResponseSchema(BaseModel):
    zone1State: DeviceSchema
    zone1Temperature: DeviceSchema
    zone1DesiredTemperature: DeviceSchema