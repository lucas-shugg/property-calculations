import requests
import json

URL_ENDPOINT = 'https://api.domain.com.au/v1/'
PROPERTIES_ENDPOINT = URL_ENDPOINT + 'properties/'
LISTINGS_ENDPOINT = URL_ENDPOINT + 'listings/'
DEFAULT_PAGE_SIZE = 1

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
    url = PROPERTIES_ENDPOINT + property_id
    res = requests.get(url, headers=get_auth_header())
    return res.json()


def get_price_estimation(property_id):
    url = PROPERTIES_ENDPOINT + property_id + "/priceEstimate"
    res = requests.get(url, headers=get_auth_header())
    return res.json()


def search_properties(terms):
    url = PROPERTIES_ENDPOINT + "_suggest?terms=" + terms + f"&pageSize={DEFAULT_PAGE_SIZE}"
    res = requests.get(url, headers=get_auth_header())
    return res.json()


def get_listings(id):
    url = LISTINGS_ENDPOINT + id
    res = requests.get(url, headers=get_auth_header())
    return res.json()

res = search_properties("coast")

properties = list(map(lambda property: get_property_info(property["id"]), res))

# print(get_property_info("YQ-6763-JX"))
print(properties)
print(list(map(lambda property: property["addressId"], properties)))



{'imageType': 'Property', 'advertId': 2010116351, 'date': '2013-04-11T04:40:39.503Z', 'fullUrl': 'https://bucket-api.domain.com.au/v1/bucket/image/w800-h600-2010116351_1_pi_150313_053608', 'rank': 1}
