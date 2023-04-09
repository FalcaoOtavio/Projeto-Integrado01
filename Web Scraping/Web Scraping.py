#Importar Bibliotecas
import requests
from bs4 import BeautifulSoup

#Incluir o par BTC/BRL
url_btcbrl = 'https://www.binance.com/pt-BR/trade/BTC_BRL?theme=dark&type=spot'

#Continuação do Código...
url = 'https://www.binance.com/pt-BR/trade/BTC_USDT?theme=dark&type=spot'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site_binance = requests.get(url, headers)
soup = BeautifulSoup(site_binance.content, 'html.parser')

valor_btcusdt = soup.find('div', class_ = 'subPrice')

print(valor_btcusdt)