# chat bot telegram    pip install pytelegrambotapi
import telebot
from telebot import TeleBot
import requests
from bs4 import BeautifulSoup

chave_api = '6138948203:AAGll3mwxTcfm5HLyJXQOiMOcCm4TXN0Ios'

bot = telebot.TeleBot(chave_api)

print('BOT INICIADO')

@bot.message_handler(commands=['Bitcoin'])
def Bitcoin(mensagem):
    response = requests.get('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwj3__mvg53-AhWVu5UCHf6EAFwQ-fUHegQIBhAf')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    preco = site.find('div', attrs={'class': 'YMlKec fxKbKc'})
    texto = f'O valor atualizado da Bitcoin é de R${preco.text}'
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Ethereum'])
def Bitcoin(mensagem):
    response = requests.get('https://www.google.com/finance/quote/ETH-BRL')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    preco = site.find('div', attrs={'class': 'YMlKec fxKbKc'})
    texto = f'O valor atualizado da Ethereum é de R${preco.text}'
    bot.send_message(mensagem.chat.id, texto)



def verificar(mensagem):        # Independete da mensagem, a função retorna verdadeira
  return True

@bot.message_handler(func=verificar)        # Pega a informação do polling e diz quando a função deve ser executada
def responder(mensagem):
  texto = """
  Bem vindo ao Alert Crypto, selecione a criptmoeda desejada:
  
  /Bitcoin
  
  /Ethereum """
  
  bot.send_message(mensagem.chat.id, texto)



bot.polling()           #'loopin' que verifica as mensagens do bot 