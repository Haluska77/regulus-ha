from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from datetime import timedelta
import logging

_LOGGER = logging.getLogger(__name__)

class RegulusUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, api, scan_interval: timedelta):

        async def async_update_data():
            return await hass.async_add_executor_job(api.route_fetch)

        super().__init__(
            hass,
            _LOGGER,
            name=api.name,
            update_method=async_update_data,
            update_interval=scan_interval,
        )
        
        self.api = api