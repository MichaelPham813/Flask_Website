import requests
import json

def get_country_data(name):
    API_KEY = '990|IhCEHr0pu5zag40MSpza6iFBdwEvl4EDCpUrkTLR'
    PAYLOADS = {'Accept':'application/json','Authorization': f'Bearer {API_KEY}'}
    URL = f'https://restfulcountries.com/api/v1/countries/{name}'
    request = requests.get(URL,headers=PAYLOADS)
    response = json.loads(request.text)
    return response
