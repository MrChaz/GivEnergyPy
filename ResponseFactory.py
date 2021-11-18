import datetime

from models import TodaySummary, DataPoint


class ResponseFactory:

    @staticmethod
    def parse_today_summary(json: dict):
        if json is not None:
            return TodaySummary(float(json['importEnergyToday']),
                                float(json['exportEnergyToday']),
                                float(json['energyToday']),
                                float(json['consumptionEnergyToday']))
        else:
            return None

    @staticmethod
    def inverter_day_multi_line(json: dict):
        if json is not None:
            data = json['data']
            if data is not None:
                return map(lambda x: DataPoint(x['loadPower'], x['hour'], x['minute'], datetime.datetime.fromisoformat(x['time'])), data)
        else:
            return None
