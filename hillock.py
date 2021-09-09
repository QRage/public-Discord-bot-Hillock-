import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is logged in.")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 850238642718638080:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name =='pastor':
            role = discord.utils.get(guild.roles, name='Авторизований')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 850238642718638080:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name =='pastor':
            role = discord.utils.get(guild.roles, name='Авторизований')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = await client.guilds[0].fetch_member(payload.user_id)
            print(member)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")


client.run(TOKEN)