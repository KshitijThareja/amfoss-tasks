import os
import telebot
import requests
import json
import csv
import urllib3
import pandas as pd
import itertools
from collections import OrderedDict
from io import StringIO

yourkey = os.getenv('245044c9')
bot_id = os.getenv('5961128583:AAFQLGENuHnjcIB-mg4p-knnjvW-tcL08dw')

bot = telebot.TeleBot('5961128583:AAFQLGENuHnjcIB-mg4p-knnjvW-tcL08dw')


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    os.remove('moviedetails.csv')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    a= message.text
    moviename= a[7:100]
    

    response =  requests.get(f"http://www.omdbapi.com/?apikey=245044c9&t={moviename}")
    


    movie_data = response.json()
    y = json.loads(json.dumps(movie_data))
    p= y['Poster']
    q= y['Title']
    w= y['Year']
    e= y['imdbRating']
    print (q,w,e)
    d= {}
    d.update({'Title': q, 'Year': w, 'imdbRating': e})
    telem= f"Title: {q},\n Year: {w},\n IMDB Rating: {e}"
    
    json_object = json.dumps(d, indent = 4)

    bot.send_photo(message.chat.id, p)
    
    bot.send_message(message.chat.id, telem)

    with open('details.json', 'w') as json_file:text= json.dump(json_object, json_file)
    print(text)
    with open('moviedetails.csv', 'a') as csvfile:
        fieldnames = ['Title', 'Year', 'imdbRating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Title': q, 'Year': w, 'imdbRating': e})
    
    
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    print(message)
    bot.send_document(message.chat.id, document=open('moviedetails.csv', 'rb'))

    


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()