from pydantic import BaseModel
from typing import Optional
from ...schema import SensorSchema

class HeatPumpResponseSchema(BaseModel):
    runningTime: SensorSchema
    idleTime: SensorSchema
    overallStatisticsTotalHours: SensorSchema
    overallStatisticsTotalStarts: SensorSchema
    overallStatisticsTodayHours: SensorSchema
    overallStatisticsTodayMinutes: SensorSchema
    overallStatisticsTodayStarts: SensorSchema
    overallStatisticsYesterdayHours: SensorSchema
    overallStatisticsYesterdayMinutes: SensorSchema
    overallStatisticsYesterdayStarts: SensorSchema
    hotWaterStatisticsTotalHours: SensorSchema
    hotWaterStatisticsTotalStarts: SensorSchema
    hotWaterStatisticsTodayHours: SensorSchema
    hotWaterStatisticsTodayMinutes: SensorSchema
    hotWaterStatisticsTodayStarts: SensorSchema
    hotWaterStatisticsYesterdayHours: SensorSchema
    hotWaterStatisticsYesterdayMinutes: SensorSchema
    hotWaterStatisticsYesterdayStarts: SensorSchema