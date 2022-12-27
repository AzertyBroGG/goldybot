import platform
import socket, translate
import discord 
from enum import Enum
import pretty_errors
from typing import List
import asyncio
import datetime
import requests, json
from os import path
import os 
import logging
from discord.ext import commands, bridge
pretty_errors.activate()
from config import prefix, intents, token
#Многоооо Импортов!

trans = translate.Translator(to_lang = "ru")
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
