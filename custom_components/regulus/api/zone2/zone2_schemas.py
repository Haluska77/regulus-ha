from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone2ResponseSchema(BaseModel):
    zone2State: DeviceSchema
    zone2Temperature: DeviceSchema
    zone2DesiredTemperature: DeviceSchema