import discord
from discord.ext import commands
from config import *
import json, aiohttp, random
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
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