from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class HeatPumpConfigFlow(config_entries.OptionsFlow, domain=DOMAIN):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Heat Pump", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("ip_address", default=self.config_entry.options.get("ip_address", "")): str,
                vol.Required("username", default=self.config_entry.options.get("username", "")): str,
                vol.Required("password", default=self.config_entry.options.get("password", "")): str,
                vol.Required("ir_version", default=self.config_entry.options.get("ir_version", "14")): str,
            })
        )
