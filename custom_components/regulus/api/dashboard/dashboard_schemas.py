from pydantic import BaseModel
from typing import Optional


class ZoneSchema(BaseModel):
    status: Optional[bool]
    actualTemperature: Optional[str]
    requiredTemperature: Optional[str]
    actualHeatingWaterTemperature: Optional[str]
    requiredHeatingWaterTemperature: Optional[str]


class HeatPumpSchema(BaseModel):
    runningStatus: Optional[bool]
    outletTemperature: Optional[str]
    inletTemperature: Optional[str]


class AkuSchema(BaseModel):
    status: Optional[bool]
    topTemperature: Optional[str]
    bottomTemperature: Optional[str]
    requiredTemperature: Optional[str]


class WaterSchema(BaseModel):
    status: Optional[bool]
    actualTemperature: Optional[str]
    requiredTemperature: Optional[str]


class SolarSchema(BaseModel):
    status: Optional[bool]
    panelTemperature: Optional[str]


class CirculationSchema(BaseModel):
    status: Optional[bool]


class DashboardResponseSchema(BaseModel):
    outdoorTemperature: Optional[str]
    rcTariff: Optional[str]
    holiday: Optional[str]
    heatPump: HeatPumpSchema
    zone1: ZoneSchema
    zone2: ZoneSchema
    aku: AkuSchema
    water: WaterSchema
    solar: SolarSchema
    circulation: CirculationSchema  # Description can be added in API layer

