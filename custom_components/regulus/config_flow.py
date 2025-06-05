from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

IR_VERSION_OPTIONS = ["12", "14"]

class HeatPumpConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Heat Pump", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address", default=""): str,
                vol.Required("username", default=""): str,
                vol.Required("password", default=""): str,
                vol.Required("ir_version", default=IR_VERSION_OPTIONS[1]): vol.In(IR_VERSION_OPTIONS)
            }),
        )
    
@staticmethod
def async_get_options_flow(config_entry):
    return HeatPumpOptionsFlow(config_entry)

class HeatPumpOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Heat Pump", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("ip_address", default=self.config_entry.options.get("ip_address", self.config_entry.data.get("ip_address", ""))): str,
                vol.Required("username", default=self.config_entry.options.get("username", self.config_entry.data.get("username", ""))): str,
                vol.Required("password", default=self.config_entry.options.get("password", self.config_entry.data.get("password", ""))): str,
                vol.Required("ir_version", default=self.config_entry.options.get("ir_version", self.config_entry.data.get("ir_version", IR_VERSION_OPTIONS[0]))): vol.In(IR_VERSION_OPTIONS)
            })
        )