# Tentativa Binance rodando em um interválo de tempo.
import schedule
import time
import regex as re
import requests
from bs4 import BeautifulSoup

#Primeiro criar uma função ou tarefa que vai ser realizada

def precobitcoin():
  resposta = requests.get('https://www.binance.com/pt-BR/price/bitcoin')
  conteudo = resposta.content
  binance = BeautifulSoup(conteudo, 'html.parser')
  bitcoin = binance.find('div', attrs={'class': 'css-1267ixm'})

  preco = bitcoin.find('div', attrs={'class': 'css-12ujz79'})
  preco = preco.text
  caractere_especial = r'\$'
  mensagem = re.sup(caractere_especial, '', preco)
  print(mensagem)

# schedule.cada.tempo.fazer

schedule.every(10).seconds.do(precobitcoin)

while 1:
  schedule.run_pending()
  time.sleep(1)