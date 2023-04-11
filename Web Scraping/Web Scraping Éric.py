# Bitcoin site do google 

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwj3__mvg53-AhWVu5UCHf6EAFwQ-fUHegQIBhAf')
content = response.content
site = BeautifulSoup(content, 'html.parser')
preco = site.find('div', attrs={'class': 'YMlKec fxKbKc'})
print(preco.text)