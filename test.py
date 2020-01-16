import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('jungsanfile-e5ae2dbc8879.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM/edit#gid=0')

sheet3 = doc.worksheet('재고주문')


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
    
    if message.content.startswith('!주문'):
        if message.channel.is_private and message.author.id != "667338660420780032":
            await client.send_message(discord.utils.get(client.get_all_members(), id="315237238940106754"), message.author.name + "(" + message.author.id + ") : " + message.content[4:] + " 주문이 접수되었습니다.")
            await client.send_message(message.channel, '\n주문이 정상적으로 접수되었습니다. \n부득이한경우 개인답변 드리겠습니다.')
            
    if message.content.startswith('!주문'):
        if message.channel.is_private and message.author.id != "667338660420780032":
            sheet3.insert_row([message.author.display_name, message.content[4:]], 3)
            await client.send_message(client.get_channel("667343258296254464"), message.author.display_name + "(" + message.author.id + ") : " + message.content[4:])
           
            
    if message.content.startswith('!답변'):
            member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
            await client.send_message(member, "홍팀장 개인답변 : " + message.content[23:])
            
            
    if message.content == '!명령어':
        command_list = ''
        command_list += '!모델명\n'     #!모델명
        command_list += '!재고 [모델명]\n'     #!재고+모델명
        command_list += '!재고 [구단위]\n'     #!재고+구단위
        command_list += '!퀵비 [동단위/동단위]\n'     #!퀵비
        command_list += '!동판 [동판신규]\n'     #!동판
        command_list += '!동판 [동판기변]\n'     #!동판
        command_list += '!동판 [소호신규]\n'     #!동판
        command_list += '!동판 [소호기변]\n'     #!동판
        command_list += '!동판 [후결합]\n'     #!동판
        command_list += '!동판 [재약정기존]\n'     #!동판
        command_list += '!동판 [재약정전환]\n'     #!동판
        command_list += '!동판 [재약정단독기존]\n'     #!동판
        command_list += '!동판 [재약정단독전환]\n'     #!동판
        command_list += '!동판 [단독]\n'     #!동판
        embed = discord.Embed(
            title = ":keyboard: 명령어",
            description= '```' + command_list + '```',
            color=0xff00ff
            )
        embed.add_field(
            name=":radio: 기타채널 명령어 ",
            value= '```!주문 [주문넣을 단말기및 요청글] 채널:재고신청봇 개인메시지 \n!단가 [모델명 요금제군 유형] 채널:무선정책조회\n!외국인단가 [모델명 요금제군 유형] 채널:외국인정책조회\n```'
            )
        await client.send_message(message.channel, embed=embed)

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
