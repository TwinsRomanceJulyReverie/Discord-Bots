import discord
from discord.ext import commands
import json
import random
import asyncio
import re

class Trivia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # Trivia Game
        elif message.content.lower().startswith('yahiro trivia'):
            with open('TriviaQuestions.json') as f:
                data = json.load(f)
            question = random.choice(data['questions'])

            choices = []
            if "4" in question:
                choices = [question["1"], question["2"], question["3"], question["4"]]
            if "3" in question and not choices:
                choices = [question["1"], question["2"], question["3"]]
            if "2" in question and not choices:
                choices = [question["1"], question["2"]]
            if "1" in question and not choices:
                choices = [question["1"]]

            random.shuffle(choices)
            question_message = f'Question: {question["question"]}  ({question["difficulty"]})\n'
            count = 0
            for choice in choices:
                count += 1
                question_message += f'{count}. {choice}\n'
            
            await message.reply(question_message)
            
            user = message.author
            def check(message: discord.Message):
                return message.author == user
            
            try:
                while True:
                    user_reply = await self.client.wait_for('message', timeout=15.00, check=check)
                    user_answer = user_reply.content.lower()

                    if re.match(f'^[1-{len(choices)}]$', user_answer):
                        if choices[int(user_answer) - 1] == question['answer']:
                            await message.reply("<:YahiroHappy:616719487928107013> Correct!")
                        else:
                            await message.reply("<:YahiroEh:813653383281377290> That's wrong...")
                        break

            except asyncio.TimeoutError:
                await message.channel.send('<:YahiroBothered:616733403546648576> You took too long...')

        # Trivia Leaderboard
        elif message.content.lower().startswith('yahiro leaderboard'):
            await message.reply("Ask me later...")


def setup(client):
    client.add_cog(Trivia(client))
