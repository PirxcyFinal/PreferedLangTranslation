"""
this script gets the accountts prefered language (language u created the account with) and u can translate with this bot
this could be useful for people who make public bots and it can be used for a better user interface
"""
import fortnitepy
import os
from translate import Translator

os.system('cls||clear')

client = fortnitepy.Client(
  auth=fortnitepy.AuthorizationCodeAuth(
    code=input('Enter authorization code: ')
  )
)

@client.event
async def event_ready():
  while True:
    os.system('cls||clear')
    i = input("What Would You Like To Translate: ")
    translator= Translator(to_lang=client.user.preferred_language)
    translation = translator.translate(i)
    print(f"Output: {translation}")
    input('\nPress Enter To Go Again')  
    
client.run()
