from decouple import config
import requests
import json


PROFILE_ID = config('PROFILE_ID')
WISE_TOKEN = config('WISE_TOKEN')

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

class Wise:

    WISE_API = 'https://api.transferwise.com'
    WISE_URL = {
        'balance': f'''{WISE_API}/v1/borderless-accounts?profileId={PROFILE_ID}'''
    }

    def get_balance(self):        
        r = requests.get(self.WISE_URL['balance'], auth=BearerAuth(WISE_TOKEN))
        try:
            if r.status_code != 200:
                raise Exception('HTTP response code not 200')
            balance_data = json.loads(r.content)
            if (balance_data):
                return {'error': False, 'data': balance_data[0]['balances'][0]['amount']['value']}
            else:
                raise Exception('Wrong JSON response')
        except Exception as error:
            return {'error': True, 'message': error}       