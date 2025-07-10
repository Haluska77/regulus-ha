from homeassistant.core import HomeAssistant
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform

from .schema import SensorSchema
from .const import DOMAIN, NAME, COMPANY

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    dashboard_coordinator = hass.data[DOMAIN][entry.entry_id]["dashboard_coordinator"]
    heatpump_coordinator = hass.data[DOMAIN][entry.entry_id]["heatpump_coordinator"]

    entities = []

    coordinators = [dashboard_coordinator, heatpump_coordinator]

    for coordinator in coordinators:
        for key, value in coordinator.data.items():
            if value["platform"] == Platform.SENSOR:
                entities.append(DynamicSensor(coordinator, entry, key, value))

    async_add_entities(entities)


class DynamicSensor(SensorEntity):
    def __init__(self, coordinator, configEntry: ConfigEntry, key: str, sensor_data: SensorSchema):
        self._coordinator = coordinator
        self._key = key
        self._attr_unique_id = f"{DOMAIN}_{key}"        
        self._attr_name = sensor_data["name"]
        self._attr_native_unit_of_measurement = sensor_data.get("unit")
        self._attr_device_class = sensor_data.get("deviceClass")
        self._attr_icon = sensor_data.get("icon")
        self._attr_device_info = {
            "identifiers": {(DOMAIN, configEntry.entry_id)},
            "name": NAME,
            "manufacturer": COMPANY,
            "model": "all models",
            "entry_type": "service",
        }

    @property
    def native_value(self):
        return self._coordinator.data[self._key]["value"]["value"]

    @property
    def extra_state_attributes(self) -> dict:
        attrs = {}
        if self._coordinator.data[self._key]["value"]["error"]:
            attrs["regulus_error"] = self._coordinator.data[self._key]["value"]["error"]
        return attrs

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self._coordinator.async_request_refresh()

    async def async_added_to_hass(self):
        self._coordinator.async_add_listener(self.async_write_ha_state)
