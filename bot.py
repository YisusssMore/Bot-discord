import discord
import random
import time
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$lanza_una_moneda'):
        lanzar = random.choice(["Cara","Cruz"])
        await message.channel.send(f"La moneda a caido en: {lanzar}")
    else:
        await message.channel.send(message.content)

client.run("MTM5ODA0ODEzNTI4ODQ1NTI4OQ.GjnOZ-.ZFwwlJ64hRmGJycvxce3urQ3cW7JOBSI3qfOYQ")