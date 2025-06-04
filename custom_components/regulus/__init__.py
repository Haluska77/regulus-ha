from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.const import Platform
from .api.dashboard.dashboard_api import DashboardApi
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    config = {
        "host": entry.data["ip_address"],
        "user": entry.data["username"],
        "password": entry.data["password"],
        "ir_version": entry.data["ir_version"]
    }
    try:
        api = DashboardApi(config)
        await hass.async_add_executor_job(api.route_fetch)
    except Exception as e:
        raise ConfigEntryNotReady(f"Could not connect to Regulus device: {e}")

    hass.data[DOMAIN]["api"] = api
    hass.data[DOMAIN][entry.entry_id] = config

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR])
    
    return True
