from datetime import datetime

from models import DataPoint


class Utility:
    @staticmethod
    def extract_subset(items: [DataPoint], lower: datetime, upper: datetime):
        filtered = []
        for x in items:
            if x.time > lower:
                filtered.append(x)
            if x.time > upper:
                break
        return filtered
