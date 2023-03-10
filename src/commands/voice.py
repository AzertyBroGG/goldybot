import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands, bridge
from gtts import gTTS
import os
from asyncio import sleep
from os.path import exists
from pathlib import Path
import speech_recognition as sr
import youtube_dl

r = sr.Recognizer()
connections = {}

youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # Bind to ipv4 since ipv6 addresses cause issues at certain times
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source: discord.AudioSource, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if "entries" in data:
            # Takes the first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
    
    
    
    
    
    
    
    
    
class Voice(Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def say(self, ctx: commands.Context, *, text1):   
      tts = gTTS(text = text1, lang = 'ru')
      tts.save('text.mp3')
      voice_channel = ctx.author.voice.channel
      channel = None
      if voice_channel != None:
          channel = voice_channel.name
      if ctx.voice_client is None:
            vc = await voice_channel.connect()
      else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client 
         
      audio = discord.FFmpegPCMAudio(source='text.mp3')
      vc.play(audio)
      while vc.is_playing():
          await sleep(.1)
      
      await ctx.send('??????????')
  
  
            
  @commands.command()
  async def play(self, ctx: commands.Context, *, url: str):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f"Player error: {e}") if e else None)

        await ctx.send(f"Now playing: {player.title}")
def setup(bot):
  bot.add_cog(Voice(bot))
