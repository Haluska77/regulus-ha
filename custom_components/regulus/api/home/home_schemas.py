from pydantic import BaseModel
from ...schema import SensorSchema

class HomeResponseSchema(BaseModel):
    zone1SummerMode: SensorSchema
    zone2SummerMode: SensorSchema
