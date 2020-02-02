import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jumun-8151173be58f.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM')
sheet1 = doc.worksheet('재고주문')
client = discord.Client()
@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='메세지 전달', type=1))
@client.event
async def on_message(message):
    global gc #정산
    global creds #정산
    
   
    if message.content.startswith('!주문'):
        gc = gspread.authorize(creds)
        wks = gc.open('오전재고').worksheet('재고주문')
        wks.insert_row([message.author.display_name, message.content[4:]], 3)
        embed1 = discord.Embed(
            title = message.author.name + " 님의 주문 ",
            description= '```' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed1.add_field(
            name=" 주문접수 확인... ",
            value= '```주문내용이 전달되어 정상적으로\n접수되었습니다. 부득이한경우\n개인답변 드리겠습니다.```'
            )
        embed2 = discord.Embed(
            title = message.author.display_name + " 님의 주문 ",
            description= '```' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed2.add_field(
            name=" 주문요청... ",
            value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
            )
        await client.send_message(message.channel, embed=embed1)
        await client.send_message(client.get_channel("667343258296254464"), embed=embed2)
        await client.send_message(client.get_channel("667343258296254464"), message.author.display_name + "(" + message.channel.name + message.channel.id + ") : " + message.content[4:] + " 주문요청!! ")
            
	
    if message.content.startswith('!답변'):
        member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
        embed = discord.Embed(
            title = "홍팀장 재고주문 답변",
            description= '```' + message.content[23:] + '```',
            color=0xFF0000
            )
        await client.send_message(member, embed=embed)
            
            
		
    if message.content == '!정책표':
        command_list = ''
        command_list += 'http://bit.ly/cellphone_price'     #!링크
        embed = discord.Embed(
            title = ":bar_chart: 정책표링크",
            description= command_list,
            color=0xf29886
            )
        await client.send_message(client.get_channel("672022974223876096"), message.author.display_name + "(" + message.author.id + message.channel.name + ") : 정책표출력!! " + message.content[4:])
        await client.send_message(message.channel, embed=embed)

 
                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
