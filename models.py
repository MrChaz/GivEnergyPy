import datetime


class TodaySummary:
    importedKW: float
    exportedKW: float
    generatedKW: float
    consumedKW: float

    def __init__(self, imported: float, exported: float, generated: float, consumed: float):
        self.importedKW = imported
        self.exportedKW = exported
        self.generatedKW = generated
        self.consumedKW = consumed

    def __str__(self):
        return f"imported: {self.importedKW} kW ~ " \
               f"exported: {self.exportedKW} kW ~ " \
               f"generated: {self.generatedKW} kW ~ " \
               f"consumed: {self.consumedKW} kW"


class DataPoint:
    hour: int
    minute: int
    time: datetime.datetime
    loadPower: float

    def __init__(self, load_power: float, hour: int, minute: int, time: datetime.datetime):
        self.loadPower = load_power
        self.hour = hour
        self.minute = minute
        self.time = time

    def __str__(self):
        return f'DataPoint: {self.time} load:{self.loadPower}'
