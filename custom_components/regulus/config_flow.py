from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers.selector import selector
from .const import DOMAIN, IR_VERSION_ALIASES, IR_VERSION_OPTIONS, POLLING_INTERVAL
from . import API_CLASSES

class HeatPumpConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Heat Pump", data=user_input)
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str,
                vol.Required("username"): str,
                vol.Required("password"): str,
                vol.Required("ir_version", default=IR_VERSION_OPTIONS[1]): selector({"select": {"options": IR_VERSION_OPTIONS}}),
                vol.Required("polling_interval", default=POLLING_INTERVAL): vol.All(vol.Coerce(int), vol.Range(min=1)),
            }),
        )
    
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry):
        return HeatPumpOptionsFlow()

class HeatPumpOptionsFlow(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        config_entry = self.config_entry
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        #legacy support for ir_version as int
        raw_ir_version = config_entry.options.get("ir_version", config_entry.data.get("ir_version", IR_VERSION_OPTIONS[0]))
        ir_version = IR_VERSION_ALIASES[raw_ir_version]
            
        schema = {}
        schema[vol.Required("ir_version", default=ir_version)] = selector({"select": {"options": IR_VERSION_OPTIONS}})
        schema[vol.Required("polling_interval", default=config_entry.options.get("polling_interval", config_entry.data.get("polling_interval", POLLING_INTERVAL)))] = vol.All(vol.Coerce(int), vol.Range(min=1))
        for api in API_CLASSES:
            option_key = f"enable_{api.key}"
            schema[vol.Required(option_key, default=config_entry.options.get(option_key, True))] = bool
            
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(schema)
        )
