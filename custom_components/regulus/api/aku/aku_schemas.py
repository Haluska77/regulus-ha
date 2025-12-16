from pydantic import BaseModel

from ...schema import DeviceSchema

class AkuResponseSchema(BaseModel):
    akuState: DeviceSchema
    akuComfortTemperature: DeviceSchema
    akuSetbackTemperature: DeviceSchema
