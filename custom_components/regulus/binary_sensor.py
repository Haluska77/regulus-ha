from homeassistant.core import HomeAssistant
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform

from .schema import DeviceSchema
from .const import DOMAIN, NAME, COMPANY
from .base import DynamicBase

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    entities = []

    for coordinator in hass.data[DOMAIN][entry.entry_id]["coordinators"]:
        for key, value in coordinator.data.items():
            if value["platform"] == Platform.BINARY_SENSOR:
                entities.append(DynamicSensor(coordinator, entry, key, value))

    async_add_entities(entities)


class DynamicSensor(DynamicBase, BinarySensorEntity):
    def __init__(self, coordinator, configEntry: ConfigEntry, key: str, sensor_data: DeviceSchema):
        super().__init__(coordinator, configEntry, key, sensor_data)
        
        self._attr_native_unit_of_measurement = sensor_data.get("unit")
        self._attr_device_class = sensor_data.get("deviceClass")

    @property
    def is_on(self):
        return self._coordinator.data[self._key]["value"]

    @property
    def extra_state_attributes(self) -> dict:
        if self._error:
            return {"error": self._error}
        return {}

    @property
    def should_poll(self):
        return False

    async def async_added_to_hass(self):
        self._coordinator.async_add_listener(self.async_write_ha_state)
