from pydantic import BaseModel

from ..schema import DeviceSchema


class SolarResponseSchema(BaseModel):
    pumpPower: DeviceSchema
    status: DeviceSchema
    panelTemperature: DeviceSchema
    consumer1state: DeviceSchema
    consumer1Heating: DeviceSchema
    consumer1Enabled: DeviceSchema
    consumer1Temperature: DeviceSchema
    consumer1Demand: DeviceSchema
    consumer1MaximumTemperature: DeviceSchema
    consumer2state: DeviceSchema
    consumer2Heating: DeviceSchema
    consumer2Enabled: DeviceSchema
    consumer2Temperature: DeviceSchema
    consumer2Demand: DeviceSchema
    consumer2MaximumTemperature: DeviceSchema
    consumer3state: DeviceSchema
    consumer3Heating: DeviceSchema
    consumer3Enabled: DeviceSchema
    consumer3Temperature: DeviceSchema
    consumer3Demand: DeviceSchema
    consumer3MaximumTemperature: DeviceSchema
