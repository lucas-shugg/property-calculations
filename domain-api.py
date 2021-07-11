import requests
import json


url_endpoint = 'https://api.domain.com.au/v1/properties/'
#property_id = 'RF-8884-AK'

def get_auth_header():
    client_id = 'client_edca3ea76673a09feb5ba36b02f61344'
    client_secret = 'secret_681b282780dc8fdd272381cbf812c6b5'
    scopes = ['api_properties_read']
    auth_url = 'https://auth.domain.com.au/v1/connect/token'
    response = requests.post(auth_url, data = {
                    'client_id':client_id,
                    'client_secret':client_secret,
                    'grant_type':'client_credentials',
                    'scope':scopes,
                    'Content-Type':'text/json'
                    })
    json_res = response.json()
    auth = {'Authorization':'Bearer ' + json_res['access_token']}
    return auth


def get_property_info(property_id):
    url = url_endpoint + property_id
    res = requests.get(url, headers=get_auth_header())
    return res.json()


def get_price_estimation(property_id):
    url = url_endpoint + property_id + "/priceEstimate"
    res = requests.get(url, headers=get_auth_header())
    return res.json()


res = get_price_estimation("RF-8884-AK")

print(res)
