from pydantic import BaseModel
from typing import Optional

class SensorSchema(BaseModel):
        name: Optional[str]
        value: Optional[str]
        unit: Optional[str]
        deviceClass: Optional[str]
        icon: Optional[str]

def sensor(name: str, value: str, unit: str, device_class: str, icon: str) -> SensorSchema:
        return SensorSchema(
            name=name,
            value=value,
            unit=unit,
            deviceClass=device_class,
            icon=icon
        )
