import datetime
import requests

from ResponseFactory import ResponseFactory


class GivEnergyApi:
    API_ROOT = 'https://www.givenergy.cloud/GivManage/api/'
    API_LOGIN = f'{API_ROOT}login'
    API_PLANT_SUMMARY = f'{API_ROOT}plant/getPlantSummary'
    API_INVERTER_DAY_MULTI_LINE = f'{API_ROOT}invChart/dayMultiLine'

    def __init__(self):
        self.session = None
        self.inverterSerialNum = ''
        self.authenticated = False

    def authenticate(self, account, password):
        self.session = requests.session()
        payload = {'account': account, 'password': password}
        response = self.session.post(GivEnergyApi.API_LOGIN, data=payload)

        json = None
        if response.status_code == 200:
            json = response.json()

        if json is not None:
            self.authenticated = json['success']
            if self.authenticated:
                self.inverterSerialNum = json['inverters'][0]['serialNum']

        return self.authenticated

    def today_summary(self):
        result = None
        if self.session is not None and self.authenticated:
            json = self.request_json(GivEnergyApi.API_PLANT_SUMMARY)
            result = ResponseFactory.parse_today_summary(json)

        return result

    def inverter_day_multi_line(self, day: datetime.date):
        result = None
        if self.session is not None and self.authenticated:
            payload = {'serialNum': self.inverterSerialNum,
                       'dateText': day.isoformat(),
                       'forPlant': True}
            json = self.request_json(GivEnergyApi.API_INVERTER_DAY_MULTI_LINE, payload)
            result = ResponseFactory.inverter_day_multi_line(json)

        return result

    def request_json(self, request, payload=None):
        if payload is None:
            payload = {}
        json = None
        if self.session is not None and self.authenticated:
            response = self.session.post(request, data=payload)
            if response.status_code == 200:
                json = response.json()
                print(json)
        return json
