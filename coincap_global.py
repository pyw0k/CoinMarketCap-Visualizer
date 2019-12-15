import json
import requests

global_url = 'https://api.coinmarketcap.com/v2/global'

request = requests.get(global_url)
results = request.json()

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
<<<<<<< HEAD
=======
global_cap = results['data']['quotes']['USD']['total_market_cap']
>>>>>>> 996f75bcd819cfe9e380a4b6ddf3bb52ac9f6660
global_volume = results['data']['quotes']['USD']['total_volume_24h']

print()
print('There are currently ' + str(active_currencies) + ' active currencies and ' + str(active_markets) + '.')
<<<<<<< HEAD
=======
print('The global cap of all cryptos is ' + str(global_cap) + ' and the 24h global volume is ' + str(global_volume) + '.')
>>>>>>> 996f75bcd819cfe9e380a4b6ddf3bb52ac9f6660
print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '.')
print()
import json
import requests

global_url = 'https://api.coinmarketcap.com/v2/global'

request = requests.get(global_url)
results = request.json()

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes']['USD']['total_market_cap']
global_volume = results['data']['quotes']['USD']['total_volume_24h']

print()
print('There are currently ' + str(active_currencies) + ' active currencies and ' + str(active_markets) + '.')
print('The global cap of all cryptos is ' + str(global_cap) + ' and the 24h global volume is ' + str(global_volume) + '.')
print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '.')
print()
print('This information was last updated on ' + str(last_updated) + '.')