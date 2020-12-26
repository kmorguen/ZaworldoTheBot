import discord
import os
import requests
import json
import random


client = discord.Client()

ban_words =  ["fuck", "bitch", "salope", "pute", "merde"]

ban_words_response = ["votre phrase contient un ou des mots NSFW", "veuillez surveuiller votre langage svp", "votre message contient un ou des mots NSFW ce qui est passible de bannissement"]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$bitch'):
        await message.channel.send('Pas de gros mot svp')

    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    
    if any(word in msg for word in ban_words):
      await message.channel.send(random.choice(ban_words_response))

token = os.environ.get("DISCORD_BOT_SECRET") 
client.run(token)
