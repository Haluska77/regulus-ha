[![version](https://img.shields.io/github/manifest-json/v/Haluska77/regulus-ha?filename=custom_components%2Fregulus%2Fmanifest.json&label=version)](https://github.com/Haluska77/regulus-ha/releases/latest)
[![releases](https://img.shields.io/github/downloads/Haluska77/regulus-ha/total)](https://github.com/Haluska77/regulus-ha/releases)
[![HACS](https://img.shields.io/badge/HACS-Default-orange.svg)](https://hacs.xyz)

# Regulus Heat Pump Integration
This repository makes integration of Regulus Heat Pumps into Homeassistant. Requires running heat pump connected to local network (obtaining local IP address) and basic login credentials for Regulus app provided by your seller.
This supports IR12 and IR14 version controller. (selected by initial config form)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Haluska77&repository=regulus-ha&category=Integration)

## Installation
### HACS (Recommended)
1. Ensure that HACS is installed
2. Open HACS
3. Search for "Regulus" and download the repository
4. Restart Home Assistant


### Manual
1. Create directory 'regulus' under the 'custom_components' directory in your HA instance. If you dont have 'custom_components' directory, create it under the root directory of your HA.
2. Copy all the files from the this repo custom_components/regulus directory and put it into your newly created 'regulus' directory in your HA.
3. Restart Home Assistant
4. In the HA UI go to "Settings" -> "Devices & services" and click "+ Add Integration". Search for "Regulus"
5. Fill in the initial config form
