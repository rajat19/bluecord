# Work with Python 3.6
import discord
from db import post_search_data, fetch_search_data
import settings as my_settings
from search import search_main

TOKEN = my_settings.BOT_AUTH_TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    print(f'message {message}')
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        msg = 'Hey {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        post_search_data(author_id, query)

        results = search_main(query)
        if results:
            links = ' \n'.join(results)
            # print(links)
            msg = 'Hello {}, you searched for {}. The top five results are: \n {}'.format(
                message.author.mention, query, links)
        else:
            msg = 'Hello {}, you searched for {}. \n Sorry, no matching links found.'.format(
                message.author.mention, query)
        await message.channel.send(msg)

    if message.content.startswith('!recent'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        results = fetch_search_data(author_id, query)
        # print(results)
        if(len(results) > 0):
            keywords = 'Your matching search results are: \n' + \
                ' \n'.join([x[2] for x in results])
        else:
            keywords = 'No matching results found'
        await message.channel.send(keywords)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

client.run(TOKEN)