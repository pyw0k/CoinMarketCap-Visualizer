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
	'X-CMC_PRO_API_KEY': 'API_KEY',
}

session = Session()
session.headers.update(headers)

try:
	response = session.get(url, params=parameters)
	data = json.loads(response.text)
	print(data['data'][0]['quote']['USD']['price'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)