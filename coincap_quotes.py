from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
	'start':'1',
	'limit':'1',
	'convert':'USD'
}
headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '4a659ff3-fa69-4d66-8d6f-9639b776435e',
}

session = Session()
session.headers.update(headers)

try:
	response = session.get(url, params=parameters)
	data = json.loads(response.text)
	print(data['data'][0]['quote']['USD']['price'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)