import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

async def information(ctx, bot):
  dir = db.reference(f'{ctx.author.id}')
  stats = dir.get()
  

  hpemo = bot.get_emoji(959387486105251870)
  atemo = bot.get_emoji(959387180474724372)
  patts = bot.get_emoji(959388855490969600)  
  Evasionratemo = bot.get_emoji(959390133960990730)
  name = stats['닉네임']
  money = stats['돈']
  칭호 = stats['칭호']
  LV = stats['레벨']
  EXP = stats['경험치']
  MAXEXP = stats['최대경험치']
  local = stats['위치']
  dskill = stats['스킬']['D스킬']
  lens = len(dskill)
  if lens > 1:
    del dskill[0]
  tskill = stats['스킬']['T스킬']
  lens = len(tskill)
  if lens > 1:
    del tskill[0]
  ski1 = stats['스킬']['장착스킬']['스킬1']
  ski2 = stats['스킬']['장착스킬']['스킬2']
  ski3 = stats['스킬']['장착스킬']['스킬3']
  att = stats['스탯']['공격력']
  hp = stats['스탯']['체력']
  patt = stats['스탯']['추가공격력']
  Evasionrate = stats['스탯']['회피율']

  embed = discord.Embed(title= name + " Stats(정보)", description="", color=0xE4E4E4)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="‎", value="‎‎‎**칭호**", inline=False)
  embed.add_field(name=f"[{칭호}]", value="‎", inline=False)
  embed.add_field(name="‎‎‎Your LV", value=f"{LV} LV\n{EXP}/{MAXEXP} exp\n‎", inline=False)

  embed.add_field(name="현재위치", value=f"{local}", inline=False)
  embed.add_field(name="‎", value="‎‎‎**Your state(스탯)**", inline=False)
  embed.add_field(name=f"{hpemo}체력ㅤㅤㅤ{patts}추가피해", value=f'{hp} HPㅤㅤㅤ +‎{patt}', inline=False)
  embed.add_field(name=f"{atemo}공격력ㅤㅤ{Evasionratemo}회피율", value=f"{att}ㅤㅤㅤㅤㅤㅤ{Evasionrate}%\n‎", inline=False)


  embed.add_field(name="‎", value="‎‎‎**Activation SKILL**", inline=False)
  embed.add_field(name="SKILL1‎", value='<' + ski1 + '>', inline=False)
  embed.add_field(name="SKILL2", value='<' + ski2 + '>', inline=False)
  embed.add_field(name="SKILL3", value='<' + ski3 + '>', inline=False)
  embed.add_field(name="‎", value="‎‎‎**T SKILL**", inline=False)
  embed.add_field(name=tskill, value="‎", inline=False)
  embed.add_field(name="‎", value="‎‎‎**D SKILL**", inline=False)
  embed.add_field(name=dskill, value="‎", inline=False)



  await ctx.reply(embed=embed)


async def sinformation(ctx, bot):
  dir = db.reference(f'{ctx.author.id}')
  stats = dir.get()
  

  hpemo = bot.get_emoji(959387486105251870)
  atemo = bot.get_emoji(959387180474724372)
  patts = bot.get_emoji(959388855490969600)  
  Evasionratemo = bot.get_emoji(959390133960990730)
  name = stats['닉네임']
  money = stats['돈']
  칭호 = stats['칭호']
  LV = stats['레벨']
  EXP = stats['경험치']
  MAXEXP = stats['최대경험치']
  local = stats['위치']
  dskill = stats['스킬']['D스킬']
  lens = len(dskill)
  if lens > 1:
    del dskill[0]
  tskill = stats['스킬']['T스킬']
  lens = len(tskill)
  if lens > 1:
    del tskill[0]
  ski1 = stats['스킬']['장착스킬']['스킬1']
  ski2 = stats['스킬']['장착스킬']['스킬2']
  ski3 = stats['스킬']['장착스킬']['스킬3']
  att = stats['스탯']['공격력']
  hp = stats['스탯']['체력']
  patt = stats['스탯']['추가공격력']
  Evasionrate = stats['스탯']['회피율']

  embed = discord.Embed(title= name + " Stats(정보)", description="", color=0xE4E4E4)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="‎", value="‎‎‎**칭호**", inline=False)
  embed.add_field(name=f"[{칭호}]", value="‎", inline=False)
  embed.add_field(name="‎‎‎Your LV", value=f"{LV} LV\n{EXP}/{MAXEXP} exp\n‎", inline=False)

  embed.add_field(name="현재위치", value=f"{local}", inline=False)
  embed.add_field(name="‎", value="‎‎‎**Your state(스탯)**", inline=False)
  embed.add_field(name=f"{hpemo}체력ㅤㅤㅤ{patts}추가피해", value=f'{hp} HPㅤㅤㅤ +‎{patt}', inline=False)
  embed.add_field(name=f"{atemo}공격력ㅤㅤ{Evasionratemo}회피율", value=f"{att}ㅤㅤㅤㅤㅤㅤ{Evasionrate}%\n‎", inline=False)


  embed.add_field(name="‎", value="‎‎‎**Activation SKILL**", inline=False)
  embed.add_field(name="SKILL1‎", value='<' + ski1 + '>', inline=False)
  embed.add_field(name="SKILL2", value='<' + ski2 + '>', inline=False)
  embed.add_field(name="SKILL3", value='<' + ski3 + '>', inline=False)
  embed.add_field(name="‎", value="‎‎‎**T SKILL**", inline=False)
  embed.add_field(name=tskill, value="‎", inline=False)
  embed.add_field(name="‎", value="‎‎‎**D SKILL**", inline=False)
  embed.add_field(name=dskill, value="‎", inline=False)



  await ctx.send(embed=embed)