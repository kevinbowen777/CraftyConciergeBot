# CraftyConciergeBot

## Description #

	A very rudimentary bot for use on my Discord channel

## Installation #

    git clone git://github.com/kevinbowen777/dotfiles.git

## Dependencies #

	discord.py
	python-dotenv

In order to not store Discord credentials on GitHub, this script uses
the dotenv library and a .env file. This allows for sensitive data to
be stored locally in the same directory as the script.

The .env file takes the following format:

    # .env
    DISCORD_TOKEN={your-bot-token}
    DISCORD_GUILD={your-guild-name}

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
