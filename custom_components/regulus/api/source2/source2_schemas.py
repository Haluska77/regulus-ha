from pydantic import BaseModel

from ..schema import DeviceSchema

class Source2ResponseSchema(BaseModel):
    state: DeviceSchema
    serviceEnabled: DeviceSchema
    heatingDemandTemperature: DeviceSchema
