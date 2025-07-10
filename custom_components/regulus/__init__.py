import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.const import Platform
from datetime import timedelta

from .coordinator import RegulusUpdateCoordinator
from .api.dashboard.dashboard_api import DashboardApi
from .api.heatPump.heatPump_api import HeatPumpApi
from .api.home.home_api import HomeApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.debug("SETUP: async_setup_entry called for %s", entry.entry_id)

    hass.data.setdefault(DOMAIN, {})
    config = {
        "host": entry.options.get("ip_address", entry.data["ip_address"]),
        "user": entry.options.get("username", entry.data["username"]),
        "password": entry.options.get("password", entry.data["password"]),
        "ir_version": entry.options.get("ir_version", entry.data["ir_version"]),
        "polling_interval": timedelta(seconds=entry.options.get("polling_interval", entry.data["polling_interval"])),
    }
    try:
        dashboard_api = DashboardApi(config)
        await hass.async_add_executor_job(dashboard_api.route_fetch)
    except Exception as e:
        raise ConfigEntryNotReady(f"Could not connect to Regulus device: {e}")

    dashboard_coordinator = RegulusUpdateCoordinator(hass, "dashboard", dashboard_api, config["polling_interval"])
    await dashboard_coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("Dashboard Coordinator data: %s", dashboard_coordinator.data)

    heatPump_api = HeatPumpApi(config)
    await hass.async_add_executor_job(heatPump_api.route_fetch)
    heatpump_coordinator = RegulusUpdateCoordinator(hass, "heatPump", heatPump_api, config["polling_interval"])
    await heatpump_coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("HeatPump Coordinator data: %s", heatpump_coordinator.data)

    home_api = HomeApi(config)
    await hass.async_add_executor_job(home_api.route_fetch)
    home_coordinator = RegulusUpdateCoordinator(hass, "home", home_api, config["polling_interval"])
    await home_coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("Home Coordinator data: %s", home_coordinator.data)

    hass.data[DOMAIN][entry.entry_id] = {
        "dashboard_coordinator": dashboard_coordinator,
        "heatpump_coordinator": heatpump_coordinator,
        "home_coordinator": home_coordinator,
        }

    entry.async_on_unload(
        entry.add_update_listener(async_reload_entry)
    )

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR, Platform.BINARY_SENSOR])
    
    return True

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    _LOGGER.debug("RELOAD: async_reload_entry called for %s", entry.entry_id)
    await hass.config_entries.async_reload(entry.entry_id)
    
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.debug("UNLOAD: async_unload_entry called for %s", entry.entry_id)
    unload_ok = await hass.config_entries.async_unload_platforms(entry, [Platform.SENSOR, Platform.BINARY_SENSOR])
    if unload_ok:
        del hass.data[DOMAIN][entry.entry_id]
    return unload_ok