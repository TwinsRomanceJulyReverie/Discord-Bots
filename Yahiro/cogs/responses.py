import discord
from discord.ext import commands
import random
import re

class Responses(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # Prevent Repeats
        if message.author == self.client.user:
            return

        # Command List
        elif message.content.lower().startswith('yahiro help'):
            with open('CommandList.txt') as f:
                command_list = f.read()
                await message.author.send(command_list)

        # Responses
        elif message.content.lower().startswith('i love you yahiro') or message.content.lower().startswith('i love you, yahiro'):
            await message.channel.send('<:YahiroEh:813653383281377290>')

        elif message.content.lower().startswith('how are you yahiro?'):
            await message.channel.send('No alcohol...<:YahiroSad:813653383771717672>')

        elif message.content.lower().startswith('good morning yahiro') or message.content.lower().startswith('gm yahiro'):
            await message.channel.send('its a great day for commerce <:YahiroHappy:616719487928107013>')

        elif message.content.lower().startswith('good night yahiro') or message.content.lower().startswith('gn yahiro'):
            await message.channel.send('Way ahead of you.')
        
        elif message.content.lower().startswith('yahiro kill'):

            # guild = self.client.get_guild(813586694255149096) # Test
            guild = self.client.get_guild(348796287606456321) # YnS

            user_to_kill = message.content[12:]
            m = message.mentions[0]
            
            if m is not None:
                kill_responses = ["DIE! <:YahiroEh:813653383281377290> :axe:",
                                "Rest in pieces <:YahiroHappy:616719487928107013> :carpentry_saw:",
                                "No, leave me alone <:YahiroBothered:616733403546648576>",
                                "Nyome would not approve <:YahiroSad:813653383771717672>",
                                "<:YahiroBlush:852673021461397535>",
                                "<:AkiraShishouGun:644894915175776256>"]
                
                user_id = m.id
                
                if self.client.get_user(user_id) == self.client.user:   # Can't kill self
                    return

                elif user_id == 1000295303439732796: # Akira bot                    
                    await message.channel.send(f'Akira kill <@!{message.author.id}>')
                    
                elif guild.get_member(user_id) is not None:
                    await message.channel.send(f'{user_to_kill} {random.choice(kill_responses)}')


        # Reactions
        elif message.content.lower().startswith('stupid bots'):
            await message.add_reaction('<:YahiroBothered:616733403546648576>')

        elif (message.content.startswith('<:MotokaHappy:616738739259179063>') 
            or message.content.lower().startswith('<:AkiraHappy:852672068766924820>')
            or message.content.lower().startswith('<:AkiraHappy2:598913220085940244>')):

            await message.add_reaction('<:YahiroHappy:616719487928107013>')
        elif message.content.lower() == "yahiro, reset" and message.author.id == 407747014806208523:
            await message.channel.send("Resetting")
            exit()


def setup(client):
    client.add_cog(Responses(client))