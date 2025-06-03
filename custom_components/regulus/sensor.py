from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from homeassistant.helpers.typing import HomeAssistantType, ConfigType
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN
from custom_components.regulus.api.dashboard.dashboard_api import DashboardApi


DataUpdateCoordinator_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=5)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    ip = data["ip_address"]
    username = data["username"]
    password = data["password"]

    dashboard_api = hass.data[DOMAIN]["api"]

    async def async_update_data():
        return await hass.async_add_executor_job(dashboard_api.route_fetch)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="dashboard_api",
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL,
    )

    await coordinator.async_config_entry_first_refresh()

    entities = []
    for key, value in coordinator.data.items():
        metadata = SENSOR_METADATA.get(key, {})
        entities.append(DynamicSensor(coordinator, key, metadata))

    async_add_entities(entities)


class DynamicSensor(SensorEntity):
    def __init__(self, coordinator, key: str, metadata: dict):
        self._coordinator = coordinator
        self._key = key
        self._metadata = metadata

    @property
    def name(self):
        return self._metadata.get("name", self._key.replace("_", " ").title())

    @property
    def unique_id(self):
        return f"dashboard_{self._key}"

    @property
    def native_value(self):
        try:
            return float(self._coordinator.data.get(self._key))
        except (TypeError, ValueError):
            return self._coordinator.data.get(self._key)

    @property
    def native_unit_of_measurement(self):
        return self._metadata.get("unit")

    @property
    def device_class(self):
        return self._metadata.get("device_class")

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self._coordinator.async_request_refresh()

    async def async_added_to_hass(self):
        self._coordinator.async_add_listener(self.async_write_ha_state)
