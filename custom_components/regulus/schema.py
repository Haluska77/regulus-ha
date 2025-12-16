from pydantic import BaseModel
from typing import Callable, Optional, Dict, Union
from homeassistant.const import Platform
from .service.xml_parser_service import get_value_from_map

class DeviceSchema(BaseModel):
        name: Optional[str]
        value: Optional[Union[str, bool]]  
        registryKey: Optional[str]
        unit: Optional[str]
        deviceClass: Optional[str]
        icon: Optional[str]
        platform: Platform
        error: Optional[str] = None

def deviceSensor(name: str, registryKey: str, unit: str, device_class: str, icon: str, platform: Platform, 
                 schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str], 
                 converter: Optional[Callable[[str], Union[str, bool, int]]] = None) -> DeviceSchema:
        device = get_value_from_map(schema_xml_map, registryKey, registry_mapper, converter)
        return DeviceSchema(
            name=name,
            value=device.value,
            registryKey=registryKey,
            unit=unit,
            deviceClass=device_class,
            icon=icon,
            platform=platform,
            error=device.error
        )
