import json
import requests

global_url = 'https://api.coinmarketcap.com/v2/global'

request = requests.get(global_url)
results = request.json()

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_volume = results['data']['quotes']['USD']['total_volume_24h']

print()
print('There are currently ' + str(active_currencies) + ' active currencies and ' + str(active_markets) + '.')
print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '.')
print()
print('This information was last updated on ' + str(last_updated) + '.')
