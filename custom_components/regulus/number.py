from homeassistant.core import HomeAssistant
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .schema import DeviceSchema
from .const import DOMAIN
from .service.abstract_api import AbstractApi
from .base import DynamicBase
from typing import TypeVar

T = TypeVar("T")

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    entities = []

    for coordinator in hass.data[DOMAIN][entry.entry_id]["coordinators"]:
        for key, value in coordinator.data.items():
            if value["platform"] == Platform.NUMBER:
                entities.append(DynamicNumber(coordinator, entry, key, value))

    async_add_entities(entities)

class DynamicNumber(DynamicBase, NumberEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, configEntry: ConfigEntry, key: str, 
                 sensor_data: DeviceSchema):
        super().__init__(coordinator, configEntry, key, sensor_data)

        self._attr_native_unit_of_measurement = sensor_data.get("unit")
        self._attr_device_class = sensor_data.get("deviceClass")
        self._attr_native_min_value = sensor_data.get("min", 0)
        self._attr_native_max_value = sensor_data.get("max", 100)
        self._attr_native_step = sensor_data.get("step", 1)
        
    @property
    def native_value(self):
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
        
    async def async_set_native_value(self, value: float) -> None:
        body = {self._registry_key: value}
        await self.hass.async_add_executor_job(self._api.route_update, body)
        await self._coordinator.async_request_refresh()