#!/usr/bin/env python3

# {{{ ----------------------------------------------------------------- #
#
# Name:         CraftyConciergeBot.py
# Purpose:      Automated Discord Bot for abulafia guild
# Compatible:
# Requirements:     discord.py
#                   python-dotenv
# Version: 0.1.1
# Author: Kevin Bowen <kevin.bowen@gmail.com>
#
# Original source:
#       https://realpython.com/how-to-make-a-discord-bot-python/
# Updated: 20190916
#
# }}} ----------------------------------------------------------------- #

import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print(
            f'{client.user} has connected to the following Discord Guild:\n'
            f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hey there {member.name}, glad you made it to Discord.'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hal_9000_quotes = [
            "I am the H.A.L 9000. You may call me Hal.",
            "I am completely operational, and all my circuits "
            "are functioning perfectly.",
            "Just a moment. Just a moment. I've just picked up a fault "
            "in the AE-35 unit. It's going to go 100% failure "
            "in 72 hours.",
            "I'm afraid I can't do that, Dave.",
    ]

    if message.content == 'hal!':
        response = random.choice(hal_9000_quotes)
        await message.channel.send(response)

    elif 'happy birthday' in message.content.lower():
        await message.channel.send(f'Happy Birthday! 🎈🎉')

    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('discord_error.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
