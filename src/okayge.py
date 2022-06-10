import discord 
from discord.ext import commands
import random 
from random import randint

bot = commands.Bot(command_prefix=".")

bot.remove_command('help')

token = ""





@bot.event 
async def on_message(message):
    message_count = 0
    acceptedterms = ['Okay', 'okay', 'Okayge', "How are you <@984804937903005766>?"]
    helloterms = ["Hey", "Hi", "Hello", "hey", "hi", "hello"]
    otherterms = ["Hello <@984804937903005766>"]
    swearterms = ["Fuck you <@984804937903005766>", "Fuck off <@984804937903005766>", "Piss off <@984804937903005766>", "Do I care?", "did I ask?", "Did I ask?", "Do I care?"]
    
    if any(word in message.content for word in acceptedterms):
        if not message.author.bot:
         num = randint(0, 40)
         # react
         if num > 20:
          await message.reply('<:okayge:984807384541184040>')
         else: 
            await message.reply('<:okayge:984807384541184040>👍')
    elif message.content in helloterms:
          await message.reply('<:okaygewave:984810292351488030>')
    elif message.content in otherterms:
        await message.reply('https://tenor.com/view/napoleon-dynamite-wave-bye-gif-15387504')
    elif message.content in swearterms:
            num = randint(0, 40)
            if num > 10:
                if num < 20:
                   if message.content == "Fuck you <@984804937903005766>": 
                      await message.reply("<a:shutup:984819046975418460>")
                   else: 
                    await message.reply(f"<:didiask:984818924786941982>")
                elif num > 20:
                   if message.content == "Fuck you <@984804937903005766>": 
                      await message.reply("<a:shutup:984819046975418460>") 
                   else:
                    await message.reply("<:doicare:984818999604944987>")
            else: 
                await message.reply("<a:shutup:984819046975418460>")            
bot.run(token)
