from pydantic import BaseModel
from typing import Dict, Optional, Union, Callable

class RegistryResult(BaseModel):
    value: Optional[Union[str, bool, int]]
    error: Optional[str]
    
def parse_xml_to_map(xml: str) -> Dict[str, str]:
    return parse_xml(get_registry_map, xml)


def parse_acer_value(xml: str) -> str:
    return parse_xml(get_acer_value, xml)


def get_registry_map(parsed: Dict) -> Dict[str, str]:
    result = {}
    try:
        inputs = parsed["PAGE"]["INPUT"]
        if not isinstance(inputs, list):
            inputs = [inputs]

        for input_item in inputs:
            name = input_item.get("@NAME", "UNKNOWN")
            value = input_item.get("@VALUE", "")
            result[name] = value
    except Exception as e:
        print("Error extracting registry map:", e)
    return result


def get_acer_value(parsed: Dict) -> str:
    try:
        return parsed["LOGIN"]["ACER"].get("@VALUE", "")
    except Exception as e:
        print("Error extracting ACER value:", e)
        return ""


def parse_xml(operation, xml: str):
    try:
        import xmltodict
    except ImportError:
        raise ImportError("Please install xmltodict using `pip install xmltodict`")

    try:
        parsed = xmltodict.parse(xml)
        return operation(parsed)
    except Exception as e:
        print("Error parsing XML:", e)
        raise e


def get_value_from_map(
    response_map: Dict[str, str], sensor_name: str, registry_mapper: Dict[str, str], converter: Optional[Callable[[str], Union[str, bool, int]]] = None
) -> RegistryResult:
    registry_name = registry_mapper.get(sensor_name)
    if registry_name is None:
        msg = (
            f"Application mapping is invalid. Sensor '{sensor_name}' is not assigned "
            f"to any Regulus Registry name."
        )
        return RegistryResult(value=None, error=msg)

    registry_value = response_map.get(registry_name)

    if registry_value is None:
        msg = (
            f"Property '{sensor_name}' is assigned to registry '{registry_name}', "
            f"but is not found in response xml"
        )
        return RegistryResult(value=None, error=msg)

    converted_value = converter(registry_value) if converter else registry_value
    return RegistryResult(value=converted_value, error=None)