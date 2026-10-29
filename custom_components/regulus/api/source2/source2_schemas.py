from pydantic import BaseModel

from ..schema import DeviceSchema

class Source2ResponseSchema(BaseModel):
    state: DeviceSchema
    heatingDemandTemperature: DeviceSchema
