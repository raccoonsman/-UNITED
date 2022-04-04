import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



async def nicknamechange(ctx, name):
  if 'None' in str(type(name)):
    await ctx.reply('`?변경 [이름]`입니다.')
    return None

  dir = db.reference(f'{ctx.author.id}')
  users = dir.get()
  oldname = users['닉네임']
  ticket = users['변경권']
  if ticket < 1:
    await ctx.reply(f'닉네임변경권 갯수가 부족합니다.\n> 닉네임변경권 : {ticket}개')
    return None
  if oldname == name:
    await ctx.reply('변경할려는 닉네임이 현재 닉네임이랑 같습니다.')
    return None
  ticket = ticket - 1
  dir.update({'변경권' : ticket})
  dir.update({'닉네임' : name})
  await ctx.reply(f'닉네임이 변경되었습니다\n> `{oldname}` → `{name}`')