from homeassistant.core import HomeAssistant
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .schema import DeviceSchema
from .const import DOMAIN
from .base import DynamicBase

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    entities = []

    for coordinator in hass.data[DOMAIN][entry.entry_id]["coordinators"]:
        for key, value in coordinator.data.items():
            if value["platform"] == Platform.SWITCH:
                entities.append(DynamicSwitch(coordinator, entry, key, value))

    async_add_entities(entities)


class DynamicSwitch(DynamicBase, SwitchEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, configEntry: ConfigEntry, key: str, sensor_data: DeviceSchema):
        super().__init__(coordinator, configEntry, key, sensor_data)
                
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
        
    async def async_turn_on(self, **kwargs) -> None:
        body = {self._registry_key: "1"}
        await self.hass.async_add_executor_job(self._api.route_update, body)
        await self._coordinator.async_request_refresh()
        
    async def async_turn_off(self, **kwargs) -> None:
        body = {self._registry_key: "0"}
        await self.hass.async_add_executor_job(self._api.route_update, body)
        await self._coordinator.async_request_refresh()