from pydantic import BaseModel
from typing import Optional
from .service.xml_parser_service import RegistryResult
from homeassistant.const import Platform

class SensorSchema(BaseModel):
        name: Optional[str]
        value: RegistryResult
        unit: Optional[str]
        deviceClass: Optional[str]
        icon: Optional[str]
        platform: Platform

def sensor(name: str, value: RegistryResult, unit: str, device_class: str, icon: str, platform: Platform) -> SensorSchema:
        return SensorSchema(
            name=name,
            value=value,
            unit=unit,
            deviceClass=device_class,
            icon=icon,
            platform=platform
        )
