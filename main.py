import discord
client = discord.Client(intents=discord.Intents.all())
sent = set()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(activity=discord.Streaming(name="github.com/j2nx", url="https://www.youtube.com/watch?v=JcelF-4gC_k"))
    
    for guild in client.guilds:
        for member in guild.members:
            if not member.bot and member.id not in sent:
                try:
                    await member.create_dm()
                    await member.dm_channel.send(f'mass dmed message {member.mention}')
                    sent.add(member.id)
                except discord.Forbidden:
                    print(f"unable to mass dm {member.name}")
    


@client.event
async def on_member_join(member):
    try:
        await member.create_dm()
        await member.dm_channel.send(f'join dm message {member.mention}')
    except:
        print(f"unable to dm on {member.name} on join")

@client.event
async def on_member_remove(member):
    try:
        await member.create_dm()
        await member.dm_channel.send(f'leave dm message {member.mention}')
    except:
        print(f"unable to dm {member.name} on join")



client.run('bot token')
