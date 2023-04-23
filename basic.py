import disnake
from disnake.ext import commands
import os


bot = commands.Bot(command_prefix='*')


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    global bot
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reactions = message.reactions
    if message.author.id == bot.user.id and len(message.embeds) > 0:
        likes = dislikes = 0
        if message.embeds[0].title == 'Голосование блогов':
            for reaction in reactions:
                if reaction.emoji == '👍':
                    likes = reaction.count - 1
                elif reaction.emoji == '👎':
                    dislikes = reaction.count - 1
            if likes + dislikes == 0:
                likesperc = 0
            else:
                likesperc = 100*likes/(likes+dislikes)
            embed = disnake.Embed(title='Голосование блогов',\
                                  description=message.embeds[0].description)\
                                  .add_field('Лайков', str(likes)).add_field('Дизлайков', str(dislikes))\
                                  .add_field('Процент лайков', str(likesperc)[:5])
            await message.edit(embed=embed)


@bot.event
async def on_raw_reaction_remove(payload):
    global bot
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reactions = message.reactions
    if message.author.id == bot.user.id and len(message.embeds) > 0:
        likes = dislikes = 0
        if message.embeds[0].title == 'Голосование блогов':
            for reaction in reactions:
                if reaction.emoji == '👍':
                    likes = reaction.count - 1
                elif reaction.emoji == '👎':
                    dislikes = reaction.count - 1
            if likes + dislikes == 0:
                likesperc = 0
            else:
                likesperc = 100*likes/(likes+dislikes)
            embed = disnake.Embed(title='Голосование блогов',\
                                  description=message.embeds[0].description)\
                                  .add_field('Лайков', str(likes)).add_field('Дизлайков', str(dislikes))\
                                  .add_field('Процент лайков', str(likesperc)[:5])
            await message.edit(embed=embed)


@bot.slash_command(description="Голосование блогов", guild_ids=[465128456280080384])
async def blogsvote(inter):
    if inter.author.id != 332398668252708864:
        return await inter.send('Вы не Гедор!')
    await inter.send('Начинаем...', ephemeral=True)
    for search in inter.guild.categories:
        if search.id == 549192015309701120:
            for blog in search.channels:
                if blog.id not in (748553951451938898, 761947124237467659, 907311864147496971, 1060149935766511637)\
                        and 'архив' not in blog.name:
                    embed = disnake.Embed(title='Голосование блогов', \
                                          description=f'Проголосуйте за блог {blog.mention}')\
                        .add_field('Лайков', '0').add_field('Дизлайков', '0')
                    msg = await inter.channel.send(embed=embed)
                    await msg.add_reaction('👍')
                    await msg.add_reaction('👎')


@bot.slash_command(description="тест")
async def att(inter, att: disnake.Attachment):
    await inter.send('aaass', ephemeral=True)


token = os.environ.get('TOKEN')
bot.run(token)