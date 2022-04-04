import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



async def help(ctx, bot):
  slash = bot.get_emoji(959486919971070023)
  f = bot.get_emoji(959669424430940180)
  embed = discord.Embed(title="너구리 UNITED", description=f"", color=0x2f3136)
  embed.add_field(name=f"‎", value="**기본도움말**", inline=False)
  embed.add_field(name=f"{slash}도움말", value="봇의 사용법을 확인합니다.", inline=False)
  embed.add_field(name=f"{slash}가입", value="서비스를 이용하기 위해 가입을 진행합니다.", inline=False)
  embed.add_field(name=f"{slash}탈퇴", value="탈퇴를 진행합니다.", inline=False)

  embed.add_field(name=f"‎", value="**게임도움말**", inline=False)
  embed.add_field(name=f"{slash}정보", value="사용자의 레벨, 위치, 스킬등을 확인합니다", inline=False)
  embed.add_field(name=f"{slash}인벤토리", value="자신의 인벤을 확인합니다.", inline=False)
  embed.add_field(name=f"{slash}변경", value="자신의 닉네임을 확인합니다.", inline=False)
  embed.add_field(name=f"{f}이동", value="장소를 이동합니다.", inline=False)
  embed.set_footer(text=f"접두사 : ? | 슬래시 명령어 지원")
  await ctx.send(embed=embed)