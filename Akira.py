import os
import random
import discord
from discord.ext import commands

# from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

TOKEN = ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
GUILD = ('Yosuga no Sora')

bot = commands.Bot(command_prefix='!')

client = discord.Client(intents=intents)

welcome = ["Welcome!",
         "Welcome <:AkiraHappy2:598913220085940244>",
         "<a:AkiraWelcome:642665323064983582>",
         "<:AkiraWave:660947544796299324>",
         "Enjoy your stay <:AkiraWink2:657053283009036320>",
         "Welcome! <a:AkiraShishou:642665322708729862>",
         "<:AkiraShishouGun:644894915175776256>",
         "<a:Waterhose:644904614998704128>",
         "<a:Shishou:642665322884890625>"]

motoka = 800821327648391168
akira = 1000295303439732796
sora = 768265134027440128
bots = [motoka, akira, sora]

help = """**These are a list of my commands** <:AkiraSmile2:598830891820777483>\n
1. Hello Akira or Hi Akira
2. I love you Akira.
3. Do a prayer Akira
4. Akira?
5. Sing for us, Akira!
6. Good morning Akira or GM Akira
7. Good night Akira or GN Akira
8. Shishou
9. Amatsume!
10. Squeeze!
11. Nyome
12. Welcome!
13. Akira stop
14. Kazuha
15. Ryouhei or <:RyouheiEhehe:617064221745872927> or <:RyouheiPose:852673404284567584>
16. Cream bread
17. Akira do your homework
18. What's your favourite restaurant Akira?
19. Akira spray **@user**
20. Akira kill **@user**
21. <:KazuhaHappy:616717915483275345>
22. <:AkiraShishouGun:644894915175776256>
23. <:CatShishou:617066832213311675> or <:CatShishou2:617067951543025677>"""


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    await client.change_presence(activity=discord.Game(name="Akira's route"))

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    # """Runs whenever a new member joins the server"""
    channel = client.get_channel(595525657971392562)
    last = await channel.fetch_message(channel.last_message_id)
    if last.author.id == motoka:
        await channel.send(member.mention + random.choice(welcome))



@client.event
async def on_message(message):
    try:
        admin = discord.utils.get(message.channel.guild.roles, name="Admin")
        botdev = discord.utils.get(message.channel.guild.roles, name="Bot Dev")
        mod = discord.utils.get(message.channel.guild.roles, name="Mods")

        offtopic = message.guild.get_channel(620723472988897281)
    except:
        pass

    if message.author.id == akira:
        return
    if message.content.lower() == "welcome!":
        await message.channel.send("<a:AkiraWelcome:642665323064983582>")

    if message.content.lower() == "kazuha":
        await message.channel.send("Onee-chan!")

    if message.content.lower() in ["hello akira", "hi akira"]:
        await message.channel.send(random.choice(["<:AkiraWave:660947544796299324>", "Yahoo! <:AkiraWink:615085666081964042>"]))

    if message.content.lower() == "i love you akira":
        await message.channel.send("I love you too. <:AkiraBlush:605477383910326273>")

    if message.content.lower() == "akira?":
        await message.channel.send(random.choice(["Yees? <:AkiraBlush:605477383910326273>", "Yahoo! I'm here! <:AkiraWink:615085666081964042>"]))

    if message.content.lower() == "do a prayer akira":
        await message.channel.send("\"Sayori-hime-sama, Haru-kun is back...\" <:AkiraBlush3:852672066607775834>")

    if message.content.lower() == "sing for us, akira!":
        await message.channel.send("ラッパラッパ、みんなが笑顔 美味しい ニッコニコ！ <:AkiraSerious:616724140291915973>")

    if message.content.lower() in ["good morning akira", "gm akira"]:
        await message.channel.send("Ohayou! <:AkiraHappy:852672068766924820>")

    if message.content.lower() in ["good night akira", "gn akira"]:
        await message.channel.send(random.choice(["<:AkiraSleepy:656438236565995521>", "<:AkiraSleepy:605658630838288395>", "Oyasumi"]))

    if message.content.lower() == "amatsume!":
        await message.channel.send("Hai! <:AkiraWink2:657053283009036320>")

    if message.content.lower() == "uwu":
        await message.channel.send("<:AkiraUwu:605476491937185823>")

    if message.content.lower() == "nyome":
        await message.channel.send("<:AkiraShy:852672067085795348>")

    if message.content.lower() == "cream bread":
        await message.channel.send("Where? <:AkiraWhat:605665009317576705>")

    if message.content.lower() == "akira do your homework":
        await message.channel.send("<:AkiraSad:607813699826352128> Can I copy yours?")

    if message.content.lower() == "what's your favourite restaurant akira?":
        await message.channel.send("Rappa Sushi! <:AkiraSmile2:598830891820777483>")

    if message.content.lower() == "stupid bots":
        await message.add_reaction("<:AkiraPout:605477436393783327>")

    if "<:catshishou:617066832213311675>" in message.content.lower() or "<:catshishou2:617067951543025677>" in message.content.lower():
        await message.add_reaction("<:AkiraSmile2:598830891820777483")

    if message.content.lower() == "<:akirashishougun:644894915175776256>":
        await message.channel.send("<:akirashishougun:644894915175776256>")

    if message.content.lower() in ["<:ryouheiehehe:617064221745872927>", "<:ryouheipose:852673404284567584>", "ryouhei"]:
        await message.add_reaction("<:AkiraWave:660947544796299324>")
        await message.add_reaction("<:AkiraWink:615085666081964042>")

    if message.content.lower() == "<:kazuhahappy:616717915483275345>":
        await message.add_reaction("<AkiraKazuhaKiss:661411557489508352>")

    if message.content.lower() == "akira help":
        await message.author.send(help)

    if "akira kill" in message.content.lower():
        responses = [
            "<:AkiraShishouGun:644894915175776256>",
            "May Sayorihime-sama forgive you <:AkiraShishouGun:644894915175776256>",
            "Yahoo! <:Dagger:853058515248873473>",
            "<:AkiraHappy2:598913220085940244> <:Dagger:853058515248873473>",
            "<a:Waterhose:644904614998704128>",
        ]
        meslist = message.content.split(" ")
        if meslist[1] == "kill" and len(meslist) == 3:
            mentions = meslist[-1]
            if "@" in mentions:
                await message.channel.send(mentions + random.choice(responses))


    if message.content.lower() == "akira, reset" and botdev in message.author.roles:
        await message.channel.send("Resetting")
        exit()

    if message.content == "Akira, send a message to edit" and botdev in message.author.roles:
        await message.channel.send("message")

    if message.content.lower() == "shishou":
        await message.add_reaction("<:AkiraUwU:605476491937185823>")
        await message.add_reaction("<:CatShishou2:617067951543025677")

    if message.content.lower() == "squeeze!":
        await message.channel.send("<:AkiraUwU:605476491937185823>")

    if message.content.lower() == "akira stop":
        await message.add_reaction("<:AkiraEhehe:615083705073139722>")

    if "akira spray" in message.content.lower():
        if "@" in message.content.split()[-1]:
            await message.channel.send("<a:Waterhose:644904614998704128>")

    if message.content.lower() == "hashire sori yo kaze no you ni tsukimihara wo":
        await message.add_reaction("<:AkiraPadoru:703452369551098098>")
        await message.channel.send("***PADORU PADORU!***")


client.run(TOKEN)