
import platform
print("Запуск...") 
print("="*10, "О системе: ", "="*10)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
###
import discord #Создание Клиента
from discord.ext import commands, bridge
 #Команды
from enum import Enum
import pretty_errors
from typing import List
import asyncio
import datetime
import requests, json
from os import path
import os #Тоже генераторы
import logging
pretty_errors.activate()
from config import prefix, intents, token

def load_exts(bot):
    for filename in os.listdir("./commands"):
         if filename.endswith(".py") and not filename.startswith('view'):
            bot.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./events"):
         if filename.endswith(".py"):
            bot.load_extension(f"events.{filename[:-3]}")
    for filename in os.listdir("./ecogoldy"):
         if filename.endswith(".py"):
            bot.load_extension(f"ecogoldy.{filename[:-3]}")
            
class GoldyBot(bridge.Bot):
    def __init__(self):
        super().__init__(command_prefix = prefix, 
                         intents = intents, 
                         case_insensitive = True, 
                         help_command = None,
                         owner_id = 969853884535283742)
    async def on_ready(self):
        await self.wait_until_ready()	
        print('Клиент готов!')
        await self.user.edit(username = 'GoldyBot')
    async def on_command_completion(self, ctx):
        try:
          await ctx.message.add_reaction('✅')
        except:
          pass
    async def on_command_error(self, ctx, error):
        try:
          await ctx.message.add_reaction('❎')
        except:
          pass
bot = GoldyBot()
load_exts(bot)

#Создание бота
### ?
#Логи discord
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='pycord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(name)s: %(message)s'))
logger.addHandler(handler)

#

bot.run(token)


