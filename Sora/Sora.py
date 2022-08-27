import os
import random
import discord
from discord.ext import commands
#from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

meid = 407747014806208523

TOKEN = ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
GUILD = ('Yosuga no Sora')

bot = commands.Bot(command_prefix='!')

client = discord.Client(intents=intents)

welcome = [
    " is here <:SoraEheheh:609373578575740948>",
    " Welcome <:SoraBunny:644895104343080980>",
    " <a:SoraSplashed:657109137406165025>",
    " <:SoraHuggy:609368621692485633>",
    " Enjoy the server. We have memes.",
    " Welcome <:SoraHappy:595869879588880393>",
    " Enjoy your stay.",
    " has joined <:SoraHappy:595869879588880393>",
    " <a:SoraDisgust:642730713178701825>",
    " Oh no. Another one. <:SoraUegh:598833101698891777>",
    " <a:SoraSlap:644371223572119554>",
    " Oh no. Another one. <:SoraMendo:598857944334991371>"
]

motoka = 800821327648391168
akira = 1000295303439732796
sora = 768265134027440128
bots = [motoka, akira, sora]
editthisone = 0

divlst = 877749728547315733

smitelst = []

flagdict = {"🇺🇸": "America", "🇧🇷": "Brazil", "🇨🇦": "Canada", "🇬🇧": "UK", "🇵🇭": "Philippines", "🇻🇳": "Vietnam", "🇵🇱": "Poland",
            "🇷🇺": "Russia", "🇩🇪": "Germany", "🇮🇩": "Indonesia", "🇦🇺": "Australia", "🇫🇷": "France", "🇮🇳": "India", "🇦🇷": "Argentina",
            "🇨🇳": "China", "🇲🇾": "Malaysia", "🇸🇬": "Singapore", "🇮🇹": "Italy", "🇫🇮": "Finland", "🇹🇷": "Turkey", "🇳🇱": "Netherlands",
            "🇪🇸": "Spain", "🇹🇭": "Thailand", "🇯🇵": "Japan", "🇨🇱": "Chile", "🇨🇿": "Czechia", "🇨🇴": "Colombia", "🇳🇿": "New Zealand",
            "🇵🇹": "Portugal", "🇵🇪": "Peru", "🇺🇦": "Ukraine", "🇭🇺": "Hungary", "🇰🇷": "South Korea", "🇧🇩": "Bangladesh", "🇸🇪": "Sweden",
            "🇸🇦": "Saudi Arabia", "🇷🇴": "Romania", "🇮🇪": "Ireland", "🇦🇹": "Austria", "🇩🇰": "Denmark", "🇨🇭": "Switzerland",
            "🇭🇷": "Croatia", "🇱🇻": "Latvia", "🇮🇱": "Israel", "🇦🇪": "UAE", "🇻🇪": "Venezuela", "🇮🇷": "Iran", "🇪🇪": "Estonia",
            "🇧🇪": "Belgium", "🇳🇴": "Norway", "🇷🇸": "Serbia", "🇧🇬": "Bulgaria", "🇵🇰": "Pakistan", "🇲🇳": "Mongolia", "🇪🇬": "Egypt",
            "🇪🇨": "Ecuador", "🇴🇲": "Oman", "🇵🇸": "Palestine", "🇿🇦": "South Africa", "🇰🇿": "Kazakhstan", "🇩🇿": "Algeria",
            "🇱🇹": "Lithuania", "🇰🇬": "Kyrgyzstan", "🇧🇾": "Belarus", "🇳🇵": "Nepal", "🇹🇹": "Trinidad and Tobago", "🇱🇺": "Luxembourg",
            "🇱🇰": "Sri Lanka", "🇦🇱": "Albania", "🇸🇮": "Slovenia", "🇬🇹": "Guatemala", "🇵🇾": "Paraguay", "🇲🇪": "Montenegro",
            "🇮🇸": "Iceland", "🇯🇲": "Jamaica", "🇸🇩": "Sudan", "🇧🇿": "Belize", "🇨🇺": "Cuba", "🇯🇴": "Jordan", "🇺🇾": "Uruguay",
            "🇳🇬": "Nigeria", "🇸🇾": "Syria", "🇸🇰": "Slovakia", "🇮🇶": "Iraq", "🇲🇲": "Myanmar", "🇶🇦": "Qatar", "🇲🇻": "Maldives",
            "🇹🇼": "Taiwan", "🇿🇼": "Zimbabwe", "🇦🇿": "Azerbaijan", "🇬🇪": "Georgia", "🇦🇫": "Afghanistan", "🇲🇦": "Morocco",
            "🇬🇩": "Grenada", "🇨🇷": "Costa Rica", "🇧🇦": "Bosnia and Herzegovina", "🇦🇩": "Andorra", "🇦🇴": "Angola",
            "🇦🇬": "Antigua and Barbuda", "🇦🇲": "Armenia", "🇧🇸": "Bahamas", "🇧🇭": "Bahrain", "🇧🇧": "Barbados", "🇧🇯": "Benin",
            "🇧🇹": "Bhutan", "🇧🇴": "Bolivia", "🇧🇼": "Botswana", "🇧🇳": "Brunei", "🇧🇫": "Burkina Faso", "🇧🇮": "Burundi",
            "🇰🇭": "Cambodia", "🇨🇲": "Cameroon", "🇨🇻": "Cape Verde", "🇨🇫": "Central African Republic", "🇹🇩": "Chad",
            "🇰🇲": "Comoros", "🇨🇩": "Democratic Republic of the Congo", "🇨🇮": "Cote d'Ivoire", "🇨🇾": "Cyprus",
            "🇩🇯": "Djibouti", "🇩🇲": "Dominica", "🇩🇴": "Dominican Republic", "🇹🇱": "East Timor", "🇸🇻": "El Salvador",
            "🇬🇶": "Equatorial Guinea", "🇪🇷": "Eritrea", "🇪🇹": "Ethiopia", "🇫🇯": "Fiji", "🇵🇫": "French Polynesia",
            "🇬🇦": "Gabon", "🇬🇲": "The Gambia", "🇬🇭": "Ghana", "🇬🇮": "Gibraltar", "🇬🇷": "Greece", "🇬🇱": "Greenland",
            "🇬🇵": "Guadeloupe", "🇬🇳": "Guinea", "🇬🇼": "Guinea-Bissau", "🇬🇾": "Guyana", "🇭🇹": "Haiti", "🇭🇳": "Honduras",
            "🇭🇰": "Hong Kong", "🇰🇪": "Kenya", "🇰🇮": "Kiribati", "🇰🇵": "North Korea", "🇰🇼": "Kuwait", "🇱🇦": "Laos",
            "🇱🇧": "Lebanon", "🇱🇸": "Lesotho", "🇱🇷": "Liberia", "🇱🇾": "Libya", "🇱🇮": "Liechtenstein", "🇲🇴": "Macau",
            "🇲🇰": "Macedonia", "🇲🇬": "Madagascar", "🇲🇼": "Malawi", "🇲🇱": "Mali", "🇲🇹": "Malta", "🇲🇭": "Marshall Islands",
            "🇲🇶": "Martinique", "🇲🇷": "Mauritania", "🇲🇺": "Mauritius", "🇲🇽": "Mexico", "🇫🇲": "Micronesia", "🇲🇩": "Moldova",
            "🇲🇨": "Monaco", "🇲🇿": "Mozambique", "🇳🇦": "Namibia", "🇳🇷": "Nauru", "🇳🇨": "New Caledonia", "🇳🇮": "Nicaragua",
            "🇳🇪": "Niger", "🇲🇵": "Northern Mariana Islands", "🇵🇼": "Palau", "🇵🇦": "Panama", "🇵🇬": "Papua New Guinea",
            "🇵🇷": "Puerto Rico", "🇷🇪": "Réunion", "🇷🇼": "Rwanda", "🇰🇳": "Saint Kitts and Nevis", "🇱🇨": "Saint Lucia",
            "🇼🇸": "Samoa", "🇸🇲": "San Marino", "🇸🇹": "Sao Tome and Princ.", "🇸🇳": "Senegal", "🇸🇨": "Seychelles", "🇸🇱": "Sierra Leone",
            "🇸🇧": "Solomon Islands", "🇸🇴": "Somalia", "🇻🇨": "St. Vincent and Gren.", "🇸🇷": "Suriname", "🇸🇿": "Swaziland",
            "🇹🇯": "Tajikistan", "🇹🇿": "Tanzania", "🇹🇬": "Togo", "🇹🇴": "Tonga", "🇹🇳": "Tunisia", "🇹🇲": "Turkmenistan",
            "🇹🇻": "Tuvalu", "🇺🇬": "Uganda", "🇺🇿": "Uzbekistan", "🇻🇺": "Vanuatu", "🇻🇦": "Vatican City",
            "🇻🇬": "British Virgin Islands", "🇻🇮": "US Virgin Islands", "🇪🇭": "Western Sahara", "🇾🇪": "Yemen", "🇿🇲": "Zambia"}

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    await client.change_presence(activity=discord.Game(name="Sora's route"))

    try:
        f = open("smite.txt", "r")
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            smitelst.append(int(lines[i]))
    except:
        pass

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    #"""Runs whenever a new member joins the server"""
    channel = client.get_channel(595525657971392562)
    last = await channel.fetch_message(channel.last_message_id)
    if last.author.id == akira:
        await channel.send(member.mention + random.choice(welcome))

@client.event
async def on_message(message):

    if message.author.id in smitelst:
        await message.delete()
    try:
        admin = discord.utils.get(message.channel.guild.roles, name="Admin")
        botdev = discord.utils.get(message.channel.guild.roles, name="Bot Dev")
        mod = discord.utils.get(message.channel.guild.roles, name="Mods")
    except:
        pass

    naoreact = "<a:SoraDisgust:642730713178701825>"

    if "nao" in message.content.lower() and message.content != "<:NaoYeyy:609375678579867658>" and message.content != "<:NaoSmile:598913197168132117>" and message.content != "<:NaoLUL:609342186684940288>" and message.content != "<:NaoBlush:852672067693576202>" and message.content != "<:NaoFlustered:852672068574117908>":
        react = naoreact
        await message.add_reaction(react)

    if message.author == client.user:
        return
    hello = "...Hi"
    morning = "...Good morning"
    night = "...Goodnight"
    love = [
        "I don't love you. <:SoraUegh:598833101698891777>",
        "I only love Haru! <:SoraAngry:609367953003118593>"
        ]
    prayer = [
        "...Baka",
        "I pray my internet connection improves...",
        "I pray these idiots leave me alone...",
        "バカ…",
        "このバカがほっておくように祈る。"
        ]
    question = [
        "...What? <:SoraMendo:598857944334991371>",
        "Nani?",
        "<:SoraWhat:595878621202087936>"
        ]
    waifu = "Don't talk about me like that!"
    howareyou = [
        "I'm hungry. I wonder when Haru will make dinner...",
        "I miss Haru...",
        "<:SoraHappy:595869879588880393>",
        "<:SoraSleepy2:657111076076257290>"
        ]
    chores = "...No <:SoraMendo:598857944334991371>"
    harusponse = "<:SoraHappy2:683311267871850567>"
    wincest = "Says who?"
    daisuki = "私はハルしか愛してない。<:SoraAngry:609367953003118593>"
    cute = [
        "...",
        "...Stop <:SoraEh2:598863930458243082>",
        "Dont say that <:SoraBlush2:598833027019440128>"
        ]
    bye = "Finally..."
    stupidbots = "<:SoraMendo:598857944334991371>"
    naosponse = "<:SoraAngry:609367953003118593>"
    waifureact = [
        "<a:SoraDisgust:642730713178701825>",
        "<:SoraBlush2:598833027019440128>"
        ]
    naoreact = [
        "<a:SoraDisgust:642730713178701825>",
        "<:SoraAngry:609367953003118593>"
    ]
    ehehehgrin = [
        "<:SoraEheheh:609373578575740948>",
        "<:SoraEvilGrin:652655851340955674>"
        ]
    cat = "<:SoraHappy:595869879588880393>"
    ryouheieyes = "<:SoraUegh:598833101698891777>"
    kozueeh = "<:SoraEvilGrin:652655851340955674>"
    cutereact = "<:SoraGlare:666305669711921177>"
    killsora = [
        "<:SoraMendo:598857944334991371> No",
        "*Jumps into Lake Hakone* <:SoraCry:609368553442902017>"
    ]
    help = """**Here are a list of my commands** <:SoraHappy2:683311267871850567>

1. Sora hug **@user**
2. Sora slap **@user**
3. Sora kill **@user**
4. Sora roast **@user**
5. Ping **@user**
6. Hi/Hello/Hai/Haii/Haiii Sora
7. Good morning/GM Sora
8. Good night/Goodnight/GN Sora
9. Goodbye
10. I love Sora
11. I love you Sora
12. Do a prayer
13. Stupid Bots
14. Nao
15. How are you Sora?
16. Incest is Wrong
17. Sora?
18. Sora is best waifu
19. Sora do some chores
20. Haru
21. Sora daisuki
22. Sora give cookies
23. Sora you are cute
24. Omae Wa Mou Shindeiru
25. Hello there
26. Splash splash
27. Sora do you love Haru?
28. :curry: 
29. <:KozueEh:657441676452954133> 
30. <:SoraAngry:609367953003118593> <:Dagger:853058515248873473>
31. <:HarukaEhehe:609322762330308618> 
32. <:RyouheiEyes:631841754370539560>
33. <:SoraEvilGrin:652655851340955674> / <:SoraEheheh:609373578575740948>
34. <:catshishou2:617067951543025677> / <:catshishou:617066832213311675>
35. <:NaoYeyy:609375678579867658> / <:NaoSmile:598913197168132117> / <:NaoLUL:609342186684940288>
36. **@Sora**"""

    if "sora, smite " in message.content.lower() and message.author.id == meid:
        f = open("smite.txt", "a")
        smote = message.mentions[0].id
        smitelst.append(smote)
        f.write(smote)
        f.close()

    if "sora, unsmite" in message.content.lower() and message.author.id == meid:
        smote = message.mentions[0].id
        if smote in smitelst:
            smitelst.remove(smote)
        f = open("smite.txt", "w")
        for id in smitelst:
            f.write(str(id) + "\n")
        f.close()

    
    if message.content.lower() == "hi sora" or message.content.lower() == "hello sora" or message.content.lower() == "hai sora" or message.content.lower() == "haii sora" or message.content.lower() == "haiii sora":
        name = message.author.name
        response = hello + " " + name
        await message.channel.send(response)
    
    if message.content.lower() == "good morning sora" or message.content.lower() == "morning sora" or message.content.lower() == "gm sora":
        response = morning + " " + message.author.name
        await message.channel.send(response)
    
    if message.content.lower() == "good night sora" or message.content.lower() == "goodnight sora" or message.content.lower() == "gn sora":
        response = night + " " + message.author.name
        await message.channel.send(response)
        
    if message.content.lower() == "i love sora":
        response = love[0]
        await message.channel.send(response)

    if message.content.lower() == "i love you sora":
        response = love[1]
        await message.channel.send(response)
        
    if message.content.lower() == "do a prayer":
        response = random.choice(prayer)
        await message.channel.send(response)
    
    if message.content.lower() == "sora?":
        response = random.choice(question)
        await message.channel.send(response)
    
    if message.content.lower() == "sora is best waifu":
        react = random.choice(waifureact)
        response = waifu
        await message.add_reaction(react)
        await message.channel.send(response)
    
    if message.content.lower() == "how are you sora?":
        response = random.choice(howareyou)
        await message.channel.send(response)
    
    if message.content.lower() == "sora do some chores":
        response = chores
        await message.channel.send(response)
    
    if message.content == "<:HarukaEhehe:609322762330308618>":
        react = harusponse
        await message.add_reaction(react)
    
    if message.content.lower() == "incest is wrong":
        response = wincest
        await message.channel.send(response)
    
    if message.content.lower() == "sora daisuki":
        response = daisuki
        await message.channel.send(response)
    
    if message.content.lower() == "sora you are cute":
        x = random.randint(1, 2)
        if x == 1:
            response = random.choice(cute)
            await message.channel.send(response)
    
    if message.content.lower() == "goodbye":
        response = bye
        await message.channel.send(response)
    
    if message.content.lower() == "stupid bots":
        react = stupidbots
        await message.add_reaction(react)
    
    if message.content == "<:NaoYeyy:609375678579867658>" or message.content == "<:NaoSmile:598913197168132117>" or message.content == "<:NaoLUL:609342186684940288>" or message.content == "<:NaoBlush:852672067693576202>" or message.content == "<:NaoFlustered:852672068574117908>":

        react2 = naoreact[1]

        await message.add_reaction(react2)
    
    if message.content == "<:SoraEvilGrin:652655851340955674>" or message.content == "<:SoraEheheh:609373578575740948>":
        react = random.choice(ehehehgrin)
        await message.add_reaction(react)
    
    if message.content == "<:CatShishou:617066832213311675>" or message.content == "<:CatShishou2:617067951543025677>":
        react = cat
        await message.add_reaction(react)
    
    if message.content == "<:RyouheiEyes:631841754370539560>":
        react = ryouheieyes
        await message.add_reaction(react)
    
    if message.content == "<:KozueEh:657441676452954133>":
        react = kozueeh
        await message.add_reaction(react)

    if "sora please hug" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[2] == "hug" and len(meslist) == 4:
            mentions = meslist[-1]
            if "@" in mentions:
                await message.delete()
                await message.channel.send(mentions + "<:SoraHuggy:609368621692485633>")

    if "sora hug" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[1] == "hug" and len(meslist) == 3:
            mentions = meslist[-1]
            if "@" in mentions:
                x = random.randint(1,2)
                if x == 1:
                    await message.delete()
                    await message.channel.send(mentions + "<:SoraHuggy:609368621692485633>")
                if x == 2:
                    await message.channel.send("<:SoraMendo:598857944334991371>")

    if "sora slap" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[1] == "slap" and len(meslist) == 3:
            mentions = meslist[-1]
            if "@" in mentions:
                await message.delete()
                if mentions == "<@768265134027440128>" or mentions == "<@!768265134027440128>":
                    await message.channel.send(message.author.mention + "<a:SoraSlap:644371223572119554>")
                else:
                    await message.channel.send(mentions + "<a:SoraSlap:644371223572119554>")

    if "sora kill" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[1] == "kill" and len(meslist) == 3:
            mentions = meslist[-1]
            if "@" in mentions:
                if mentions == "<@768265134027440128>" or mentions == "<@!768265134027440128>":
                    response = random.choice(killsora)
                    await message.channel.send(response)
                else:
                    x = random.randint(1,6)
                    if x == 1:
                        response = mentions + "<a:SoraConsume:670097762188263424>"
                    elif x == 2:
                        response = "*Pushes " + mentions + " into Lake Hakone with a weight attatched*"
                    elif x == 3:
                        response = mentions + "<:SoraHappy2:683311267871850567> <:Dagger:853058515248873473>"
                    elif x == 4:
                        response = "No... too lazy"
                    elif x == 5:
                        response = mentions + "<:SoraEvilGrin:652655851340955674>"
                    elif x == 6:
                        response = mentions + "<:SoraAngry:609367953003118593> <:Dagger:853058515248873473>"
                    await message.channel.send(response)

    if "ping" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[0] == "ping" and len(meslist) == 2:
            mentions = meslist[-1]
            if "@" in mentions:
                await message.delete()
                x = random.randint(1,3)
                if x == 1:
                    response = mentions + " Baka..."
                elif x == 2:
                    response = mentions
                elif x == 3:
                    response = mentions + "<:SoraMendo:598857944334991371>"
                await message.channel.send(response)

    if "sora roast" in message.content.lower():
        meslist = message.content.split(" ")
        if meslist[1] == "roast" and len(meslist) == 3:
            mentions = meslist[-1]
            if "@" in mentions:
                if mentions == "<@768265134027440128>" or mentions == "<@!768265134027440128>":
                    await message.channel.send("No u")
                else:
                    x = random.randint(1,6)
                    if x == 1:
                        response = "You're not even worthy of *worshipping* me."
                    elif x == 2:
                        response = "You're like my internet connection. Slow and unresponsive."
                    elif x == 3:
                        response = mentions + """ There's people like Haru! <:SoraHappy2:683311267871850567>
There's people like Ryouhei. <:SoraMendo:598857944334991371>
Then there's people like you... <:SoraUegh:598833101698891777>"""
                    elif x == 4:
                        response = "You're a... a... uh.. Nao! <:SoraAngry:609367953003118593>"
                    elif x == 5:
                        response = "Nao is better company than you."
                    elif x == 6:
                        response = "Baka <:SoraAngry:609367953003118593>"
                    await message.channel.send(response)

    if "haru" in message.content.lower():
        react = "❤"
        await message.add_reaction(react)

    if message.content == "🍛":
        react = "<:SoraHappy2:683311267871850567>"
        await message.add_reaction(react)

    if "sora give cookies" in message.content.lower():
        react = "\N{cookie}"
        await message.add_reaction(react)

    if message.content.lower() == "omae wa mou shindeiru":
        response = "NANI?!"
        await message.channel.send(response)

    if message.content.lower() == "hello there":
        response = "General Kenobi"
        await message.channel.send(response)

    if message.content.lower() == "splash splash":
        response = "CHAPA CHAPA"
        await message.channel.send(response)

    if message.content.lower() == "sora do you love haru?":
        response = "<:SoraGiggle:698698889993125898>"
        await message.channel.send(response)

    """if "" in message.content.lower():
        react = "<:SoraHappy2:683311267871850567>"
        await message.add_reaction(react)"""

    if message.content == "<@768265134027440128>" or message.content == "<@!768265134027440128>":
        x = random.randint(1,5)
        if x == 1:
            response = message.author.mention + " What? I'm busy."
        elif x == 2:
            response = message.author.mention + " This better not be chores..."
        elif x == 3:
            response = "I'm trying to look at memes. Is this important?"
        elif x == 4:
            response = message.author.mention + " Leave me alone!"
        elif x == 5:
            response = message.author.mention + " What? <a:SoraIcecream:644895514017660939>"
        await message.channel.send(response)

    if message.content.lower() == "hashire sori yo kaze no you ni tsukimihara wo":
        x = random.randint(1,7)
        if x == 1:
            react = "<:SoraPadoru1:689991176509587542>"
        elif x == 2:
            react = "<:SoraPadoru2:689991226971521195>"
        elif x == 3:
            react = "<:SoraPadoru3:689991227873165420>"
        elif x == 4:
            react = "<:SoraPadoru4:689991232994279467>"
        elif x == 5:
            react = "<:SoraPadoru5:689991233002668068>"
        elif x == 6:
            react = "<:SoraPadoru6:689991235884286062>"
        elif x == 7:
            react = "<:SoraPadoru7:689991236983193697>"
        response = "***PADORU PADORU!***"
        await message.add_reaction(react)
        await message.channel.send(response)

    if message.content.lower() == "sora help":
        response = help
        await client.get_user(message.author.id).send(response)

    if "sora crucify" in message.content.lower():
        meslist = message.content.split(" ")
        mentions = meslist[-1]
        if "@" in mentions:
            response = mentions + " <:SoraHappy2:683311267871850567> :cross: :fire:"
            await message.channel.send(response)

    if message.content == "<:SoraAngry:609367953003118593> <:Dagger:853058515248873473>":
        await message.channel.send("<:SoraAngry:609367953003118593> <:Dagger:853058515248873473>")

    if message.content == "<@768265134027440128> <:SoraHuggy:609368621692485633>" or message.content == "<@!768265134027440128> <:SoraHuggy:609368621692485633>":
        await message.channel.send(message.author.mention + " <:SoraHuggy2:704552679178895430>")

    if message.content == "<@768265134027440128> <:SoraHuggy2:704552679178895430>" or message.content == "<@!768265134027440128> <:SoraHuggy2:704552679178895430>":
        await message.channel.send(message.author.mention + " <:SoraHuggy:609368621692485633>")

    kaschat = 668939443121422396
    try:
        kc = message.guild.get_channel(kaschat)
        supv = message.guild.get_channel(718891441539252285)
        offtopic = message.guild.get_channel(620723472988897281)
    except:
        pass

    if "sora add" in message.content.lower() and (admin in message.author.roles or botdev in message.author.roles or mod in message.author.roles):
        role = discord.utils.get(guild.roles, name="Kasugano")
        ment = message.mentions[0].name
        if message.mentions[0]:
            await message.mentions[0].add_roles(role)
            print("role given")
        else:
            print("member not found")
        with open("mesfile.txt", 'r') as f:
            editthisone = int(f.read())
        edit = await kc.fetch_message(editthisone)
        newthing = edit.content.split("\n")
        new = newthing[0] + " " + ment
        listnum = newthing[-1].split(" ")
        listnum[0] = str(int(listnum[0]) + 1)
        if len(new + "." + "\n\n" + listnum[0] + " Total") > 2000:
            await edit.edit(content=newthing[0])
            newedit = await message.channel.send(ment + "\n\n" + listnum[0] + " Total")
            with open("mesfile.txt", 'w') as f:
                f.write(str(newedit.id))
            await newedit.pin()
        else:
            await edit.edit(content=new + "." + "\n\n" + listnum[0] + " Total")

    if message.content == "do the list sora" and (admin in message.author.roles or botdev in message.author.roles or mod in message.author.roles):
        with open("mesfile.txt", 'r') as f:
            editthisone = int(f.read())
        mem5 = await kc.fetch_message(editthisone)
        await mem5.unpin()
        m = mem5.content
        mlist = m.split(".")
        m = ""
        for mem in mlist:
            if len(m+mem) < 2000:
                m += ". " + mem
            else:
                await kc.send(m)
                m = mem
        editthisone = await kc.send(m)
        await editthisone.pin()
        with open("mesfile.txt", 'w') as f:
            f.write(str(editthisone.id))

    if "+1" in message.content.lower() and (
            mod in message.author.roles or admin in message.author.roles or botdev in message.author.roles):
        try:
            total = 0
            write = []
            mes = ""
            cdict = {}
            country = message.content.split(" ")[-1]
            f = open("countries.txt", "r")
            lines = f.readlines()
            f.close()
            editthisone = int(lines[0])
            write.append(lines[0])
            for i in range(1, len(lines)):
                cdict[lines[i].split(":")[0]] = int(lines[i].split(":")[1])
            if country in flagdict and not flagdict[country] in cdict:
                cdict[flagdict[country]] = 0
            cdict[flagdict[country]] += 1
            cdict = dict(sorted(cdict.items(), key=lambda item: item[1]))
            for key in cdict.keys():
                write.append(key + ":" + str(cdict[key]) + "\n")
                print(key + ":" + str(cdict[key]) + "\n")
                mes += key + ": " + str(cdict[key]) + ". "
                total += cdict[key]
            f = open("countries.txt", "w")
            f.writelines(write)
            f.close()
            edit = await offtopic.fetch_message(editthisone)
            await edit.edit(content=mes + "\n\n" + str(total) + " Total")
        except:
            await message.channel.send("No...")

    if "-1" in message.content.lower() and (
            mod in message.author.roles or admin in message.author.roles or botdev in message.author.roles):
        try:
            total = 0
            write = []
            mes = ""
            cdict = {}
            country = message.content.split(" ")[-1]
            f = open("countries.txt", "r")
            lines = f.readlines()
            f.close()
            editthisone = int(lines[0])
            write.append(lines[0])
            for i in range(1, len(lines)):
                cdict[lines[i].split(":")[0]] = int(lines[i].split(":")[1])
            if country in flagdict and not flagdict[country] in cdict:
                cdict[flagdict[country]] = 1
            cdict[flagdict[country]] -= 1
            cdict = dict(sorted(cdict.items(), key=lambda item: item[1]))
            for key in cdict.keys():
                write.append(key + ":" + str(cdict[key]) + "\n")
                print(key + ":" + str(cdict[key]) + "\n")
                mes += key + ": " + str(cdict[key]) + ". "
                total += cdict[key]
            f = open("countries.txt", "w")
            f.writelines(write)
            f.close()
            edit = await offtopic.fetch_message(editthisone)
            await edit.edit(content=mes + "\n\n" + str(total) + " Total")
        except:
            await message.channel.send("No...")

    if message.content.lower() == "sora, reset" and botdev in message.author.roles:
        await message.channel.send("Resetting")
        exit()

    if message.content == "Sora, send a message to edit" and botdev in message.author.roles:
        await message.channel.send("message")


client.run(TOKEN)
