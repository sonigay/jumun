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
    await client.change_presence(game=discord.Game(name='주문재고 전달', type=1))




@client.event
async def on_message(message):
    global gc #정산
    global creds	#정산
    
    if message.content.startswith('!주문'):
        if message.channel.is_private and message.author.id != "667338660420780032":
            await client.send_message(discord.utils.get(client.get_all_members(), id="315237238940106754"), message.author.name + "(" + message.author.id + ") : " + message.content[4:] + " 주문이 접수되었습니다.")
            await client.send_message(message.channel, '\n주문이 정상적으로 접수되었습니다. \n부득이한경우 개인답변 드리겠습니다.')
            
    if message.content.startswith('!주문'):
		if message.channel.is_private and message.author.id != "667338660420780032":
            gc = gspread.authorize(creds)
            wks = gc.open('오전재고').worksheet('재고주문')
            wks.insert_row([message.author.display_name, message.content[4:]], 3)
            await client.send_message(client.get_channel("667343258296254464"), message.author.display_name + "(" + message.author.id + ") : " + message.content[4:])
           
            
    if message.content.startswith('!답변'):
            member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
            await client.send_message(member, "홍팀장 개인답변 : " + message.content[23:])
            
            
    if message.content == '!정책표':
	command_list = ''
	command_list += 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTmWzJs5QX3i2Q5LaOugdA7NoxLZ3O_fQZAyYMejopSp0u-nuoe9iaQREswxmanQSbXs1Swm_ukKaJ7/pubhtml#\n'     #!모델명
	embed = discord.Embed(
		title = ":bar_chart: 정책표링크",
		description= '```' + command_list + '```',
		color=0xFFD5B4
		)
	await client.send_message(client.get_channel("672022974223876096"), message.author.display_name + "(" + message.author.id + ") : " + message.content[4:], embed=embed)
            
 

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
