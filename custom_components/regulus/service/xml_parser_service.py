import xml.etree.ElementTree as ET

from typing import Dict, List, Optional
from importlib import import_module
from homeassistant.exceptions import ConfigEntryNotReady


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
    response_map: Dict[str, str], registry_key: str, registry_errors: List[str], ir_version: int
) -> Optional[str]:
    registry_name = load_registry_mapper(ir_version).get(registry_key)
    if registry_name is None:
        msg = (
            f"Application mapping is invalid. Property '{registry_key}' is not assigned "
            f"to any Regulus Registry name."
        )
        registry_errors.append(msg)
        raise ConfigEntryNotReady(msg)

    registry_value = response_map.get(registry_name)
    if registry_value is None:
        msg = (
            f"'{registry_key}' could not be found. '{registry_name}' is missing in xml response or "
            f"'{registry_key}' is mapped to another registry. Please contact Regulus provider."
        )
        registry_errors.append(msg)
        print(
            f"Property '{registry_key}' is assigned to registry '{registry_name}', "
            f"but is not found in response xml"
        )
        return None

    return registry_value

def load_registry_mapper(ir_version: int) -> dict:

    version_map = {
        12: "custom_components.regulus.mapper.registry_mapper_ir12",
        14: "custom_components.regulus.mapper.registry_mapper_ir14",
    }

    module_name = version_map.get(ir_version)
    if not module_name:
        raise ValueError(f"Unsupported ir_version: {ir_version}")

    module = import_module(module_name)
    return module.REGISTRY_MAPPER