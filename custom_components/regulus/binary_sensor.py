from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform

from .schema import SensorSchema
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=5)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    dashboard_coordinator = hass.data[DOMAIN][entry.entry_id]["dashboard_coordinator"]

    entities = []
    for key, value in dashboard_coordinator.data.items():
        if value["platform"] == Platform.BINARY_SENSOR:
            entities.append(DynamicSensor(dashboard_coordinator, key, value))

    async_add_entities(entities)


class DynamicSensor(BinarySensorEntity):
    def __init__(self, coordinator, key: str, value: SensorSchema):
        self._coordinator = coordinator
        self._key = key
        self.value = value

    @property
    def unique_id(self):
        return f"{self._key}_binary_sensor"

    @property
    def name(self):
        return self.value.get("name")

    @property
    def state(self):
        return self._coordinator.data[self._key].get("value")

    @property
    def native_unit_of_measurement(self):
        return self.value.get("unit")

    @property
    def device_class(self):
        return self.value.get("deviceClass")

    @property
    def icon(self):
        return self.value.get("icon")

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self._coordinator.async_request_refresh()

    async def async_added_to_hass(self):
        self._coordinator.async_add_listener(self.async_write_ha_state)
