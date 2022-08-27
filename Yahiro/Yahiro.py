import discord
from discord.ext import commands
import random
from imgurpython import ImgurClient
import os


# Get Client
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents = intents)
imgur_client = ImgurClient('b2129c4fdd96a11', '13a803e30483767b077dbbb9f9883a4f65b9eae9')

# Load Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='やひろの進路'))

# On message events
@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.mention_everyone:
        return

    # Ping bot response
    if client.user.mentioned_in(message):
        mention_responses = ["FOR THE LOVE OF GOD WHAT?", 
                            "THIS BETTER BE IMPORTANT",
                            "<:YahiroPing:853459359744393247>",
                            "<:YahiroBlush:852673021461397535>",
                            "<:WhoSummonedTheAlmighty:852669869152272415>",
                            "So if I put off rent for another week, I can pay the utility bill... Huh? What was that? Kinda busy right now."]
        await message.channel.send(random.choice(mention_responses))

    # Gallery
    elif message.content.lower().startswith('yahiro gallery'):
        album = imgur_client.get_album_images('ACoXw3k')
        if len(album) > 0:
            pic = random.randint(0, len(album))
            await message.reply(album[pic].link)
        else:
            await message.reply('no images found')

# Bot Token
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client.run(token)