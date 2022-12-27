
import discord
from discord.ext import commands
from config import *
import json, aiohttp, random
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
animal = 'https://some-random-api.ml/img/'

from translate import Translator
from asyncio import sleep
translator= Translator(to_lang="ru")

class Panel(discord.ui.View):
    def __init__(self, bot, *args, **kwargs):
      self.bot = bot
      super().__init__(*args, **kwargs)
      
    @discord.ui.button(label = 'botinfo', style = discord.ButtonStyle.primary)
    async def botinfo(self, button, interaction):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldybot.gq \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner_id}> \nБот создан: \n{self.bot.user.created_at} \nВ боте обновления каждый день!")
        await interaction.response.send_message(embed = embed, ephemeral = True)
        
    @discord.ui.button(label='role', style = discord.ButtonStyle.primary)
    async def role(self, button, interaction):
        role = discord.utils.get(interaction.guild.roles,name=interaction.user.name) 
        if role not in interaction.guild.roles:
            await interaction.guild.create_role(name = interaction.user.name)
        role = discord.utils.get(interaction.guild.roles, name = interaction.user.name)
        await role.edit(colour=discord.Color.random())
        await interaction.user.add_roles(role) 
        await interaction.response.send_message("Вам выдана персональная роль на 5 минут", ephemeral = True)
        await sleep(300)
        await interaction.user.remove_roles(role)
        await role.delete()
        
    @discord.ui.button(label='random', style = discord.ButtonStyle.primary)
    async def random(self, button, interaction):
        await interaction.response.send_message(f'Случайное число от 0 до 1000: \n{random.randint(0,1001)}', ephemeral = True)
        
    @discord.ui.button(label='joke', style = discord.ButtonStyle.primary)
    async def joke(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
                async with cs.get(joke) as r:
                    if r.status == 200:
                        js = await r.json()
                        joke_t = translator.translate(js['joke'])
                        await interaction.response.send_message(joke_t, ephemeral = True)
                     
   @discord.ui.button(label='coin', style = discord.ButtonStyle.primary)
    async def coin(self, button, interaction):
        rand = random.randrange(0,2)
        if rand == 0:
            coin = "Орёл"
            file = "assets/coin1.jpg"
        else:
            coin = "Решка"
            file = "assets/coin2.jpg"
        file = discord.File(file)
        embed = discord.Embed(title = f"Я подбросил монетку и получил: {coin}")
        await interaction.response.send_message(embed = embed)
        await interaction.response.send_message(file = file)
        
    @discord.ui.button(label='cat', style = discord.ButtonStyle.primary)
    async def cat(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'cat') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])
    
    @discord.ui.button(label='dog', style = discord.ButtonStyle.primary)
    async def dog(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'dog') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])
                    
    @discord.ui.button(label='pikachu', style = discord.ButtonStyle.primary)
    async def pikachu(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'pikachu') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])
                    
    @discord.ui.button(label='koala', style = discord.ButtonStyle.primary)
    async def koala(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'koala') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])
                    
    @discord.ui.button(label='fox', style = discord.ButtonStyle.primary)
    async def fox(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'fox') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])
                    
    @discord.ui.button(label='panda', style = discord.ButtonStyle.primary)
    async def panda(self, button, interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'panda') as r:
                if r.status == 200:
                    js = await r.json()
                    await interaction.response.send_message(js['link'])