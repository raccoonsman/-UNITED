import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

async def move(ctx, bot):
  dir = db.reference(f'{ctx.author.id}')
  stats = dir.get()
  ing = stats['ing']
  local = stats['위치']
  if ing != 0:
    await ctx.reply(f'이동이 불가합니다!\n사유 : {ing}중')
    return None

  dir.update({'ing' : '이동'})
  town = bot.get_emoji(959399077995499550)
  battle = bot.get_emoji(959398828858028032)
  harbor = bot.get_emoji(959398696821329942)
  X = bot.get_emoji(943780055761440779)



  time = 8  
  def check(m):
    return m.author == ctx.author
  msg = await ctx.send(
        f"**현재위치 : {local}**\n>>> {town} 마을 : 상점, 아카데미\n{harbor} 항구 : 다른 대륙으로 이동가능\n{battle} 던전 : 전투를 통해 보상과 경험치를 획득합니다.",
        components = [
            Select(
                placeholder = "이동할 장소를 골라주세요!",
                options = [
                    SelectOption(emoji = town, label = "이라키", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = battle, label = "초보자던전", value = f"{ctx.author.id}B"),
                    SelectOption(emoji = harbor, label = "로스항구", value = f"{ctx.author.id}C"),
                    SelectOption(emoji = X, label = "이동취소", value = f"{ctx.author.id}N"),
                ]
            )
        ]
    )

  interaction = await bot.wait_for("select_option", check=check)

  await msg.delete()
  users = interaction.values[0]
  if users == f"{ctx.author.id}A":
    if local == '이라키':
      await ctx.reply('현재 `이라키`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.reply(f'`{local}`에서 `이라키`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.reply('`이라키`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '이라키'})

  if users == f"{ctx.author.id}B":
    if local == '초보자던전':
      await ctx.reply('현재 `초보자던전`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.reply(f'`{local}`에서 `초보자던전`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.reply('`초보자던전`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '초보자던전'})

  if users == f"{ctx.author.id}C":
    if local == '로스항구':
      await ctx.reply('현재 `로스항구`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.reply(f'`{local}`에서 `로스항구`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.reply('`로스항구`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '로스항구'})

  if users == f"{ctx.author.id}N":
    await ctx.reply('이동취소')
    dir.update({'ing' : 0})











async def smove(ctx, bot):
  dir = db.reference(f'{ctx.author.id}')
  stats = dir.get()
  ing = stats['ing']
  local = stats['위치']
  if ing != 0:
    await ctx.send(f'이동이 불가합니다!\n사유 : {ing}중')
    return None

  dir.update({'ing' : '이동'})
  town = bot.get_emoji(959399077995499550)
  battle = bot.get_emoji(959398828858028032)
  harbor = bot.get_emoji(959398696821329942)
  X = bot.get_emoji(943780055761440779)



  time = 8  
  def check(m):
    return m.author == ctx.author
  msg = await ctx.send(
        f"**현재위치 : {local}**\n>>> {town} 마을 : 상점, 아카데미\n{harbor} 항구 : 다른 대륙으로 이동가능\n{battle} 던전 : 전투를 통해 보상과 경험치를 획득합니다.",
        components = [
            Select(
                placeholder = "이동할 장소를 골라주세요!",
                options = [
                    SelectOption(emoji = town, label = "이라키", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = battle, label = "초보자던전", value = f"{ctx.author.id}B"),
                    SelectOption(emoji = harbor, label = "로스항구", value = f"{ctx.author.id}C"),
                    SelectOption(emoji = X, label = "이동취소", value = f"{ctx.author.id}N"),
                ]
            )
        ]
    )

  interaction = await bot.wait_for("select_option", check=check)

  await msg.delete()
  users = interaction.values[0]
  if users == f"{ctx.author.id}A":
    if local == '이라키':
      await ctx.send('현재 `이라키`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.send(f'`{local}`에서 `이라키`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.send('`이라키`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '이라키'})

  if users == f"{ctx.author.id}B":
    if local == '초보자던전':
      await ctx.send('현재 `초보자던전`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.send(f'`{local}`에서 `초보자던전`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.send('`초보자던전`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '초보자던전'})

  if users == f"{ctx.author.id}C":
    if local == '로스항구':
      await ctx.send('현재 `로스항구`에 계십니다.')
      dir.update({'ing' : 0})
      return None
    msg = await ctx.send(f'`{local}`에서 `로스항구`로 이동합니다...\n> 이동시간 : {time}초')
    await asyncio.sleep(time)
    await msg.delete()
    await ctx.send('`로스항구`에 도착하였습니다!')
    dir.update({'ing' : 0})
    dir.update({'위치' : '로스항구'})

  if users == f"{ctx.author.id}N":
    await ctx.send('이동취소')
    dir.update({'ing' : 0})