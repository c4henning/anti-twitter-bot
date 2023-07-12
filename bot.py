import os
import discord
from dotenv import load_dotenv
import responses


async def send_message(message, user_message, is_private):
    try:
        # pass user message to response generator
        response = responses.handle_response(user_message)
        # prevent sending an empty string as a response
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print("Woah there boss!", e)


def run_discord_bot():
    # bot token has been obfuscated for security
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # intents could probably be limited here
    # this is done on discord.com side instead
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        # Login and server list info prints to terminal
        print(f'{client.user} is active and connected to:')
        guild_count = 0
        omitted_count = 0
        for guild in client.guilds:
            guild_count += 1
            if guild_count > 10:
                omitted_count += 1
            else:
                print('\t-', guild)

        if omitted_count > 0:
            print(f'... and {omitted_count} more omitted.')

    @client.event
    async def on_message(message):
        # prevents replying to bots
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # logs all messages it hears in terminal
        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
