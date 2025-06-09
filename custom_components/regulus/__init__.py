import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.const import Platform

from .coordinator import RegulusUpdateCoordinator
from .api.dashboard.dashboard_api import DashboardApi
from .api.heatPump.heatPump_api import HeatPumpApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    config = {
        "host": entry.data["ip_address"],
        "user": entry.data["username"],
        "password": entry.data["password"],
        "ir_version": entry.data["ir_version"]
    }
    try:
        dashboard_api = DashboardApi(config)
        await hass.async_add_executor_job(dashboard_api.route_fetch)
    except Exception as e:
        raise ConfigEntryNotReady(f"Could not connect to Regulus device: {e}")

    dashboard_coordinator = RegulusUpdateCoordinator(hass, "dashboard", dashboard_api)
    await dashboard_coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("Coordinator data: %s", dashboard_coordinator.data)

    heatPump_api = HeatPumpApi(config)
    await hass.async_add_executor_job(heatPump_api.route_fetch)
    heatpump_coordinator = RegulusUpdateCoordinator(hass, "heatPump", heatPump_api)
    await heatpump_coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("Coordinator data: %s", heatpump_coordinator.data)

    hass.data[DOMAIN][entry.entry_id] = {
        "dashboard_coordinator": dashboard_coordinator,
        "heatpump_coordinator": heatpump_coordinator
        }

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR, Platform.BINARY_SENSOR])
    
    return True
