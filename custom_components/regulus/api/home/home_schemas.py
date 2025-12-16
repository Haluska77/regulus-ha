from pydantic import BaseModel
from ...schema import DeviceSchema

class HomeResponseSchema(BaseModel):
    zone1SummerMode: DeviceSchema
    zone2SummerMode: DeviceSchema
