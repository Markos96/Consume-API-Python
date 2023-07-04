import requests

name = "Argentina"

URL = f'https://restcountries.com/v3.1/name/{name}'

response = requests.get(URL)

if response.status_code == 200:
    countries = response.json()

    print(countries[0]['name']['common'])
    print(countries[0]['capital'])

else:
    print("Error")
