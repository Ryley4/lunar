# Note: All IDs have been removed for privacy.
#       Replace placeholders with your own IDs before use.

#py-cord
import discord
import random
import logging
import time
import datetime
import re
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.errors import NotFound, HTTPException, ApplicationCommandInvokeError


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Bot(intents=intents)


# Log error/debug messages (pycord no longer prints in stdout without logging)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

startTime = time.time()

cogs = []

for i in range(len(cogs)):
    cogs[i].setup(bot)

with open('filterList.txt') as file:
    file = file.read().split()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'{status}'))
    print(f'Logged in as {bot.user}')

status = random.choice(
        [
    
            "with fire",

        ]
    )

@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "",
            description = f"{error}",
            color = 0x3584ff,
        )
        await ctx.respond(embed=embed)
    else:
        raise error
    
@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        warn = "Please wait {:.1f} second(s) before using that command again.".format(error.retry_after)
        embed=discord.Embed(title='', description=f'{warn}', color=0xff9800)
        await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    print("on_member_join triggered.")
    try:
        print("Attempting to create embed...")
        
        created_at = member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        
        welcome_channel_id = 00000000000 # <insert channel ID here>
        welcome_channel = bot.get_channel(welcome_channel_id)

        embed = discord.Embed(
            title=f"{member}",
            description=f"Account created on {created_at} UTC±00:00\nUser ID: `{member.id}`\n",
            color=0x3584ff
        )

        avatar_url = member.avatar.url if member.avatar else None
        if avatar_url:
            embed.set_thumbnail(url=avatar_url)

        embed.set_footer(text="System message not manifesting upon the appearance of this report indicates a lack of user input.")

        await welcome_channel.send(embed=embed)

        member_count_channel_id = 00000000000 # <insert channel ID here>
        member_count_channel = bot.get_channel(member_count_channel_id)
        guild = member.guild
        await member_count_channel.edit(name=f'Member Count: {guild.member_count}')
    except Exception as e:
        print(f"Error occurred: {e}")

@bot.event 
async def on_member_remove(member):
    guild = member.guild
    # Member count voice channel id
    channel = bot.get_channel(00000000000) # <insert channel ID here>
    await channel.edit(name = f'Member Count: {guild.member_count}')

# Chat filter event
@bot.event 
async def on_message(message):
    
    if message.author.bot:
        return

    for badword in file:
        if re.search(rf'\b{re.escape(badword)}\b', message.content, re.I):
            author = message.author
            drone = bot.get_channel(000000000000000) # <insert mod channel ID here>
            embed = discord.Embed(title=f'Message Removed • {author}', color=0xff0000)
            embed.add_field(name="Author", value=f"{message.author.mention}", inline=True)
            embed.add_field(name="Content", value=f"{message.content}", inline=True)
            embed.add_field(name="Location", value=f"{message.channel.mention}", inline=True)
            embed.set_footer(text=f"Reference: {author} • {author.id}")
            embed.timestamp = datetime.datetime.utcnow()
            await drone.send(embed=embed)
            await message.delete()
            return 

@bot.slash_command(name="ping", description="Check if Lunar is online.")
@commands.cooldown(2, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.respond(
        random.choice(
            [
               "<insert_reply_here>",
            ]
        ), ephemeral=True
    )

@bot.slash_command(name="uptime", description="Show Lunar's uptime.")
@commands.cooldown(2, 5, commands.BucketType.user)
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(
        title = "",
        description = f"{uptime}",
        color = 0x3584ff,
    )
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="kick", description="Kick a server member.")
@has_permissions(kick_members=True, ban_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title = "",
        description = f"{member.mention} has been kicked.",
        color = 0xff0000,
    )
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="ban", description="Ban a server member.")
@has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: discord.Member, file: discord.Attachment=None, reason=None):
    try:
        embed = discord.Embed(
            title = "",
            description = f"{member.mention} has been banned.",
            color = 0xff0000,
        )
        embed.set_footer(text=f"Reference: {member} • {member.id}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.respond(embed=embed)

        author = ctx.author
        banMuteChannel = bot.get_channel(00000000000000) # <insert ban log channel ID here>

        embed = discord.Embed(
            title = "",
            description = "",
            color = 0xff0000,
        )
        embed.set_author(
            name = f"Ban  •  {member}",
            icon_url = f"{member.avatar}",
        )
        embed.add_field(
            name = "User",
            value = f"{member.mention}",
            inline = True,
        )
        embed.add_field(
            name = "Moderator",
            value = f"{author}",
            inline = True,
        )
        embed.add_field(
            name = "Reason",
            value = reason,
            inline = True,
        )
        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.utcnow()
        await member.ban(reason=reason)
        await banMuteChannel.send(embed=embed)
        if file is not None:
            await banMuteChannel.send(file=file)

    except discord.NotFound:
        embed = discord.Embed(
            title = '',
            description = 'This ID could not be found in this server.',
            color = 0xff9800,
        )
        await ctx.respond(embed=embed)
    except discord.HTTPException: 
        embed = discord.Embed(
            title = '',
            description = 'ID could not be found in this server.',
            color = 0xff9800,
        )
        await ctx.respond(embed=embed)
    except ValueError:
        embed = discord.Embed(
            title = '',
            description = 'Unknown member_id.',
            color = 0xff9800,
        )

@bot.slash_command(name="unban", description="Unban a previously banned server member.")
@has_permissions(kick_members=True, ban_members=True)
async def unban(ctx, member : discord.Member):
    try:
        await ctx.guild.unban(member)
        embed = discord.Embed(
            title = "",
            description = f"{member.mention} has been unbanned.",
            color = 0x3584ff,
        )
        await ctx.respond(embed=embed)
    except discord.NotFound:
        embed = discord.Embed(
            title = '',
            description = 'This ID does not belong to a user.',
            color = 0xff9800,
        )
        await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="eject", description="sussus amongus")
@has_permissions(kick_members=True, ban_members=True)
async def eject(ctx, member : discord.Member):
    guild = member.guild
    embed = discord.Embed(
        title = "",
        description = f"{member.mention} was not The Impostor.    ~ ඞ\n {guild.member_count} Impostors remains.",
        color = 0xff0000,
    )
    await ctx.guild.kick(member)
    await ctx.send(embed=embed)

@bot.slash_command(name="mute", description="Mute a server member.")
@has_permissions(kick_members=True, ban_members=True)
async def mute(ctx, member:discord.Member, file: discord.Attachment=None, reason=None):
    try:
        embed = discord.Embed(
            title = "",
            description = f"{member.mention} has been muted.",
            color = 0xff0000,
        )
        embed.set_footer(text=f"Reference: {member} • {member.id}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.respond(embed=embed)

        author = ctx.author
        banMuteChannel = bot.get_channel(000000000000000) # insert ban log channel ID here
        guild = ctx.guild
        muteRole = member.guild.get_role(000000000000000) # insert mute role ID here 

        embed = discord.Embed(
            title = "",
            description = "",
            color = 0xff0000,
        )
        embed.set_author(
            name = f"Mute  •  {member}",
            icon_url = f"{member.avatar}",
        )
        embed.add_field(
            name = "User",
            value = f"{member.mention}",
            inline = True,
        )
        embed.add_field(
            name = "Moderator",
            value = f"{author}",
            inline = True,
        )
        embed.add_field(
            name = "Reason",
            value = reason,
            inline = True,
        )
        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.utcnow()

        await member.add_roles(muteRole)
        await banMuteChannel.send(embed=embed)
        await banMuteChannel.send(file)

    except discord.NotFound:
        embed = discord.Embed(
            title = '',
            description = 'This ID does not belong to a user.',
            color = 0xff9800,
        )
    except discord.Forbidden:
        embed = discord.Embed(
            title = '',
            description = f'Elevated permissions required to mute {member.mention}.',
            color = 0xff9800,
        )
        await ctx.respond(embed=embed)

@bot.slash_command(name="unmute", description="Unmute a server member.") 
@has_permissions(kick_members=True, ban_members=True)
async def unmute(ctx, member: discord.Member, reason=None):

    shameCorner = member.guild.get_role(0000000000000) # insert server mute role ID here

    if shameCorner in member.roles:
        await member.remove_roles(shameCorner)
        await ctx.respond("✅")

    else:
        embed=discord.Embed(title='', description=f'Failed to unmute {member.mention}.', color=0xff0000)
        await ctx.send(embed=embed)

@bot.slash_command(name="rename", description="Rename a channel name.")
@has_permissions(kick_members=True, ban_members=True)
async def rename(ctx, channel: discord.TextChannel, *, new_name):
    await channel.edit(name=new_name)
    await ctx.respond("✅", ephemeral=True)

@bot.slash_command(name="slowmode", description="Enable slowmode for x second(s).")
@has_permissions(kick_members=True, ban_members=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    embed = discord.Embed(
        title = f'Slowmode has been set to {seconds} second(s).',
        color = 0xff9800,
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.respond(embed=embed, ephemeral=False)

@bot.slash_command(name="filteradd", description="Add a new word to chat filter.")
@has_permissions(kick_members=True, ban_members=True)
async def filteradd(ctx, word):
    filter = open('filterList.txt', "a")
    filter.write(word + "\n")
    filter.close()    
    await ctx.respond("✅")

@bot.slash_command(name="filterdel", description="Remove a word from chat filter.")
@has_permissions(kick_members=True, ban_members=True)
async def filterdel(ctx, word):
    filter = open("filterList.txt", "r")
    lines = filter.readlines()
    filter.close()

    newfilter = open("filterList.txt", "w")
    for line in lines:
        if line.strip('\n') != word:
            newfilter.write(line)

    newfilter.close()

    await ctx.respond("✅")

@bot.slash_command(name="filterlist", description="Display chat filter data.")
@has_permissions(kick_members=True, ban_members=True)
async def filterlist(ctx):
    filter = open("filterList.txt", "r")
    content = filter.read()
    content_list = content.splitlines()
    filter.close()
    await ctx.respond(f'`{content_list}`')

@bot.slash_command(name="relay", description="Relay a message as Lunar.")
@has_permissions(kick_members=True, ban_members=True)
async def relay(ctx, *, message):
    await ctx.send(f'{message}')
    
@bot.slash_command(name="info", description="Display info window.")
@commands.cooldown(2, 5, commands.BucketType.user)
async def info(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed=discord.Embed(title = '', description = '', color=0x3584ff)
    embed.set_author(name = "Lunar", icon_url="https://cdn.discordapp.com/emojis/1172733676933611570.webp?size=96&quality=lossless")
    embed.add_field(name = "Library" , value = "py-cord", inline=False)
    embed.add_field(name = "Version" , value = "-", inline=True)
    embed.add_field(name = "Type " , value = "Private", inline=True)
    embed.add_field(name = "Uptime" , value = f"{uptime}", inline=True)
    embed.add_field(name = "Host" , value = "-", inline=True)
    embed.set_footer(text=f"Reference ID: 724865184983810128")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.respond(embed=embed)

@bot.slash_command(name="clear", description="Remove specified number of messages. (Default = 4)")
@has_permissions(kick_members=True, ban_members=True)
async def clear(ctx, amount=4):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)
    await ctx.respond("✅", ephemeral=True)

@bot.slash_command(name="emoteurl", description="Display emote URL.")
@commands.cooldown(2, 5, commands.BucketType.user)
async def emoteurl(ctx, emoji: discord.PartialEmoji):
    await ctx.respond(emoji.url, ephemeral=False)

@bot.slash_command(name="services", description="Display Lunar's autonomous modules.")
@has_permissions(kick_members=True, ban_members=True)
async def services(ctx):

    embed=discord.Embed(title="Autonomous Modules", description=description, colour=0x3584ff)
    embed.set_footer(text=f'Latency:  {round(bot.latency * 1000)}ms')
    await ctx.respond(embed=embed, ephemeral=True)

description = ("\n`on_member_join` Passive member-join screening."
              "\n`member_count` Updates member counter."
              "\n`auth_ping` Unauthorized ping detection."
              "\n`filter` Chat filter."
              )

@bot.slash_command(name='pfpurl', help="Display a member's pfp URL.")
@commands.cooldown(2, 5, commands.BucketType.user)
async def avatar(ctx, *, member: discord.Member = None):

    if member is None:
        member = ctx.author

    await ctx.respond(member.avatar.url, ephemeral=True)

@bot.slash_command(name='lock', description="Restrict members from sending messages in current or specified channel.")
@has_permissions(kick_members = True, ban_members = True)
async def lock(ctx, channel: discord.TextChannel):
    restricted_channels = [00000000,
                           ] 
    if channel.id in restricted_channels:
        embed = discord.Embed(
            title="",
            description="The use of this command in a private channel is forbidden.",
            color=0xff9800
        )
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        restricted_channels.append(channel.id)
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond("✅", ephemeral=True)

@bot.slash_command(name='unlock', description="Allow members to send messages in current or specified channel.")
@has_permissions(kick_members = True, ban_members = True)
async def unlock(ctx, channel: discord.TextChannel):
    restricted_channels = [000000000,
                           ] 
    if channel.id in restricted_channels:
        embed = discord.Embed(
            title="",
            description="The use of this command in a private channel is forbidden.",
            color=0xff9800
        )
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        restricted_channels.append(channel.id)
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond("✅", ephemeral=True)
        

bot.run("") 
