from bs4 import BeautifulSoup
import discord, urllib.request

token = "your_token"
client = discord.Client()

# bot's setting
@client.event
async def on_ready():
    print(client.user.name)
    print("!!Program is started!!")
    game = discord.Game("안녕하세요? 민파고입니다.")
    await client.change_presence(status=discord.Status.online, activity=game)


# message interaction
@client.event
async def on_message(message):
    ### bot introducer
    # help 
    if message.content == "!help":
        embed = discord.Embed(title="!!HElP!!", color=0xFF2D00)
        embed.set_footer(text="**!command**")
        await message.channel.send(embed=embed)

    # introduce commands
    if message.content == "!command":
        embed = discord.Embed(title="!!Command!!", color=0xFF2D00)
        embed.add_field(name="1. !who are you 2. !sites 3. !when 4. !weather", value="⚠️caution⚠️ plz use '!'", inline=True)
        embed.set_footer(text="Request --> kar7mp5")
        embed.set_thumbnail(url="https://chojiautoclub.tommy1005a.repl.co/photo%20groups/hina.jpg")
        await message.channel.send(embed=embed)
    ###

    # school club site introduce
    if message.content == "!who are you":
        embed = discord.Embed(title="!!My name is '민파고'!!", color=0xFF2D00)
        embed = embed.add_field(name="!!만들어진 목적!!", value="동아리원에게 맨날 주소 알려주기 귀찮아서 만듦", inline=True)
        embed.set_thumbnail(url="https://chojiautoclub.tommy1005a.repl.co/photo%20groups/hina.jpg")
        await message.channel.send(embed=embed)

    if message.content == "!sites":
        embed = discord.Embed(title="!!Adresses!!", color=0xFF2D00)
        embed.add_field(name="This is chojiclub's adress", value="https://chojiautoclub.tommy1005a.repl.co/", inline=True)
        embed.add_field(name="!!Replit adress!!", value="https://replit.com/", inline=True)
        embed.add_field(name="!!Arduino adress!!", value="https://www.arduino.cc/", inline=True)
        embed.add_field(name="!!Python adress!!", value="https://www.python.org/", inline=True)
        embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/99C94E495C81F1AA0F")
        await message.channel.send(embed=embed)

    if message.content == "!when":
        embed = discord.Embed(title="!!동아리 활동 시간!!", color=0xFF2D00)
        embed.add_field(name="매주(전면등교시)", value="화요일, 수요일(바뀔 수 있음)", inline=True)
        embed.set_footer(text="***⚠️자주 결석하면 동아리 활동에서 제외될 수 있음⚠️***")
        embed.set_thumbnail(url="https://image.fmkorea.com/files/attach/new/20180401/44021718/278909402/1000600949/1c8be5ddc71f92b7f875b55f0bf8b27d.jpeg")
        await message.channel.send(embed=embed)

 
    # weather forecast
    if message.content =="!weather":
        webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%95%88%EC%82%B0%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=h72j%2FdprvOsssAJiJ9dssssst64-240195')
        soup = BeautifulSoup(webpage, 'html.parser')
        cast = soup.find('p',"summary")
        temps = soup.find('dl',"summary_list")
        # pound = soup.find('div', 'detail_box')
        embed = discord.Embed(title="!!Today forecast!!", color=0xFF2D00)
        embed.add_field(name="!!Ansan's weather!!", value=str(cast.get_text())+str(temps.get_text()), inline=True)
        # embed.set_footer(text=str(pound.get_text()))
        embed.set_thumbnail(url="https://www.weather.go.kr/wgis-nuri/images/opengraph.png")
        await message.channel.send(embed=embed)
    

    ### memes
    # stop!!
    if message.content == "멈춰" or message.content == "멈춰!" or message.content == "멈춰!!":
        await message.channel.send("https://tenor.com/view/%EB%A9%88%EC%B6%B0-stop-gif-21048386")
    ###

client.run(token)
