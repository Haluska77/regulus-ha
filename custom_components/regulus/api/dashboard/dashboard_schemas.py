from pydantic import BaseModel
from ...schema import SensorSchema

class DashboardResponseSchema(BaseModel):
    outdoorTemperature: SensorSchema
    rcTariff: SensorSchema
    holiday: SensorSchema
    heatPumpRunningStatus: SensorSchema
    heatPumpOutletTemperature: SensorSchema
    heatPumpInletTemperature: SensorSchema
    zone1Status: SensorSchema
    zone1ActualTemperature: SensorSchema
    zone1RequiredTemperature: SensorSchema
    zone1ActualHeatingWaterTemperature: SensorSchema
    zone1RequiredHeatingWaterTemperature: SensorSchema
    zone2Status: SensorSchema
    zone2ActualTemperature: SensorSchema
    zone2RequiredTemperature: SensorSchema
    zone2ActualHeatingWaterTemperature: SensorSchema
    zone2RequiredHeatingWaterTemperature: SensorSchema
    akuStatus: SensorSchema
    akuTopTemperature: SensorSchema
    akuBottomTemperature: SensorSchema
    akuRequiredTemperature: SensorSchema
    waterStatus: SensorSchema
    waterActualTemperature: SensorSchema
    waterRequiredTemperature: SensorSchema
    solarStatus: SensorSchema
    solarPanelTemperature: SensorSchema
    circulationStatus: SensorSchema

