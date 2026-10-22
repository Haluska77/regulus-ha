from pydantic import BaseModel

from ...schema import DeviceSchema


class SolarResponseSchema(BaseModel):
    solarPumpPower: DeviceSchema
    solarStatus: DeviceSchema
    solarPanelTemperature: DeviceSchema
    solarConsumer1Heating: DeviceSchema
    solarConsumer1Enabled: DeviceSchema
    solarConsumer1Temperature: DeviceSchema
    solarConsumer1Demand: DeviceSchema
    solarConsumer1MaximumTemperature: DeviceSchema
    solarConsumer2Heating: DeviceSchema
    solarConsumer2Enabled: DeviceSchema
    solarConsumer2Temperature: DeviceSchema
    solarConsumer2Demand: DeviceSchema
    solarConsumer2MaximumTemperature: DeviceSchema
    solarConsumer3Heating: DeviceSchema
    solarConsumer3Enabled: DeviceSchema
    solarConsumer3Temperature: DeviceSchema
    solarConsumer3Demand: DeviceSchema
    solarConsumer3MaximumTemperature: DeviceSchema
