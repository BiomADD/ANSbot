import discord 
import os
import requests
#import json
#import urllib.parse

#May not need to inport this since .env is deprecated
#from dotenv import load_dotenv

#assigns DISCORD bot key
my_secret = os.environ['TOKEN']

#Creates discord client
client = discord.Client()

#Returns a quote from the API
def total_players_online():
  url = 'https://celestiusrvr.com/.netlify/functions/status'
  json_data = requests.get(url).json()
  totalPlayers = json_data['totalPlayers']
  return totalPlayers

def midgard_players_online():
  url = 'https://celestiusrvr.com/.netlify/functions/status'
  json_data = requests.get(url).json()
  midgardPlayers = json_data['midgardPlayers']
  return midgardPlayers

def hibernia_players_online():
  url = 'https://celestiusrvr.com/.netlify/functions/status'
  json_data = requests.get(url).json()
  hiberniaPlayers = json_data['hiberniaPlayers']
  return hiberniaPlayers

def albion_players_online():
  url = 'https://celestiusrvr.com/.netlify/functions/status'
  json_data = requests.get(url).json()
  albionPlayers = json_data['albionPlayers']
  return albionPlayers


  
#handles discord event
@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #Checks whether message comes from bot and if so it ends function call
  if message.author == client.user:
    return
  #If message not from bot, continue with function.
  
  if message.content.startswith('!players'):
    players = total_players_online()
    await message.channel.send("Total number of players online: " + str(players))
  
  if message.content.startswith('!hib'):
    hib_players = hibernia_players_online()
    await message.channel.send("Total number of hibs online: " + str(hib_players))
  
  if message.content.startswith('!mid'):
    mid_players = midgard_players_online()
    await message.channel.send("Total number of mids online: " + str(mid_players))

  if message.content.startswith('!alb'):
    alb_players = albion_players_online()
    await message.channel.send("Total number of albs online: " + str(alb_players))


#Bot run after grabbing token
client.run(os.getenv('TOKEN'))

