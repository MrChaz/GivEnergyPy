import json
from functools import reduce

from givenergy import GivEnergyApi


class Appliance:
    name = ''
    averageConsumptionWatts = 0.0

    def __init__(self, name: str, average_consumption_watts: float):
        self.name = name
        self.averageConsumptionWatts = average_consumption_watts


def load_appliances():
    loaded = []
    json_data = json.load(open('appliance_data.json'))
    for name, data in json_data.items():
        loaded.append(Appliance(name, data['averageConsumptionWatts']))
    return loaded


api = GivEnergyApi()
success = api.authenticate('login', 'password')
print(f'Authenticated with GivEnergy? {success}')

# For now let's assume we've worked out the amount of energy used and saved that previously.
appliances = load_appliances()

# This could be in a loop or in a chron job
snapshot = api.snapshot()
print(f'received: {snapshot}')

if snapshot is not None and snapshot.gridPowerWatts > 0:

    # find out if any of the appliance can be run now
    available = snapshot.gridPowerWatts
    usable = filter(lambda x: x.averageConsumptionWatts < available, appliances)

    combined = []
    for item in usable:
        print(f'we could use {item.name}')

        available = available - item.averageConsumptionWatts
        if available > 0:
            combined.append(item)

    combined_names = reduce(lambda old, cur: f'{old}, {cur.name}', combined, '')
    print(f'we could use {combined_names} all at once')
else:
    print('no headroom for appliances')
