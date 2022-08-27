import discord
from discord.ext import commands
import random

fightdict = {}

class fighter:
    def __init__(self, p):
        self.player = p
        self.hp = 100
        self.defence = 0
    def defend(self):
        x = random.randint(5, 25)
        self.defence += x
        if self.defence > 50:
            self.defence = 50
        return x

    def gethit(self, dmg):
        if self.defence > dmg - 5:
            self.hp -= 5
        else:
            self.hp -= (dmg - self.defence)
        return self.hp

class fight:
    def __init__(self, player1, player2):
        self.player1 = fighter(player1)
        self.player2 = fighter(player2)
        self.turn = random.choice([player1, player2])
        self.nturn = None
        self.swap()

    def __del__(self):
        del self.player2
        del self.player1

    def taketurn(self, action, player):
        self.swap()
        if player.id == self.player1.player.player.id:
            atk = self.player1
            dfnd = self.player2
        elif player.id == self.player2.player.player.id:
            atk = self.player2
            dfnd = self.player1
        if action == "end":
            return None, None
        elif action == "punch":
            dmgnum = random.randint(1, 3)
            if dmgnum == 1:
                dmg = random.randint(1, 19)
            elif dmgnum == 2:
                dmg = random.randint(20, 49)
            elif dmgnum == 3:
                dmg = random.randint(50, 100)
            newhp = dfnd.gethit(dmg)
            return dmg, newhp
        elif action == "defend":
            bulk = atk.defend()
            return bulk, atk.defence

    def swap(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.nturn = self.player1
        else:
            self.turn = self.player1
            self.nturn = self.player2


def RockPaperScissors(user_throw):
    bot_throw_sequence = ['rock', 'paper', 'scissors']
    bot_throw = random.choice(bot_throw_sequence)
    if user_throw == 'rock':
        if bot_throw == 'rock':
            return 'draw', bot_throw
        if bot_throw == 'paper':
            return 'bot', bot_throw
        if bot_throw == 'scissors':
            return 'user', bot_throw
    if user_throw == 'paper':
        if bot_throw == 'rock':
            return 'user', bot_throw
        if bot_throw == 'paper':
            return 'draw', bot_throw
        if bot_throw == 'scissors':
            return 'bot', bot_throw
    if user_throw == 'scissors':
        if bot_throw == 'rock':
            return 'bot', bot_throw
        if bot_throw == 'paper':
            return 'user', bot_throw
        if bot_throw == 'scissors':
            return 'draw', bot_throw


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # Coin flip
        if message.content.lower().startswith('yahiro flip a coin'):
            num = random.randrange(2)
            if num == 1:
                await message.reply('🪙 Oh, would you look at that, it’s heads')
            else:
                await message.reply('🪙 Tails. We’re done here, right?')

        # rock paper scissors
        elif message.content.lower().startswith('yahiro rock') or message.content.lower().startswith(
                'yahiro paper') or message.content.lower().startswith('yahiro scissors'):
            user_throw = message.content[7:]
            user_throw = user_throw.lower()
            if not user_throw or len(user_throw) > 8:
                await message.reply('<:YahiroEh:813653383281377290>')
            else:
                result, bot_throw = RockPaperScissors(user_throw)
                if result == 'user':
                    await message.reply(bot_throw.upper() + '\nYou win... <:YahiroSad:813653383771717672>')
                if result == 'bot':
                    await message.reply(bot_throw.upper() + '\nI Win <:YahiroHappy:616719487928107013>')
                if result == 'draw':
                    await message.reply(bot_throw.upper() + '\nA draw... <:YahiroBothered:616733403546648576>')

        # Dice
        elif message.content.lower().startswith('yahiro roll a dice'):
            dice_responses = ['(number)...', 'yawn (number)', "Ugggggghhhhh... You're so noisy... (number)",
                         "I think it's a (number)", "Let's see, (number)", "My head hurts too much for this. (number)",
                         "(number) \nDid things go the way you wanted?",
                         "Chill out, okay? Gimme a sec. It's a (number)", "Hmm... Looks like (number) wins.",
                         "What? Oh yeah, the dice roll. (number) Totally forgot about that."]
                         
            response = random.choice(dice_responses)
            dice_num = random.randint(1, 6)
            response = response.replace('(number)', str(dice_num))
            await message.reply(response)

        # 8 Ball
        elif message.content.lower().startswith('yahiro 8ball'):
            eightball_responses = ["Sure, whatever",
                                "Hell yeah! <:YahiroHappy:616719487928107013> ",
                                "Cheers to that! :beers:",
                                "No.",
                                "Guess what, brat? No.",
                                "If you feel the need to ask, then it’s probably no.",
                                "Lemme think...yes",
                                "Lemme think...no",
                                "<sigh> Yes",
                                "<sigh> No",
                                "Ugghhhhhhhhhhhh, I think so...",
                                "Ugghhhhhhhhhhhh, I don't think so...",
                                "<yawn> Yes, now let me sleep",
                                "<yawn> No, now let me sleep",
                                "Go bother someone else with your questions",
                                "Too tired right now",
                                "<:YahiroBothered:616733403546648576> ",
                                "Do I HAVE to answer that?",
                                "Can you like... just shut up... for the rest of my life?",
                                "Nyome! Deal with this for me!",
                                "Are Nao's boobs big?",
                                "Does Sora like Haru?",
                                "Does Motoka wear a Maid dress?",
                                "My powers are a little weak at the moment. They might strengthen if you buy a couple of those ice pops over there first."]
            if (message.content.lower().startswith("yahiro 8ball ") == False):
                await message.reply("You need to ask a question, Stupid")
            else:    
                await message.reply(random.choice(eightball_responses))

        # Fight
        elif message.content.lower().startswith("yahiro, i want to fight "):
            if message.author == message.mentions[0]:
                await message.channel.send("You can't fight yourself! <:YahiroBothered:616733403546648576>")
                return
            p1 = fighter(message.author)
            p2 = fighter(message.mentions[0])
            f = fight(p1, p2)
            t = f.turn
            fightdict[message.author.id] = f
            fightdict[message.mentions[0].id] = f
            await message.channel.send("OK, I'll be the ref! <:YahiroHappy:616719487928107013>\n\n" + t.player.player.mention + " Do you want to **Punch, Defend, or End** the fight?")

        elif message.content.lower() in ["punch", "defend", "end"]:
            m = message.author
            a = message.content.lower()
            try:
                f = fightdict[m.id]
            except:
                return
            if f.turn.player.player == m:
                ret1, ret2 = f.taketurn(a, m)
            else:
                return
            defender = f.turn
            dmen = defender.player.player.mention
            if ret1 == None:
                await message.channel.send(f"{m.mention} gave up <:YahiroBothered:616733403546648576>. What a wuss.\n{dmen} wins.")
                del f
                del fightdict[m.id]
                del fightdict[defender.player.player.id]
            elif a == "punch":
                mes = ""
                if ret1 < 20:
                    mes = "Is that all you have? <:YahiroEh:813653383281377290>"
                elif ret1 < 51:
                    mes = "Good hit!"
                elif ret1 < 100:
                    mes = "This is too one sided. <:YahiroBothered:616733403546648576>"
                elif ret1 == 100:
                    mes = "<:YahiroBlush:852673021461397535>"
                await message.channel.send(f"{m.mention} did {ret1} damage. {dmen} has {ret2} health. {mes}")
                if ret2 <= 0:
                    await message.channel.send(f"{dmen} **lost!** Pathetic <:YahiroBothered:616733403546648576>")
                    del f
                    del fightdict[m.id]
                    del fightdict[defender.player.player.id]
                else:
                    await message.channel.send(f"{dmen} Do you want to **Punch, Defend, or End** the fight?")
            elif a == "defend":
                await message.channel.send(f"{m.mention} raised their defence by {ret1}!")
                await message.channel.send(f"{dmen} Do you want to **Punch, Defend, or End** the fight?")

# Setup                                
def setup(client):
    client.add_cog(Games(client))
