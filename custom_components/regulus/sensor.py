from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
import requests

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    ip = data["ip_address"]
    username = data["username"]
    password = data["password"]

    sensors = [
        HeatPumpSensor("Temperature", ip, username, password, "temperature", "°C"),
        HeatPumpSensor("Power", ip, username, password, "power", None),
    ]
    async_add_entities(sensors)

class HeatPumpSensor(Entity):
    def __init__(self, name, ip, username, password, field, unit):
        self._attr_name = f"Heat Pump {name}"
        self._ip = ip
        self._username = username
        self._password = password
        self._field = field
        self._attr_unit_of_measurement = unit
        self._state = None

    @property
    def state(self):
        return self._state

    async def async_update(self):
        try:
            url = f"http://{self._ip}/api/status"
            resp = requests.get(url, auth=(self._username, self._password), timeout=5)
            if resp.status_code == 200:
                self._state = resp.json().get(self._field)
            else:
                self._state = None
        except Exception:
            self._state = None
