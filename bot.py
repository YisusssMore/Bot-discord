import discord
import random
import os
from dotenv import load_dotenv
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

load_dotenv("C:/Users/USER/OneDrive/Desktop/Proyectos Python/Bot_discord/DiscordToken.env")
TOKEN = os.getenv("DISCORD_TOKEN")

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
    elif message.content.startswith('$crear_contraseña'):
        gen_pass(12)
        password = gen_pass(12)
        await message.channel.send(f"La contraseña es la siguiente: {password}")
    else:
        await message.channel.send(message.content)

client.run(TOKEN)


