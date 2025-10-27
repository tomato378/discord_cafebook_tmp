import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import threading
from typing import Optional
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix=os.getenv('PREFIX', '!'), intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    if bot.user:
        print(f'✅ Bot is ready! Logged in as {bot.user.name} (ID: {bot.user.id})')
        print(f'📊 Serving {len(bot.guilds)} servers')
        print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('❌ You do not have permission to use this command!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'❌ Missing required argument: {error.param.name}')
    else:
        print(f'Error: {error}')
        await ctx.send('❌ An error occurred while executing this command!')

@bot.command(name='ping')
async def ping(ctx):
    """Check the bot's response time and status"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong!\n💓 API Latency: {latency}ms')

@bot.command(name='help')
async def help_command(ctx):
    """List all available commands"""
    prefix = bot.command_prefix
    embed = discord.Embed(
        title='📚 Available Commands',
        description='Here are all the commands you can use:',
        color=discord.Color.blue()
    )
    
    for command in bot.commands:
        embed.add_field(
            name=f'{prefix}{command.name}',
            value=command.help or 'No description',
            inline=False
        )
    
    embed.set_footer(text=f'Use {prefix}<command> to execute a command')
    await ctx.send(embed=embed)

@bot.command(name='serverinfo')
async def serverinfo(ctx):
    """Display information about the server"""
    if not ctx.guild:
        await ctx.send('❌ This command can only be used in a server!')
        return
    
    guild = ctx.guild
    embed = discord.Embed(
        title='📊 Server Information',
        color=discord.Color.green()
    )
    
    embed.add_field(name='Name', value=guild.name, inline=True)
    embed.add_field(name='ID', value=guild.id, inline=True)
    embed.add_field(name='Owner', value=f'<@{guild.owner_id}>', inline=True)
    embed.add_field(name='Created', value=guild.created_at.strftime('%Y-%m-%d'), inline=True)
    embed.add_field(name='Members', value=guild.member_count, inline=True)
    embed.add_field(name='Channels', value=len(guild.channels), inline=True)
    embed.add_field(name='Roles', value=len(guild.roles), inline=True)
    embed.add_field(name='Boost Level', value=guild.premium_tier, inline=True)
    embed.add_field(name='Boosts', value=guild.premium_subscription_count or 0, inline=True)
    
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    
    await ctx.send(embed=embed)

@bot.command(name='userinfo')
async def userinfo(ctx, member: Optional[discord.Member] = None):
    """Display information about a user"""
    member = member or ctx.author
    
    embed = discord.Embed(
        title='👤 User Information',
        color=discord.Color.purple()
    )
    
    embed.add_field(name='Username', value=str(member), inline=True)
    embed.add_field(name='ID', value=member.id, inline=True)
    embed.add_field(name='Bot', value='Yes' if member.bot else 'No', inline=True)
    embed.add_field(name='Account Created', value=member.created_at.strftime('%Y-%m-%d'), inline=True)
    
    if ctx.guild and member.joined_at:
        embed.add_field(name='Joined Server', value=member.joined_at.strftime('%Y-%m-%d'), inline=True)
        roles = [role.name for role in member.roles if role.name != '@everyone']
        embed.add_field(name='Roles', value=', '.join(roles) if roles else 'None', inline=False)
    
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    """Clear a specified number of messages (requires Manage Messages permission)"""
    if amount < 1 or amount > 100:
        await ctx.send('❌ Please provide a number between 1 and 100!')
        return
    
    try:
        deleted = await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f'✅ Successfully deleted {len(deleted) - 1} messages!')
        await msg.delete(delay=3)
    except discord.Forbidden:
        await ctx.send('❌ I do not have permission to delete messages!')
    except Exception as e:
        print(f'Error clearing messages: {e}')
        await ctx.send('❌ There was an error trying to delete messages!')

if __name__ == '__bot__':
    keep_alive()
    
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print('❌ ERROR: DISCORD_TOKEN not found in environment variables!')
        print('Please add your Discord bot token to the Secrets tab.')
        exit(1)
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print('❌ Failed to login to Discord: Invalid token')
        exit(1)
    except Exception as e:
        print(f'❌ Error starting bot: {e}')
        exit(1)
