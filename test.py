import discord
import asyncio
import random
import os
import datetime
import time
import arrow
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
        
        curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
        krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
        gc = gspread.authorize(creds)
        wks = gc.open('오전재고').worksheet('재고주문')
        wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
        embed1 = discord.Embed(
            title = message.author.display_name + "님 의 주문 ",
            description= '```' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed1.add_field(
            name=" 주문접수 확인... ",
            value= '```주문내용이 전달되어 정상적으로\n접수되었습니다. 부득이한경우\n개인답변 드리겠습니다.```'
            )
        embed2 = discord.Embed(
            title = message.author.display_name + "님 의 주문내용 ",
            description= '```' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed2.add_field(
            name=" 주문 접수처... ",
            value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
            )
        await client.send_message(message.channel, embed=embed1)
        await client.send_message(client.get_channel("667343258296254464"), embed=embed2)
            
	
    if message.content.startswith('!답변'):
        member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
        embed = discord.Embed(
            title = message.author.display_name + "님 답변",
            description= '```' + message.content[23:] + '```',
            color=0xFF0000
            )
        await client.send_message(member, embed=embed)
	
	
	
    if message.content.startswith('!공지'):
        members = discord.utils.get(client.get_all_channels(), id="667707237623660569", id="667239441307533312", id="667241204739604490", id="667241430070198273", id="667241481907470336", id="667241531694120970", id="667241582411513856", id="667241378534653983", id="667240616207450122", id="667242915378102293", id="667243361614168088", id="667243407227224064", id="667243524433117218", id="667247020926435344", id="667243630989410304", id="667243696915218432", id="667243782604849155", id="667243837206429696", id="667244790404087808", id="667244947677904898", id="667245023359664142", id="667245114619592765", id="667245155790618625", id="667245231447474176", id="667245522549211138", id="667245576014004256", id="667245650802507777", id="667245748907147275", id="667245819786690560", id="667245916947742760", id="667246076453191690", id="667246146074443807", id="667246234851082240", id="667246316652593163", id="667246366468079626", id="667246430074699777", id="667246487872339968", id="667246552238129153", id="667246600019771472", id="667246718198218772", id="667246834892144640", id="667247069580492820", id="667247107232628736", id="667247142833881108", id="667247180188483584", id="667247225847545866", id="667247261734141962", id="667247287679975446", id="667247313525407755", id="667247368902672404", id="667247397075681299", id="667247433041838100", id="667247472908828676", id="667247519264407552", id="667247545893781524")
        embed = discord.Embed(    
            title = "📌 공지사항",
            description= '```' + message.content[4:] + '```',
            color=0xFF0000	
            )
        await client.send_message(members, embed=embed)
		
		
		
    if message.content == '!정책표':
        command_list = ''
        command_list += 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTmWzJs5QX3i2Q5LaOugdA7NoxLZ3O_fQZAyYMejopSp0u-nuoe9iaQREswxmanQSbXs1Swm_ukKaJ7/pubhtml'     #!링크
        embed = discord.Embed(
            title = ":bar_chart: 정책표링크",
            description= command_list,
            color=0xf29886
            )
        await client.send_message(client.get_channel("672022974223876096"), message.author.display_name + "(" + message.author.id + message.channel.name + ") : 정책표출력!! " + message.content[4:])
        await client.send_message(message.channel, embed=embed)

 
                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
