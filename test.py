import discord
import asyncio
import random
import os
import datetime
from time import sleep
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
async def on_member_join(member):
    sleep(1)	
    fmt = '{1.name} 에 오신것을 환영합니다.\n{0.mention} 님!! \n매장이름/직급/성함/연락처 이렇게 남겨주시면 \n확인후 권한을 승인해드리겠습니다. '
    channel = member.server.get_channel("661832869521391646")
    return await client.send_message(channel, fmt.format(member, member.server))




@client.event
async def on_message(message):
    global gc #정산
    global creds #정산
    

    if message.content.startswith('!그레이드'):
        gc = gspread.authorize(creds)
        wks = gc.open('오전재고').worksheet('그레이드')
        result = wks.acell('B1').value
        embed1 = discord.Embed(
            title = ' 파트너 그레이드 안내!! ',
            description= '**```css\n' + result + ' ```**',
            color=0x7fffd4
            )
        embed2 = discord.Embed(
            title = ' 파트너 그레이드 조회!! ',
            description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
            color=0x00ffff
            )
        await client.send_message(client.get_channel("674827771817623572"), embed=embed2)	
        await client.send_message(message.channel, embed=embed1)


    if message.content.startswith('!주문'):
        
        curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
        krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
        gc = gspread.authorize(creds)
        wks = gc.open('오전재고').worksheet('재고주문')
        wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
        embed1 = discord.Embed(
            title = message.author.display_name + "님 의 주문 ",
            description= '```fix\n' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed1.add_field(
            name=" 주문접수 확인... ",
            value= '```diff\n!주문내용이 전달되어 정상적으로\n!접수되었습니다. 부득이한경우\n!개인답변 드리겠습니다.```'
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
        neyongdabtotal = message.content[23:]
        neyongdab = neyongdabtotal.split("/")
        neyong = neyongdab[0]
        dab = neyongdab[1]
	
        embed = discord.Embed(
            title = "주문내용",
            description= '```fix\n' + neyong + '```',
            color=0xFF0000
            )
        embed.add_field(
            name = message.author.display_name + "님 답변",
            value= '```Tex\n' + '$' + dab + '```'
	    )
        await client.send_message(member, embed=embed)
	
	
	
    if message.content.startswith('!공지'):
         if message.author.id == '315237238940106754' :
             embed = discord.Embed(    
                 title = "📌 공지사항",
                 description= '```' + message.content[4:] + '```',
                 color=0xFF0000	
                 )
             await client.send_message(client.get_channel("667707237623660569"), embed=embed)
             await client.send_message(client.get_channel("667239441307533312"), embed=embed)
             await client.send_message(client.get_channel("667241204739604490"), embed=embed)
             await client.send_message(client.get_channel("667241430070198273"), embed=embed)
             await client.send_message(client.get_channel("667241481907470336"), embed=embed)
             await client.send_message(client.get_channel("667241531694120970"), embed=embed)
             await client.send_message(client.get_channel("667241582411513856"), embed=embed)
             await client.send_message(client.get_channel("667241378534653983"), embed=embed)
             await client.send_message(client.get_channel("667240616207450122"), embed=embed)
             await client.send_message(client.get_channel("667242915378102293"), embed=embed)
             await client.send_message(client.get_channel("667243361614168088"), embed=embed)
             await client.send_message(client.get_channel("667243407227224064"), embed=embed)
             await client.send_message(client.get_channel("667243524433117218"), embed=embed)
             await client.send_message(client.get_channel("667247020926435344"), embed=embed)
             await client.send_message(client.get_channel("667243630989410304"), embed=embed)
             await client.send_message(client.get_channel("667243696915218432"), embed=embed)
             await client.send_message(client.get_channel("667243782604849155"), embed=embed)
             await client.send_message(client.get_channel("667243837206429696"), embed=embed)
             await client.send_message(client.get_channel("667244790404087808"), embed=embed)
             await client.send_message(client.get_channel("667244947677904898"), embed=embed)
             await client.send_message(client.get_channel("667245023359664142"), embed=embed)
             await client.send_message(client.get_channel("667245114619592765"), embed=embed)
             await client.send_message(client.get_channel("667245155790618625"), embed=embed)
             await client.send_message(client.get_channel("667245231447474176"), embed=embed)
             await client.send_message(client.get_channel("667245522549211138"), embed=embed)
             await client.send_message(client.get_channel("667245576014004256"), embed=embed)
             await client.send_message(client.get_channel("667245650802507777"), embed=embed)
             await client.send_message(client.get_channel("667245748907147275"), embed=embed)
             await client.send_message(client.get_channel("667245819786690560"), embed=embed)
             await client.send_message(client.get_channel("667245916947742760"), embed=embed)
             await client.send_message(client.get_channel("667246076453191690"), embed=embed)
             await client.send_message(client.get_channel("667246146074443807"), embed=embed)
             await client.send_message(client.get_channel("667246234851082240"), embed=embed)
             await client.send_message(client.get_channel("667246316652593163"), embed=embed)
             await client.send_message(client.get_channel("667246366468079626"), embed=embed)
             await client.send_message(client.get_channel("667246430074699777"), embed=embed)
             await client.send_message(client.get_channel("667246487872339968"), embed=embed)
             await client.send_message(client.get_channel("667246552238129153"), embed=embed)
             await client.send_message(client.get_channel("667246600019771472"), embed=embed)
             await client.send_message(client.get_channel("667246718198218772"), embed=embed)
             await client.send_message(client.get_channel("667246834892144640"), embed=embed)
             await client.send_message(client.get_channel("667247069580492820"), embed=embed)
             await client.send_message(client.get_channel("667247107232628736"), embed=embed)
             await client.send_message(client.get_channel("667247142833881108"), embed=embed)
             await client.send_message(client.get_channel("667247180188483584"), embed=embed)
             await client.send_message(client.get_channel("667247225847545866"), embed=embed)
             await client.send_message(client.get_channel("667247261734141962"), embed=embed)
             await client.send_message(client.get_channel("667247287679975446"), embed=embed)
             await client.send_message(client.get_channel("667247313525407755"), embed=embed)
             await client.send_message(client.get_channel("667247368902672404"), embed=embed)
             await client.send_message(client.get_channel("667247397075681299"), embed=embed)
             await client.send_message(client.get_channel("667247433041838100"), embed=embed)
             await client.send_message(client.get_channel("667247472908828676"), embed=embed)
             await client.send_message(client.get_channel("667247519264407552"), embed=embed)
             await client.send_message(client.get_channel("667247545893781524"), embed=embed)

 
                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
