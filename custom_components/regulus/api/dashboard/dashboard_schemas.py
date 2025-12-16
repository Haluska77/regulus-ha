from pydantic import BaseModel
from ...schema import DeviceSchema

class DashboardResponseSchema(BaseModel):
    outdoorTemperature: DeviceSchema
    rcTariff: DeviceSchema
    holiday: DeviceSchema
    heatPumpRunningStatus: DeviceSchema
    heatPumpOutletTemperature: DeviceSchema
    heatPumpInletTemperature: DeviceSchema
    zone1Status: DeviceSchema
    zone1ActualTemperature: DeviceSchema
    zone1RequiredTemperature: DeviceSchema
    zone1ActualHeatingWaterTemperature: DeviceSchema
    zone1RequiredHeatingWaterTemperature: DeviceSchema
    zone2Status: DeviceSchema
    zone2ActualTemperature: DeviceSchema
    zone2RequiredTemperature: DeviceSchema
    zone2ActualHeatingWaterTemperature: DeviceSchema
    zone2RequiredHeatingWaterTemperature: DeviceSchema
    akuStatus: DeviceSchema
    akuTopTemperature: DeviceSchema
    akuBottomTemperature: DeviceSchema
    akuRequiredTemperature: DeviceSchema
    waterStatus: DeviceSchema
    waterActualTemperature: DeviceSchema
    waterRequiredTemperature: DeviceSchema
    solarStatus: DeviceSchema
    solarPanelTemperature: DeviceSchema
    circulationStatus: DeviceSchema

