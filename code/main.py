import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
import asyncio
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#파이어베이스

from discord.ext import tasks
from itertools import cycle
#빙빙 돌아가는

from command.user.join import *
from command.user.secession import *
from command.user.information import *
from command.move import *
from help import help
from command.nicknamechange import *
from command.invent import *

cred = credentials.Certificate('database.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'rink'
})


@tasks.loop(seconds=3)    # n초마다 다음 메시지 출력
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

bot = commands.Bot(command_prefix=['?'], intents=discord.Intents.all())
bot = ComponentsBot(command_prefix = "?")
slash = SlashCommand(bot, sync_commands=True)
status = cycle(["슬래시커맨드 지원!", "접두사 : ?", f"TEAM PLAY"])


@bot.event
async def on_ready():
  print('로딩완료')
  change_status.start()



@bot.command()
async def 도움말(ctx):
  await help(ctx, bot)
@slash.slash(name="도움말", description = "도움말을 확인합니다.", guild_ids=[958012815090786324])
async def 가입(ctx: SlashContext):
  await help(ctx, bot)


  
@bot.command(aliases=['ㄱㅇ'])
async def 가입(ctx):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await join(ctx, bot)
    return None
  await ctx.reply('가입이 되어 있습니다!')
@slash.slash(name="가입", description = "가입을 진행합니다", guild_ids=[958012815090786324])
async def 가입(ctx: SlashContext):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await sjoin(ctx, bot)
    return None
  await ctx.send('가입이 되어 있습니다!')
#####################가입#####################

@bot.command()
async def 탈퇴(ctx):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await secession(ctx)
@slash.slash(name="탈퇴", description = "탈퇴를 진행합니다", guild_ids=[958012815090786324])
async def 탈퇴(ctx: SlashContext):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await ssecession(ctx)
  #####################탈퇴#####################


@bot.command(aliases=['ㅈㅂ'])
async def 정보(ctx):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await information(ctx, bot)
@slash.slash(name="정보", description = "사용자의 정보를 봅니다", guild_ids=[958012815090786324])
async def 정보(ctx: SlashContext):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await sinformation(ctx, bot)
  #####################정보#####################

@bot.command(aliases=['ㅇㄷ'])
async def 이동(ctx):
  
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await move(ctx, bot)
#####################이동#####################

@bot.command(aliases=['ㅇㅂ'])
async def 인벤토리(ctx):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await invent(ctx, bot)
@slash.slash(name="인벤토리", description = "자신의 보유 아이템들을 확인합니다.", guild_ids=[958012815090786324])
async def 인벤토리(ctx: SlashContext):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await invent(ctx, bot)


@bot.command(aliases=['변경'], pass_context=True)
async def 닉네임변경(ctx, name=None):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  
  await nicknamechange(ctx, name)
@slash.slash(name="닉네임변경", description = "사용자의 닉네임을 변경합니다.", guild_ids=[958012815090786324])
async def 정보(ctx: SlashContext, name):
  dir = db.reference(f'user')
  a = dir.get()
  b = ctx.author.id
  if b not in a:
    await ctx.reply('가입이 되어 있지 않습니다!')
    return None
  await nicknamechange(ctx, name)
  #####################정보#####################
bot.run("token")
