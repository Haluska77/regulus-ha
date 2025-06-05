from datetime import timedelta
import logging

from .schema import SensorSchema
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=5)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
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
    # _LOGGER.debug("Coordinator data: %s", coordinator.data)

    entities = []
    for key, value in coordinator.data.items():
        entities.append(DynamicSensor(coordinator, key, value))

    async_add_entities(entities)


class DynamicSensor(SensorEntity):
    def __init__(self, coordinator, key: str, value: SensorSchema):
        self._coordinator = coordinator
        self._key = key
        self.value = value

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
