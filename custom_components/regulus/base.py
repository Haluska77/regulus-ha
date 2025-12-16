from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, NAME, COMPANY


class DynamicBase(CoordinatorEntity):

    def __init__(self, coordinator, configEntry, key, sensor_data):
        super().__init__(coordinator)

        self._coordinator = coordinator
        self._api = coordinator.api
        self._key = key

        self._attr_unique_id = f"{DOMAIN}_{key}"
        self._attr_name = sensor_data["name"]
        self._attr_icon = sensor_data.get("icon")
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"{configEntry.entry_id}_{coordinator.api.key}")},
            name=f"{NAME} - {coordinator.api.name}",
            manufacturer=COMPANY,
            model=f"IR {configEntry.options.get("ir_version", configEntry.data["ir_version"])}",
            entry_type="service",
        )

        self._registry_key = sensor_data.get("registryKey")
        self._error = sensor_data.get("error")
