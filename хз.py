import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random

token = '5574492322:AAGE7NS1XoN8Mdk6Ni9oKf7_4V-p_8b0iq0'
bot = telebot.TeleBot(token)
URL = 'https://www.anekdot.ru/best/anekdot/0708/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='text')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Анекдоты")
    item2 = types.KeyboardButton("Кнопка2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Чо вам надо?', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Анекдоты":
        bot.send_message(message.chat.id, random.choice(quotes))
    elif message.text == 'Кнопка №2':
        bot.send_message(message.chat.id, 'Кнопка 2')
    if message.text == 'Покажи':
        bot.send_message(message.chat.id, 'Я показал')


bot.infinity_polling()
