import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import asyncio
#기본 import

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


async def join(ctx, bot):
  user = {
    "닉네임" : ctx.author.name,
    "레벨" : 0,
    "경험치" : 0,
    "최대경험치" : 100,
    "ing" : 0,
    "위치" : "이라키",
    "칭호" : "없음",
    "변경권" : 0,
    "인벤토리" : {
      "슬라임점액" : 0,
      "나무장작" : 0,
      "허니비의_꿀" : 0,
      "레어" : {
        "<R>슬라임의_정수" : 0,
        "<R>질좋은_나무장작" : 0,
        "<R>아미 와스프의 꿀" : 0
      }
    },
    "돈" : 0,
    "스탯" : {
      "체력" : 100,
      "공격력" : 10,
      "회피율" : 0,
      "추가공격력" : 0
    },
    "스킬" : {
      'D스킬' : ['없음'],
      "T스킬" : ['없음'],
      "장착스킬" : {
        '스킬1' : '없음',
        '스킬2' : '없음',
        '스킬3' : '없음'
      }
    },
    '팀' : {
      '1' : '없음',
      '2' : '없음',
      '연결상태' : 'X'
    }    
  }
  dir = db.reference(f'{ctx.author.id}')
  dir.update(user)
  dir = db.reference('user')
  lists = dir.get()
  new = [ctx.author.id]
  dir = db.reference()
  dir.update({'user' : lists + new})

  loding = bot.get_emoji(958668652180287508)
  msg = await ctx.reply(f'> 가입을 진행중입니다....\n‎\n{loding} | 유저의 정보를 불러옵니다...')
  await asyncio.sleep(1.5)
  await msg.edit(content = f'> 가입을 진행중입니다....\n‎\n{loding} | 유저의 정보를 저장중입니다.')
  await asyncio.sleep(1.5)
  await msg.edit(content = f'> 가입을 진행중입니다....\n‎\n{loding} | 리소스를 불러옵니다...')
  await asyncio.sleep(1.0)
  await msg.delete()
  await ctx.reply('가입이 완료되었습니다!')
  

async def sjoin(ctx, bot):
  user = {
    "닉네임" : ctx.author.name,
    "레벨" : 0,
    "경험치" : 0,
    "최대경험치" : 100,
    "ing" : 0,
    "위치" : "이라키",
    "칭호" : "없음",
    "변경권" : 0,
    "돈" : 0,
    "인벤토리" : {
      "슬라임점액" : 0,
      "나무장작" : 0,
      "허니비의_꿀" : 0,
      "레어" : {
        "<R>슬라임의_정수" : 0,
        "<R>질좋은_나무장작" : 0,
        "<R>아미 와스프의 꿀" : 0
      }
    },
    "스탯" : {
      "체력" : 100,
      "공격력" : 10,
      "회피율" : 0,
      "추가공격력" : 0
    },
    "스킬" : {
      'D스킬' : ['없음'],
      "T스킬" : ['없음'],
      "장착스킬" : {
        '스킬1' : '없음',
        '스킬2' : '없음',
        '스킬3' : '없음'
      }
    },
    '팀' : {
      '1' : '없음',
      '2' : '없음',
      '연결상태' : 'X'
    }    
  }
  dir = db.reference(f'{ctx.author.id}')
  dir.update(user)
  dir = db.reference('user')
  lists = dir.get()
  new = [ctx.author.id]
  dir = db.reference()
  dir.update({'user' : lists + new})
  loding = bot.get_emoji(958668652180287508)  
  msg = await ctx.send(f'> 가입을 진행중입니다....\n‎\n{loding} | 유저의 정보를 불러옵니다...')
  await asyncio.sleep(1.5)
  await msg.edit(content = f'> 가입을 진행중입니다....\n‎\n{loding} | 유저의 정보를 저장중입니다.')
  await asyncio.sleep(1.5)
  await msg.edit(content = f'> 가입을 진행중입니다....\n‎\n{loding} | 리소스를 불러옵니다...')
  await asyncio.sleep(1.0)
  await msg.delete()
  await ctx.send(f'{ctx.author.mention} 가입이 완료되었습니다!')
  