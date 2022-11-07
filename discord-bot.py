import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("테스트를 진행"))

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(embed = discord.Embed(title = '따라하기', description = text, color = 0x00ff00))

bot.run('your token')
