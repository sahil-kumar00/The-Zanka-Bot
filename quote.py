import discord
import os
import requests
import json

intents = discord.Intents.default()
intents.messages = True  # Enable message related intents

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/quote'):  
        quote = get_quote()
        await message.channel.send(quote)

# Hardcoded token (not recommended)
client.run("MTIyNTg1Njc4NjM2MDE3NjcyMg.G88ugS.RSqHI33K2Oapm1762Bhajo_blOSf3oQKwfWMcg")