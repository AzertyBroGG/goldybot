import discord, random
from discord.ext import commands, bridge

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

        
    @commands.command()
    async def coin(self, ctx: commands.Context):
        rand = random.randrange(0,2)
        if rand == 0:
            coin = "Орёл"
            file = "assets/coin1.jpg"
        else:
            coin = "Решка"
            file = "assets/coin2.jpg"
        await ctx.send(embed = discord.Embed(title = f"Я подбросил монетку и получил: {coin}"))
        await ctx.send(file = discord.File(file))
        
    @commands.command()
    async def user(self, ctx: commands.Context):
        background = Editor("wlcbg.jpg")
        profile_image = load_image(str(ctx.author.avatar.url))
        profile = Editor(profile_image).resize((150, 150)).circle_image()

        poppins = Font.poppins(size=50, variant="bold")
        poppins_small = Font.poppins(size=25, variant="regular")
        poppins_light = Font.poppins(size=20, variant="light")

        background.paste(profile, (325, 90))
        background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)
        background.text((400, 260), "WELCOME", color="white", font=poppins, align="center")
        background.text(
    (400, 325), ctx.author.name, color="white", font=poppins_small, align="center"
)
        background.text(
    (400, 360),
    "You are the Member",
    color="#0BE7F5",
    font=poppins_small,
    align="center",
)
        await ctx.send(file = discord.File(fp=background.image_bytes, filename = 'user.png'))
        
def setup(bot):
    bot.add_cog(Fun(bot))
