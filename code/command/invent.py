import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

async def invent(ctx, bot):
  dir = db.reference(f"{ctx.author.id}")
  users = dir.get()
  money = users['돈']
  name = users['닉네임']
  change = users['변경권']
  slime = users['인벤토리']['슬라임점액']
  tree = users['인벤토리']['나무장작']
  hy = users['인벤토리']['허니비의_꿀']
  rslime = users['인벤토리']['레어']['<R>슬라임의_정수']
  rtree = users['인벤토리']['레어']['<R>질좋은_나무장작']
  rhy = users['인벤토리']['레어']['<R>아미 와스프의 꿀']

  slimemoji = bot.get_emoji(960058702235316264)
  remoji = bot.get_emoji(960453811112132628)
  coin = bot.get_emoji(960455133060300882)
  common = bot.get_emoji(960458374389055498)
  t = bot.get_emoji(960460411621240833)
  
  embed = discord.Embed(title=f"{name} Invent(인벤토리)", description="", color=0xE4E4E4)
  embed.add_field(name="‎‎", value=f"**{coin} 코인\n{money}원**‎‎‎", inline=False)
  embed.add_field(name="‎‎", value=f"**일반아이템**‎‎‎", inline=False)
  embed.add_field(name=f"슬라임점액", value=f"{slime}개‎‎", inline=True)
  embed.add_field(name=f"나무장작", value=f"‎‎{tree}개", inline=True)
  embed.add_field(name=f"허니비의_꿀", value=f"‎‎{hy}개", inline=True)
  embed.add_field(name="‎‎", value=f"{remoji}**레어아이템**‎‎‎", inline=False)
  embed.add_field(name=f"슬라임의_정수", value=f"{rslime}개‎‎", inline=True)
  embed.add_field(name=f"질좋은_나무장작", value=f"‎‎{rtree}개", inline=True)
  embed.add_field(name=f"아미 와스프의 꿀", value=f"‎‎{rhy}개", inline=True)
  embed.add_field(name="‎‎", value=f"{t}**특수아이템**‎‎‎", inline=False)
  embed.add_field(name=f"이름변경권", value=f"{change}개‎‎", inline=True)

  await ctx.send(embed=embed)


  
  