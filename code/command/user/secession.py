import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

async def secession(ctx):
  await ctx.reply('탈퇴가 성공적으로 진행이 되었습니다!\n> 불편한 사항은? `.문의`')
  dir = db.reference(f'{ctx.author.id}')
  dir.delete()  
  dir = db.reference(f'user')
  a = dir.get()
  a.remove(ctx.author.id)
  dir = db.reference()
  dir.update({'user' : a})

async def ssecession(ctx):
  await ctx.send(f'{ctx.author.mention} 탈퇴가 성공적으로 진행이 되었습니다!\n> 불편한 사항은? `.문의`')
  dir = db.reference(f'{ctx.author.id}')
  dir.delete()  
  dir = db.reference(f'user')
  a = dir.get()
  a.remove(ctx.author.id)
  dir = db.reference()
  dir.update({'user' : a})
  