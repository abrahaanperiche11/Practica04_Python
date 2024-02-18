#almacenar el precio del bitcoin
import requests
url='https://api.coindesk.com/v1/bpi/currentprice.json'
response=requests.get(url)
data = response.json()
precios=data['bpi']

usd=precios['USD']
usd_str=str(usd['rate_float'])

gbp=precios['GBP']
gbp_str=str(gbp['rate_float'])

eur=precios['EUR']
eur_str=str(eur['rate_float'])

lista_precios=[f'precio usd:{usd_str}\n',f'precio gbp:{gbp_str}\n',f'presio eur:{eur_str}\n']

with open('precios.txt',mode='w') as file:
    data=file.writelines(lista_precios)

