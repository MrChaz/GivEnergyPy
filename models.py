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


class Snapshot:
    solarGenerationWatts = 0.0
    gridPowerWatts = 0.0
    currentLoadWatts = 0.0

    def __init__(self, solar_generation_watts: float, grid_power_watts: float, current_load_watts: float):
        self.solarGenerationWatts = solar_generation_watts
        self.gridPowerWatts = grid_power_watts
        self.currentLoadWatts = current_load_watts

    def __str__(self):
        return f'Snapshot: generating:{self.solarGenerationWatts} ' \
               f'using:{self.currentLoadWatts} ' \
               f'grid:{self.gridPowerWatts}'
