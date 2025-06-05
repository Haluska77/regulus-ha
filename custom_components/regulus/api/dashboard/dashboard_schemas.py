from pydantic import BaseModel
from typing import Optional
from ...schema import SensorSchema

class DashboardResponseSchema(BaseModel):
    outdoorTemperature: SensorSchema
    # rcTariff: Optional[str]
    # holiday: Optional[str]
    heatPumpRunningStatus: SensorSchema
    # heatPumpOutletTemperature: Optional[str]
    # heatPumpInletTemperature: Optional[str]
    # zone1Status: Optional[bool]
    # zone1ActualTemperature: Optional[str]
    # zone1RequiredTemperature: Optional[str]
    # zone1ActualHeatingWaterTemperature: Optional[str]
    # zone1RequiredHeatingWaterTemperature: Optional[str]
    # zone2Status: Optional[bool]
    # zone2ActualTemperature: Optional[str]
    # zone2RequiredTemperature: Optional[str]
    # zone2ActualHeatingWaterTemperature: Optional[str]
    # zone2RequiredHeatingWaterTemperature: Optional[str]
    # akuStatus: Optional[bool]
    # akuTopTemperature: Optional[str]
    # akuBottomTemperature: Optional[str]
    # akuRequiredTemperature: Optional[str]
    # waterStatus: Optional[bool]
    # waterActualTemperature: Optional[str]
    # waterRequiredTemperature: Optional[str]
    # solarStatus: Optional[bool]
    # solarPanelTemperature: Optional[str]
    # circulationStatus: Optional[bool]

