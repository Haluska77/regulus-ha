from pydantic import BaseModel
from ...schema import DeviceSchema

class HeatPumpResponseSchema(BaseModel):
    runningTime: DeviceSchema
    idleTime: DeviceSchema
    overallStatisticsTotalHours: DeviceSchema
    overallStatisticsTotalStarts: DeviceSchema
    overallStatisticsTodayHours: DeviceSchema
    overallStatisticsTodayMinutes: DeviceSchema
    overallStatisticsTodayStarts: DeviceSchema
    overallStatisticsYesterdayHours: DeviceSchema
    overallStatisticsYesterdayMinutes: DeviceSchema
    overallStatisticsYesterdayStarts: DeviceSchema
    hotWaterStatisticsTotalHours: DeviceSchema
    hotWaterStatisticsTotalStarts: DeviceSchema
    hotWaterStatisticsTodayHours: DeviceSchema
    hotWaterStatisticsTodayMinutes: DeviceSchema
    hotWaterStatisticsTodayStarts: DeviceSchema
    hotWaterStatisticsYesterdayHours: DeviceSchema
    hotWaterStatisticsYesterdayMinutes: DeviceSchema
    hotWaterStatisticsYesterdayStarts: DeviceSchema