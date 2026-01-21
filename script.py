# ii's Stupid Bot
# Probably exploitable, probably bad
# A lot of ChatGPT was used during this I'll admit
# ..because I didn't know how to make a Discord bot

# I know now don't dunk on me

# Looking for people to help rewrite this stinkbot

import discord
import asyncio
import os
import json
import sys
import time
import yt_dlp
import random
import re
import base64
import json
import math
import socket
import aiohttp
import requests
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import glob

from discord import app_commands
from datetime import timedelta, datetime, timezone
from collections import defaultdict
from collections import deque
from datetime import datetime

TOKEN = ''
privwhurl = ''
authenticationkey = ''
ADMINROLES = [1177487180453646387, 1170116321388810411, 1170116220855537754, 1170863596100657283, 1207131095834038343]
SHITPINGPROTECTED = [1170863596100657283, 1237953269930917959, 1200174270819598478, 1170858334878965791]
SHITPOSTS = [""]
AUTOIDS = []
REMOVALIDS = []
HARDBAN = []
values = []
last_execution_times = {}
user_message_tracker = defaultdict(lambda: defaultdict(set))

TIME_WINDOW = 60
user_last_message_time = defaultdict(lambda: time.time())

# Bad words, I support everyone and this is only for auto moderation
bannedNameKeywords = ["nigger", "nigga", "nigg", "gigga", "fag", "faggot", "niger", "nigeria", "hitler", "kkk", "jews", "cracker", "fagget", "chink", "tranny", "iga", "niga", "igga", "igger", "iger", "trannies", "trany", "trannys", "tranies", "пigger", "пiggа", "пiga", "卍", "卐", "pornhub.com", "e621.net", "xvideos", "onlyfans.com", "adolf", "hilter", "hitler", "ni99er", "migger", "migga", "childporn", "rape", "raped", "raping", "raper", "rapes", "niiger", "niig", "nig", "nega", "osama", "laden", "binladen", "osamabinladen", "blacky", "blackies", "goy", "israel", "floyd"]
blacklisted_mods = ["stupidmenu", "stupid_menu", "stupid menu", "prism", "shibagt", "shiba gt", "shiba-gt", "shiba_gt" "utilla", "sscosmetx", "cosmetxss", "sscosmetics", "sscosmeticx", "cosmeticsss", "cosmeticxss" "grate", "bark", "citrvs", "totalk", "to talk", "talk"]
faqMessages = ['detected', 'kick', 'crash', 'lag', 'removed', 'watch', 'joystick', 'keybind', 'gui', ' ui ', 'sound', 'soundboard', 'master']

RAINBOW_COLORS = [
    0xFF3A3A,  # Red
    0xFFA048,  # Orange
    0xFFE95D,  # Yellow
    0x6EE25C,  # Green
    0x6999F8,  # Blue
    0x9841DB,  # Indigo
    0xF6A5FF   # Violet
]

RAINBOW_COLOR_INDEX = -1
LATEST_HASH = "?"

owners = [
    894348631904223232, # crimsoncauldron
    1129786377643503687, # golden.trophy (ii's alt)
    1317665262387986515, # rocklobster
    738573735895892050, # twigcore
    252548095244500994 # kingofnetflix
]

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
bans_log = deque()
leave_log = deque()

STICKIED_FOLDER = 'stickied/'
if not os.path.exists(STICKIED_FOLDER):
    os.makedirs(STICKIED_FOLDER)

FFMPEG_OPTIONS = {'options': '-vn'}
message_counts = {}
try:
    with open("yapdata.json", 'r') as file:
        message_counts = json.load(file)
except FileNotFoundError:
    message_counts = {}

try:
    with open("token.txt", 'r') as file:
        TOKEN = file.read().strip()
except FileNotFoundError:
    print("Error: token.txt not found.")

try:
    with open("authenticationkey.txt", 'r') as file:
        authenticationkey = file.read().strip()
except FileNotFoundError:
    print("Error: authenticationkey.txt not found.")

try:
    with open("dynowh.txt", 'r') as file:
        privwhurl = file.read().strip() 
except FileNotFoundError:
    print("Error: dynowh.txt not found.")

cosmeticdata = ""
try:
    with open("cosmetics.txt", 'r') as file:
        cosmeticdata = file.read().strip() 
except FileNotFoundError:
    print("Error: cosmetics.txt not found.")

try:
    with open("memes.txt", 'r') as file:
        SHITPOSTS = json.load(file)
except FileNotFoundError:
    with open("memes.txt", 'w') as file:
        json.dump(SHITPOSTS, file)

try:
    with open("hardban.json", 'r') as file:
        HARDBAN = json.load(file)
except FileNotFoundError:
    with open("hardban.json", 'w') as file:
        json.dump(HARDBAN, file)

mc_verified = {}
try:
    with open("mc_verified.txt", 'r') as file:
        mc_verified = json.load(file)
except FileNotFoundError:
    with open("mc_verified.txt", 'w') as file:
        json.dump(mc_verified, file)

lastyapper = 31
if message_counts:
    lastyapper = max(message_counts, key=message_counts.get)

lastTimeRepliedDM = 0
lastTimeRepliedDM2BCIFUCKEDITUP = 0
lastTimeRepliedDM3 = 0
lastTimeRepliedDM4 = 0
lastTimeRepliedDM5 = 0
lastTimeiiDkTalked = 0
announcementNotificationDelay = 0
start_time = time.time()

lastMembers = -1
curstat = discord.Status.idle

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            try:
                await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=str(client.guilds[0].member_count)+' numbskulls'))
            except:
                print("SOmehow couldn't do the most basic shit ever")

            try:
                filename = "/home/iiDk/memecount.txt"
                if not os.path.isfile(filename):
                    with open(filename, 'w') as file:
                        file.write('0')
                
                count = 0
                with open(filename, 'r') as file:
                    count = int(file.read().strip())

                count += 1
                await client.get_channel(1244077655452553246).send("Meme #"+str(count)+"\n"+random.choice(SHITPOSTS))

                with open(filename, 'w') as file:
                    file.write(str(count))
            except:
                print("No meme")

            await update_user_count()

            #try:
            #    url_prefix = "https://goldentrophy.software/"
            #    channel = client.get_channel(1183532196431134753)

            #    if channel is None:
            #        print("Channel not found.")
            #    elif not isinstance(channel, discord.TextChannel):
            #        print("Invalid channel type.")
            #    else:
            #        async for message in channel.history(limit=None, oldest_first=True):
            #            if message.content.startswith(url_prefix):
            #                await channel.send(message.content)
            #                await message.delete()
            #except:
            #    print("Whoops")

            try:
                global LATEST_HASH

                response = requests.get("https://api.seralyth.software/hash/Gorilla%20Tag_Data/Managed/Assembly-CSharp.dll") # Hash API if you want to use it I guess
                response.raise_for_status()
                data = response.json()

                LAST_HASH = LATEST_HASH
                LATEST_HASH = data.get("sha256")

                if len(LAST_HASH) > 1:
                    if LAST_HASH != LATEST_HASH:
                        await client.get_channel(1170116897182855249).send("# Gorilla Tag Update\nGorilla Tag has updated on Steam\n> Previous Hash: `" + LAST_HASH + "`\n> Current Hash: `" + LATEST_HASH + "`\n<@&1189695871735042068>\n-# Powered by kingofnetflix")
            except Exception as e:
                print("Could not get latest hash\n"+str(e))

            rainbowRole = client.guilds[0].get_role(1349857882082119720)
            
            if rainbowRole:
                global RAINBOW_COLOR_INDEX
                RAINBOW_COLOR_INDEX += 1

                if RAINBOW_COLOR_INDEX > len(RAINBOW_COLORS) - 1 or RAINBOW_COLOR_INDEX < 0:
                    RAINBOW_COLOR_INDEX = 0

                hex_code = RAINBOW_COLORS[RAINBOW_COLOR_INDEX]

                try:
                    await rainbowRole.edit(color=discord.Color(hex_code), reason="Rainbow role effect")
                except discord.Forbidden:
                    print("Missing permissions to edit role")
                    return
                except discord.HTTPException as e:
                    print(f"Failed to change role color: {e}")
            else:
                print("Rainbow role does not exist")

            if not os.path.isfile("lasthealthcheck.txt"):
                with open("lasthealthcheck.txt", 'w') as file:
                    file.write('0')

            with open("lasthealthcheck.txt", "r") as file:
                if int(datetime.now(timezone.utc).timestamp()) > int(file.read()) + 1209600:
                    with open("lasthealthcheck.txt", 'w') as files:
                        files.write(str(int(datetime.now(timezone.utc).timestamp())))

                    await client.get_channel(1170093288989147329).send('Bot health checkup in progress')

                    await client.get_channel(1170093288989147329).send('Setting system time')
                    os.system("sudo timedatectl set-ntp true")

                    await client.get_channel(1170093288989147329).send('Removing expired packages')
                    os.system("sudo apt autoremove -y")
                    os.system("sudo apt clean")

                    await client.get_channel(1170093288989147329).send('Health checkup complete')
                    await client.get_channel(1170093288989147329).send('Restarting script, please wait...')
                    os.system("sudo systemctl restart iibot")

            # elapsed_time_ms = math.floor((time.time() - start_time) * 1000)
            # if elapsed_time_ms > 86400000:
                # await client.get_channel(1170093288989147329).send('Bot is restarting, please wait...')
                # os.system("sudo reboot")
        except:
            print("Error")

        await asyncio.sleep(60)

@client.event
async def on_ready():
    elapsed_time_ms = math.floor((time.time() - start_time) * 1000)
    print(f'Logged in as {client.user}')
    try:
        if os.path.exists("fromrestart.txt"):
            with open("fromrestart.txt", 'r') as file:
                await discord.utils.get(client.guilds[0].channels, id=1170093288989147329).send(f'Bot restarted in `{elapsed_time_ms:.2f}ms` <@'+file.read().strip()+">")
            os.remove("fromrestart.txt")
        else:
            await discord.utils.get(client.guilds[0].channels, id=1170093288989147329).send(f'Bot started in `{elapsed_time_ms:.2f}ms`')
        
        await discord.utils.get(client.guilds[0].channels, id=1458530151318159421).send(content="Meme archive", file=discord.File("memes.txt"))
        await discord.utils.get(client.guilds[0].channels, id=1458530151318159421).send(content="Yap archive", file=discord.File("yapdata.json"))
    except:
        print("Could not announce bot start time")
        print(f'Bot started in `{elapsed_time_ms:.2f}ms`')
    if not hasattr(client, 'background_task'):
        client.background_task = client.loop.create_task(my_background_task())

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.guild is None:
            print("[DM] " + str(message.author.name)+": "+str(message.content)+" in dms")
            if any(role.id in ADMINROLES for role in client.guilds[0].get_member(message.author.id).roles):
                try:
                    await handleCommand(message)
                except Exception as e:
                    await client.get_channel(1458530151318159421).send("Bot error with " + str(message.content) + ": " + str(e))

            else:
                global lastTimeRepliedDM2BCIFUCKEDITUP # tomato
                if (time.time() > lastTimeRepliedDM2BCIFUCKEDITUP):
                    lastTimeRepliedDM2BCIFUCKEDITUP = time.time() + 5
                    await message.author.send("**I am not a real person**, I'm just a bot used to automatically moderate the server.\nIf you need to talk to a real moderator, feel free to message anyone else.\n\n`This message is automated. If this was not what you were looking for, ignore this message.`")
        else:
            global lastTimeiiDkTalked
            if any(role.id in ADMINROLES for role in message.author.roles):
                print("[MOD] " + str(message.author.name)+": "+str(message.content)+" in #"+str(message.channel.name))

                global announcementNotificationDelay
                if message.channel.id == 1170116897182855249 and time.time() > announcementNotificationDelay: # announcements
                    #if '@here' in str(message.content) or '@everyone' in str(message.content) or '<@&1170859430158532761>' in str(message.content) or '<@&1207083443956228176>' in str(message.content):
                    announcementNotificationDelay = time.time() + 60
                    await client.get_channel(1170093288989147329).send(f"# New Announcement\nA new announcement has been posted.\nRead here: <#1170116897182855249>")

                if message.channel.id == 1170117473912238150: # downloads
                    await message.add_reaction("✅")

                if message.channel.id == 1244093290916216874: # meme uploader
                    if message.attachments:
                        media_links = [attachment.url for attachment in message.attachments]
                        for link in media_links:
                            print("Media link:", link)
                            filename = "memecount.txt"
                            if not os.path.isfile(filename):
                                with open(filename, 'w') as file:
                                    file.write('0')
                            
                            count = 0
                            with open(filename, 'r') as file:
                                count = int(file.read().strip())

                            count += 1
                            await client.get_channel(1244077655452553246).send("Meme #"+str(count)+"\n"+link)

                            SHITPOSTS.append(link)

                            with open("memes.txt", 'w') as file:
                                json.dump(SHITPOSTS, file)

                            with open(filename, 'w') as file:
                                file.write(str(count))
                    if message.content:
                        if "http" in message.content:
                            link = message.content
                            print("Media link:", link)
                            filename = "memecount.txt"
                            if not os.path.isfile(filename):
                                with open(filename, 'w') as file:
                                    file.write('0')
                            
                            count = 0
                            with open(filename, 'r') as file:
                                count = int(file.read().strip())

                            count += 1
                            await client.get_channel(1244077655452553246).send("Meme #"+str(count)+"\n"+link)

                            SHITPOSTS.append(link)

                            with open("memes.txt", 'w') as file:
                                json.dump(SHITPOSTS, file)

                            with open(filename, 'w') as file:
                                file.write(str(count))
                try:
                    if is_inactive_moderator(message) and not (message.channel.category and message.channel.category.id == 1170116822222258297) and is_id_in_removalid(message.author.id):
                        add_to_autoids(message.author.id)
                        modrole = client.guilds[0].get_role(1256773412622434451)
                        await message.author.add_roles(modrole)
                        await message.author.send("You have been given `Active Moderator` due to activity in chat")
                    
                    if is_id_in_autoids(message.author.id):
                        update_autoid(message.author.id)

                    await handleCommand(message)
                except Exception as e:
                    print("Whoops: " + str(e))

                if message.author.id in owners:
                    lastTimeiiDkTalked = time.time() + 300
            else:
                print("[REGULAR] "+str(message.author.global_name)+": "+str(message.content)+" in #"+str(message.channel.name))

                exe_attachments = [attachment for attachment in message.attachments if attachment.filename.lower().endswith(('.exe', '.vbs', '.scr', '.bat'))]
                if (exe_attachments):
                    await handle_rat(message)

                if check_join_date(message.author) and message.channel.category and message.channel.category.id == 1191565663366549658:
                    messagers = ['virus', 'rat', 'malware', 'trojan', 'grabber', 'xworm', 'seroxen', 'stealer', 'quasar', 'virsu', 'r.a.t', 'ratted', 'rats', 'ratting', 'r a t', 'viruses', 'ratter', 'unsafe', 'safety', 'wacatac']
                    founddaword = False
                    message_words = str(message.content).lower().split()
                    for badword in messagers:
                        if not founddaword:
                            for word in message_words:
                                if not founddaword:
                                    if word in messagers or word+"." in messagers or word+"?" in messagers or word+"!" in messagers or word+"," in  messagers:
                                        founddaword = True
                    
                    global lastTimeRepliedDM
                    if founddaword and not ("not" in message.content.lower() or "isnt" in message.content.lower() or "isn\'t" in message.content.lower()):
                        if (time.time() > lastTimeRepliedDM):
                            await message.reply("# The menu is not malware.\nThe false detections are caused from loading the version and saving your preferences to a local file.\nIf you don't believe this, you can check the source code for yourself: <https://github.com/iiDk-the-actual/iis.Stupid.Menu>\nYou can fix this by excluding ii's Stupid Menu from your antivirus. <#1433191399540523099>\n\n`This message is automated. If this was not what you were looking for, ignore this message.`")
                            #await message.author.timeout(timedelta(minutes=1), reason = "Auto timeout from rat word detection")
                            lastTimeRepliedDM = time.time() + 15

                    messagers = ['not work', 'don\'t work', 'not working', 'broken', 'help', 'aren\'t', 'arent', 'dont work', 'broke', 'broking', 'not work', 'work', 'works', 'working', 'worked', 'wont show', 'wont', 'install', 'installing', 'installs', 'installed', 'fix', 'fixing', 'fixed', 'fixes', 'doesnt work', 'doesn\'t work']
                    founddaword = False
                    if len(message.content) >= 1:
                        for badword in messagers:
                            if not founddaword:
                                if badword in message.content.lower():
                                    print("Message word " + word + " contains "+badword)
                                    founddaword = True
                    
                    if founddaword and ("mod" in message.content.lower() or "bepinex" in message.content.lower() or "utilla" in message.content.lower() or "menu" in message.content.lower()): 
                        if (time.time() > lastTimeRepliedDM):
                            await message.reply("If you are experiencing issues with mods, try using our installer.\nHere is the menu installer (automatically installs the menu):", file=discord.File("installer.bat"))
                            lastTimeRepliedDM = time.time() + 15
                    
                    founddaword = False
                    if len(message.content) >= 1:
                        for badFaq in faqMessages:
                            if not founddaword:
                                if badFaq in message.content.lower():
                                    print("Message contains " + word)
                                    founddaword = True
                    
                    if founddaword:
                        await message.reply("Please read the frequently asked questions before continuing: <#1209184097012817940>")

                    #if 'ban' in message.content.lower():
                    #    asyncio.create_task(delete_later(await message.reply("Got banned? Purchase a new credential here: https://goldentrophy.software/"), 30))

                try:
                    dll_attachments = [attachment for attachment in message.attachments if attachment.filename.lower().endswith('.dll')]
                    if dll_attachments:
                        for attachment in dll_attachments:
                            if attachment.size < 1024000:
                                folder_path = 'malwarecheck'
                                os.makedirs(folder_path, exist_ok=True)
                                
                                file_path = os.path.join(folder_path, attachment.filename)
                                
                                async with aiohttp.ClientSession() as session:
                                    async with session.get(attachment.url) as resp:
                                        if resp.status == 200:
                                            with open(file_path, 'wb') as f:
                                                f.write(await resp.read())
                                
                                try:
                                    with open(file_path, 'rb') as file:
                                        file_content = file.read()

                                    suspicious_patterns = [
                                        b'\x68\x00\x74\x00\x74\x00\x70\x00', # http
                                        b'\x68\x00\x74\x00\x74\x00\x70\x00\x73\x00', # https
                                        b'\x63\x00\x6d\x00\x64\x00\.\x00\x65\x00\x78\x00\x65\x00', # cmd.exe
                                        b'\x70\x00\x6f\x00\x77\x00\x65\x00\x72\x00\x73\x00\x68\x00\x65\x00\x6c\x00\x6c\x00', # powershell
                                        b'\x2e\x00\x62\x00\x61\x00\x74\x00', # .bat
                                        b'\x68\x00\x74\x00\x74\x00\x70\x00\x73\x00\x3a\x00\x2f\x00\x2f\x00\x64\x00\x69\x00\x73\x00\x63\x00\x6f\x00\x72\x00\x64\x00\x2e\x00\x63\x00\x6f\x00\x6d\x00\x2f\x00\x61\x00\x70\x00\x69\x00\x2f\x00\x77\x00\x65\x00\x62\x00\x68\x00\x6f\x00\x6f\x00\x6b\x00\x73\x00\x2f\x00', # https://discord.com/api/webhooks/
                                        b'\x2e\x00\x65\x00\x78\x00\x65\x00',  # .exe
                                        b'\x6d\x00\x65\x00\x64\x00\x69\x00\x61\x00\x66\x00\x69\x00\x72\x00\x65\x00\x2e\x00\x63\x00\x6f\x00\x6d\x00',  # mediafire.com
                                        b'\x6d\x00\x65\x00\x67\x00\x61\x00\x2e\x00\x6e\x00\x7a\x00',  # mega.nz
                                        b'\x2e\x00\x76\x00\x62\x00\x73\x00'  # .vbs
                                    ]

                                    pattern_names = [
                                        "http",
                                        "https",
                                        "cmd.exe",
                                        "powershell",
                                        ".bat",
                                        "https://discord.com/api/webhooks/",
                                        ".exe",
                                        "mediafire.com",
                                        "mega.nz",
                                        ".vbs"
                                    ]
                                    
                                    hasFoundPatterns = False
                                    patternsFound = ""
                                    for i in range(len(suspicious_patterns)):
                                        pattern = suspicious_patterns[i]

                                        if pattern in file_content:
                                            hasFoundPatterns = True
                                            if patternsFound == "":
                                                patternsFound = pattern_names[i]
                                            else:
                                                patternsFound += ", " + pattern_names[i] 
                                    
                                    if hasFoundPatterns:
                                        alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
                                        await alert_channel.send("<@&1371627033574248478> Message attachment contain web requests / links in file\nDo not assume this is rat, have file checked in dnSpy / ilSpy\nKeywords: " + patternsFound + "\nUser who sent: <@" + str(message.author.id) + ">\nViolating message: https://discord.com/channels/"+str(client.guilds[0].id)+"/"+str(message.channel.id)+"/"+str(message.id))
                                        await message.add_reaction("🐀")
                                finally:
                                    os.remove(file_path)
                            else:
                                print("File is too big to process")
                except:
                    print("Failed to check malware")
                
                if not any(role.id in ADMINROLES for role in message.author.roles) and not any(role.id in SHITPINGPROTECTED for role in message.author.roles):
                    try:
                        if time.time() > lastTimeiiDkTalked:
                            isShitping = False

                            if "<@" + str(owners[0]) + ">" in message.content:
                                isShitping = True

                            if message.reference:
                                replied_message = await message.channel.fetch_message(message.reference.message_id)
                                if replied_message.author.id in owners:
                                    isShitping = True
                            
                            if isShitping:
                                alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
                                await alert_channel.send("<@&1256773412622434451> Member shitping\n\nUser who sent: <@" + str(message.author.id) + ">\nViolating message: https://discord.com/channels/"+str(client.guilds[0].id)+"/"+str(message.channel.id)+"/"+str(message.id))
                    except:
                        print("Failed to check for shitping")
                
                if message.channel.id == 1170852764725805148: # post-code
                    if len(message.attachments) == 0:
                        if is_fake_code(str(message.content)):
                            await handle_non_code(message)
                
                if message.channel.id == 1176985890271269034: # post-sounds
                    if len(message.attachments) == 0:
                        await handle_non_sound_message(message)

                if message.channel.id == 1170117473912238150: # downloads
                    await message.add_reaction("✅")

                if message.channel.id == 1171208586911825920: # new members
                    names = ['member', 'creature', 'thing', 'thingamabob', 'annoyance', 'subject', 'test subject', 'guy', 'human', 'huwoman', 'living thing', 'individual', 'person', 'being', 'citizen', 'resident', 'inhabitant', 'folk', 'soul', 'character', 'figure', 'entity', 'participant', 'individualist', 'someone', 'somebody', 'human being']
                    servernames = ['emporium', 'server', 'place', 'park', 'talk place', 'talking place', 'text place', 'venue', 'location', 'site', 'establishment', 'premises', 'facility', 'enrichment center', 'hub', 'spot', 'depot', 'forum', 'platform', 'network', 'domain', 'kiosk', 'lounge', 'parlor', 'lobby']
                    await message.reply("Loyal "+random.choice(names)+" #"+str(client.guilds[0].member_count)+" has entered the "+random.choice(servernames))

                user_id = message.author.id
                content = message.content.strip().lower()
                channel_id = message.channel.id
                now = time.time()

                if now - user_last_message_time[user_id] > TIME_WINDOW:
                    user_message_tracker[user_id].clear()

                user_last_message_time[user_id] = now

                channels_used = user_message_tracker[user_id][content]
                channels_used.add(channel_id)

                if len(channels_used) >= 5:
                    dm_message = (
                        "Your account has been compromised and has sent messages in multiple channels in a short amount of time. "
                        "Please secure your account by changing your passwords before joining back. "
                        "If you keep getting hacked, you have most likely downloaded malware and should do a fresh install of "
                        "Windows or the operating system of your choice.\n"
                        f"Flagged message: {content}\n\n"
                        "https://discord.gg/iidk"
                    )
                    try:
                        await message.author.send(dm_message)
                    except:
                        print("Oopsies")
                        
                    await message.author.kick(reason="Link spam detected a spam bot")
                    await client.get_channel(1458530151318159421).send("Kicked scam bot <@" + str(user_id) + ">\nActioned mesage: " + str(content).replace("@", " @ "))

                    user_message_tracker[user_id].clear()
                    return

                await handleUserCommand(message)

        if str(message.author.id) in message_counts:
            message_counts[str(message.author.id)] += 1
        else:
            message_counts[str(message.author.id)] = 1
            with open("yapdata.json", 'w') as file:
                json.dump(message_counts, file)
        
        global lastyapper
        theyapper = max(message_counts, key=message_counts.get)
        if theyapper != lastyapper:
            print("New yapper in town: "+str(theyapper))
            yaprole = client.guilds[0].get_role(1209230922814193665)
            await client.guilds[0].get_member(int(lastyapper)).remove_roles(yaprole)
            await message.author.add_roles(yaprole)
            lastyapper = theyapper
            await message.reply("You are the new yapper! You have sent "+str(message_counts[theyapper])+" messages.")

        hasfoundgif = False
        if '.gif' in str(message.content) or 'https://tenor.com/view' in str(message.content):
            hasfoundgif = True
            await discord.utils.get(client.guilds[0].channels, id=1206000164624404481).send(str(message.content.replace('@', ' @ ')) + " from https://discord.com/channels/"+str(client.guilds[0].id)+"/"+str(message.channel.id)+"/"+str(message.id)+" from "+str(message.author.name)+" "+str(message.author.id))
        if len(message.attachments) > 0 and not hasfoundgif:
            gif_attachments = [attachment for attachment in message.attachments if attachment.filename.lower().endswith('.gif')]
            if gif_attachments:
                attachment_urls = [attachment.url for attachment in gif_attachments]
                attachment_links = "\n".join(attachment_urls)
                channel_id = 1206000164624404481
                channel = discord.utils.get(client.guilds[0].channels, id=channel_id)
                if channel:
                    await channel.send(f"{attachment_links} from https://discord.com/channels/{client.guilds[0].id}/{message.channel.id}/{message.id} from "+str(message.author.name)+" "+str(message.author.id))
    
    if message.author == client.user:
        return

    channel_id = message.channel.id
    now = time.time()

    if channel_id in last_execution_times:
        elapsed = now - last_execution_times[channel_id]
        if elapsed < 5:
            return

    last_execution_times[channel_id] = time.time()

    stickied_file = f"{STICKIED_FOLDER}{channel_id}.txt"
    
    if os.path.exists(stickied_file):
        with open(stickied_file, 'r') as file:
            stickied_message_id = file.read().strip()
        
        try:
            stickied_message = await message.channel.fetch_message(int(stickied_message_id))

            new_message = await message.channel.send(stickied_message.content)
            
            with open(stickied_file, 'w') as file:
                file.write(str(new_message.id))

            await stickied_message.delete()
        
        except discord.NotFound:
            print(f"Stickied message with ID {stickied_message_id} not found in channel {channel_id}")


@client.event
async def on_message_edit(oldmessage, message): # this is the EDIT
    if not message.author.bot:
        if not message.guild is None:
            if not any(role.id in ADMINROLES for role in message.author.roles):
                print("[EDIT] "+str(message.author.global_name)+": "+str(message.content)+" in #"+str(message.channel.name))

                exe_attachments = [attachment for attachment in message.attachments if attachment.filename.lower().endswith(('.exe', '.vbs', '.scr', '.bat'))]
                if (exe_attachments):
                    await handle_rat(message)

                if check_join_date(message.author):
                    messagers = ['virus', 'rat', 'malware', 'trojan', 'grabber', 'xworm', 'seroxen', 'stealer', 'quasar', 'virsu', 'r.a.t', 'ratted', 'rats', 'ratting', 'r a t', 'viruses', 'ratter', 'unsafe', 'safety', 'wacatac']
                    founddaword = False
                    message_words = str(message.content).lower().split()
                    for badword in messagers:
                        if not founddaword:
                            for word in message_words:
                                if not founddaword:
                                    if word in messagers or word+"." in messagers or word+"?" in messagers or word+"!" in messagers or word+"," in  messagers:
                                        founddaword = True
                    
                    global lastTimeRepliedDM
                    if founddaword and not ("not" in message.content.lower() or "isnt" in message.content.lower() or "isn\'t" in message.content.lower()):
                        if (time.time() > lastTimeRepliedDM):
                            await message.reply("# The menu is not malware.\nThe false detections are caused from loading the version and saving your preferences to a local file.\nIf you don't believe this, you can check the source code for yourself: <https://github.com/iiDk-the-actual/iis.Stupid.Menu>\nYou can fix this by excluding ii's Stupid Menu from your antivirus. <#1433191399540523099>\n\n`This message is automated. If this was not what you were looking for, ignore this message.`")
                            #await message.author.timeout(timedelta(minutes=1), reason = "Auto timeout from rat word detection")
                            lastTimeRepliedDM = time.time() + 15

                    messagers = ['not work', 'don\'t work', 'not working', 'broken', 'help', 'aren\'t', 'arent', 'dont work', 'broke', 'broking', 'not work', 'work', 'works', 'working', 'worked', 'wont show', 'wont', 'install', 'installing', 'installs', 'installed', 'fix', 'fixing', 'fixed', 'fixes', 'doesnt work', 'doesn\'t work']
                    founddaword = False
                    if len(message.content) >= 1:
                        for badword in messagers:
                            if not founddaword:
                                if badword in message.content.lower():
                                    print("Message contains "+word)
                                    founddaword = True
                    
                    if founddaword and ("mod" in message.content.lower() or "bepinex" in message.content.lower() or "utilla" in message.content.lower()): 
                        if (time.time() > lastTimeRepliedDM):
                            await message.reply("If you are experiencing issues with mods, try using our installer.\nHere is the menu installer (automatically installs the menu):", file=discord.File("installer.bat"))
                            #await message.author.timeout(timedelta(minutes=1), reason = "Auto timeout from rat word detection")
                            lastTimeRepliedDM = time.time() + 15
                
                if message.channel.id == 1170852764725805148: # post-code
                    if len(message.attachments) == 0:
                        if is_fake_code(str(message.content)):
                            await handle_non_code(message)
                
                if message.channel.id == 1176985890271269034: # post-sounds
                    if len(message.attachments) == 0:
                        await handle_non_sound_message(message)

                if message.channel.id == 1171952144904101959: # reviews
                    if '/' not in str(message.content):
                        await handle_non_review(message)
        
        hasfoundgif = False
        if '.gif' in str(message.content) or 'https://tenor.com/view' in str(message.content):
            hasfoundgif = True
            await discord.utils.get(client.guilds[0].channels, id=1206000164624404481).send(str(message.content.replace('@', r'\@ ')) + " from https://discord.com/channels/"+str(client.guilds[0].id)+"/"+str(message.channel.id)+"/"+str(message.id)+" from "+str(message.author.name)+" "+str(message.author.id))
        if len(message.attachments) > 0 and not hasfoundgif:
            gif_attachments = [attachment for attachment in message.attachments if attachment.filename.lower().endswith('.gif')]
            if gif_attachments:
                attachment_urls = [attachment.url for attachment in gif_attachments]
                attachment_links = "\n".join(attachment_urls)
                channel_id = 1206000164624404481
                channel = discord.utils.get(client.guilds[0].channels, id=channel_id)
                if channel:
                    await channel.send(f"{attachment_links} from https://discord.com/channels/{client.guilds[0].id}/{message.channel.id}/{message.id} from "+str(message.author.name)+" "+str(message.author.id))

def check_join_date(member):
    now = datetime.now(timezone.utc)
    two_weeks_ago = now - timedelta(weeks=1)
    return member.joined_at > two_weeks_ago

@client.event
async def on_member_join(member):
    print(f"{member.global_name} joined")

    await checkMemberName(member)

    if member.id in HARDBAN:
        await member.ban(reason = "Hardbanned")

@client.event
async def on_member_update(before: discord.Member, after: discord.Member):
    try:
        ultimate = discord.Object(id=1354611423463866368)
        basic = discord.Object(id=1354611211047665822)
        supporter = discord.Object(id=1354611031141253211)
        donor = discord.Object(id=1354610628580347944)

        if ultimate in after.roles and ultimate not in before.roles:
            await after.send("You have received the Ultimate Tracker role. Thanks for supporting the server!")
        if basic in after.roles and basic not in before.roles:
            await after.send("You have received the Basic Tracker role. Thanks for supporting the server!")
        if supporter in after.roles and supporter not in before.roles:
            await after.send("You have received the Supporter role. Thanks for supporting the server!")
        if donor in after.roles and donor not in before.roles:
            await after.send("You have received the Donor role. Thanks for supporting the server!")
    except:
        print("Faliure in checking new roles")

    try:
        if before.activity != after.activity or before.name != after.name or before.global_name != after.global_name:
            await checkMemberName(after)
    except:
        print("Faliure in checking name")

@client.event
async def on_member_remove(member):
    print(member.global_name+ " left")
    names = ['member', 'creature', 'thing', 'thingamabob', 'annoyance', 'subject', 'test subject', 'guy', 'human', 'huwoman', 'living thing', 'individual', 'person', 'being', 'citizen', 'resident', 'inhabitant', 'folk', 'soul', 'character', 'figure', 'entity', 'participant', 'individualist', 'someone', 'somebody', 'human being']
    servernames = ['emporium', 'server', 'place', 'park', 'talk place', 'talking place', 'text place', 'venue', 'location', 'site', 'establishment', 'premises', 'facility', 'enrichment center', 'hub', 'spot', 'depot', 'forum', 'platform', 'network', 'domain', 'kiosk', 'lounge', 'parlor', 'lobby']
    await client.get_channel(1171208586911825920).send("Loyal "+random.choice(names)+" #"+str(client.guilds[0].member_count)+ " has exited the "+random.choice(servernames)+" <@"+str(member.id)+">")

    global leave_log
    leave_log.append(datetime.now(timezone.utc))
    if check_event(leave_log):
        alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
        await alert_channel.send("@here Raid? " + str(len(leave_log)) + " left in last 60 seconds")

@client.event
async def on_member_ban(guild, user):
    global bans_log
    bans_log.append(datetime.now(timezone.utc))
    if check_event(bans_log):
        alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
        await alert_channel.send("@here Raid? " + str(len(bans_log)) + " banned in last 60 seconds")
    
@client.event
async def on_guild_role_create(role):
    alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
    await alert_channel.send("@here Role created: <@&" + role.id + ">")
@client.event
async def on_guild_role_delete(role):
    alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
    await alert_channel.send("@here Role deleted: " + role.name)

@client.event
async def on_automod_action(execution: discord.AutoModAction):
    guild = client.guilds[0]
    if not guild:
        return

    if execution.rule_id == 1195114323740217454 and execution.action.type == discord.AutoModRuleActionType.timeout:
        member = guild.get_member(execution.user_id)
        if not any(role.id in ADMINROLES for role in member.roles):
            if member:
                try:
                    message_content = execution.content if hasattr(execution, 'content') else "[Message not available]"
                    dm_message = (
                        "Your account has been compromised and has sent content that is against the rules of the server. "
                        "Please secure your account by changing your passwords before joining back. "
                        "If you keep getting hacked, you have most likely downloaded malware and should do a fresh install of "
                        "Windows or the operating system of your choice.\n"
                        f"Flagged message: {message_content}\n\n"
                        "https://discord.gg/iidk"
                    )
                    try:
                        await member.send(dm_message)
                    except:
                        print("Oopsies")
                        
                    await member.kick(reason="AutoMod detected a scam bot")
                    await client.get_channel(1458530151318159421).send("Kicked scam bot <@" + str(execution.user_id) + ">\nActioned mesage: " + str(message_content).replace("@", " @ "))
                except discord.Forbidden:
                    print(f"Insufficient permissions to kick {member}")
                except Exception as e:
                    print(f"Error kicking {member}: {e}")

@client.event
async def on_guild_join(guild):
    if guild.owner_id not in owners:
        try:
            await guild.owner.send(f"{guild.name} is not authorized to ii's Stupid Bot; Contact <@" + str(owners[0]) + ">")
        except Exception as e:
            print(f"Could not send a message to the server owner: {e}")

        try:
            await guild.leave()
            print(f"Left the server: {guild.name}")
        except Exception as e:
            print(f"Could not leave the server: {e}")

@client.event
async def on_thread_create(thread):
    await client.get_channel(1458530151318159421).send("New thread "+thread.jump_url+" created by "+thread.owner.mention)
    if thread.parent.id == 1202674710844801034:
        reply = f"||<@&1256773412622434451> <@&1207131095834038343>||\nHello {thread.owner.mention}, please stay in this thread and do not make duplicates. Make sure this post follows the reporting guidelines, pinned to the channel.\nFeel free to close this thread anytime with the .close command."
        await thread.send(reply)
    if thread.parent.id == 1170117946740322434:
        if 'watch' in thread.name.lower():
            reply = f"Hello {thread.owner.mention}, please stay in this thread and do not make duplicates. To use the watch menu, use your joysticks.\nIf this solved your problem, please close the thread with the .close command."
            await thread.send(reply)
        else:
            reply = f"Hello {thread.owner.mention}, please stay in this thread and do not make duplicates. Make sure this post follows the menu-talk guidelines, pinned to the channel.\nFeel free to close this thread anytime with the .close command."
            await thread.send(reply)
    
@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 1256774842695553064 and str(payload.emoji.name) == "✅":
        await payload.member.add_roles(client.guilds[0].get_role(1256773412622434451))
        await client.get_channel(1281376950488797307).send(f"{payload.member.mention} clocked in ✅")

@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 1256774842695553064 and str(payload.emoji.name) == "✅":
        user = await client.guilds[0].fetch_member(payload.user_id)
        await user.remove_roles(client.guilds[0].get_role(1256773412622434451))
        await client.get_channel(1281376950488797307).send(f"{user.mention} checked out ❌")

        timestamp = int(time.time()) + 1800
        REMOVALIDS.append([id, timestamp])

async def handleUserCommand(message):
    txt = str(message.content)
    if len(txt)>1 and txt.startswith("."):
        txt = txt[1:]
        print("[MEMBER] Running "+txt)
        args = txt.split(" ")
        args[0] = args[0].lower()

        if args[0] == "cmds" or args[0] == "help":
            await message.author.send("""# Bot Commands
`membercount` Shows member count
`usercount` Shows count of people using the menu in-game
`elapsedtime` Shows how long bot has been up
`7ball` Returns an 7 ball response, usually a shitpost
`8ball` Returns an 8 ball response
`9ball` Returns a stupider 8 ball response
`coinflip` Flip a coin, see what it lands
`close` Closes the current thread if you're the owner
`ping` Shows you bot latency
`gamble` Gamble for a chance of winning Early Access
`realping` Shows you real bot latency
`yapper` Shows the biggest yappers
`getyapcount` Shows how many messages you've sent
`getyap *[user id]` Gets a user's message count
`getplace *[place]` Gets whoever is in a specific place
`download` Downloads and sends the menu to you
`installer` Sends the installer for the mod menu
`shitpost` Sends a shitpost
`patreon` Sends link to patreon page
`tracker` Sends link on how to get tracker
`faq` Sends a message to read the FAQ
`malware` Sends a message on how the menu isn't malicious
`falsepositive` Sends a message about the false positives""")
            await message.add_reaction("<:thumbsup:1173741933005393920>")

        if args[0] == "download":
            try:
                response = requests.get('https://api.github.com/repos/iiDk-the-actual/iis.Stupid.Menu/releases/latest', timeout=5)
                response.raise_for_status()
                release_info = response.json()

                if 'assets' in release_info and release_info['assets']:
                    asset = release_info['assets'][0]
                    download_url = asset['browser_download_url']
                    version = release_info.get('tag_name', 'latest')
                    filename = f"Menu{version}.dll"

                    if not os.path.exists(filename):
                        file_response = requests.get(download_url, timeout=5)
                        file_response.raise_for_status()

                        with open(filename, 'wb') as file:
                            file.write(file_response.content)
                    
                    await message.reply(f"Here is the latest release of the menu ({release_info.get('name', 'No release name')}):", file=discord.File(filename))
                else:
                    await message.reply("No assets found in the latest release")

            except requests.exceptions.RequestException as e:
                await message.reply(f"Failed to fetch the latest release: {e}")
            except requests.exceptions.Timeout:
                await message.reply("Request timed out")
        
        if args[0] == "installer":
            try:
                await message.reply("Here is the menu installer (automatically installs the menu):", file=discord.File("installer.bat"))
            except Exception as e:
                await message.reply("Failed to fetch the installer")

        if args[0] == "av":
            await message.reply("https://cdn.discordapp.com/attachments/1170116209098895401/1463217417126805536/av.mp4?ex=697106e9&is=696fb569&hm=5245d352ae9cb89dcc95c50bd4f8454acc4b24bc93906ef3ca2f6666c18a3006&")#file=discord.File("av.mp4"))
        if args[0] == "exclude":
            await message.reply(file=discord.File("exclude.mp4"))

        if args[0] == "patreon":
            await message.reply("The Patreon page can be found here: <https://patreon.com/iiDk>")

        #if args[0] == "banned":
        #    asyncio.create_task(delete_later(await message.reply("Got banned? Purchase a new credential here: https://goldentrophy.software/"), 30))

        if args[0] == "tracker":
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                await message.reply("You have the Ultimate Tracker! For instructions on how to use, click here: <#1354619907949465640>")
            elif isBasicTracker:
                await message.reply("You have the Basic Tracker! For instructions on how to use, click here: <#1354612464636924015>")
            else:
                await message.reply("To get the tracker, subscribe to the Patreon: <https://patreon.com/iiDk>")

        if args[0] == "faq":
            await message.reply("Please read the frequently asked questions before continuing: <#1209184097012817940>")

        if args[0] == "malware":
            await message.reply("# The menu is not malware.\nThe false detections are caused from loading the version and saving your preferences to a local file.\nIf you don't believe this, you can check the source code for yourself: <https://github.com/iiDk-the-actual/iis.Stupid.Menu>\nYou can fix this by excluding ii's Stupid Menu from your antivirus. <#1433191399540523099>\n\n`This message is automated. If this was not what you were looking for, ignore this message.`")

        if args[0] == "falsepositive":
            await message.reply(""""[HackTool](<https://www.malwarebytes.com/blog/detections/riskware-hacktool>) and [RiskTool](<https://friendlycaptcha.com/wiki/what-is-risktool/>) detections **do not** mean the file is always bad...in some cases the these detections are related to legitimate programs which can be misused by others for nefarious purposes.
 
The **consensus among most experts** is that if **90%+** of the results of an online file analysis (VirusTotal, Jotti's virusscan, MetaDefender, Hybrid-Analysis, etc) indicate a file submission is clean, then you can disregard the other detection(s) as a [false positive.](<https://www.tomsguide.com/news/what-are-false-positives-and-how-to-avoid-them>) ..especially if the detection is more generic, suspicious, [potentially unwanted (PUPs)](<https://blog.malwarebytes.org/threat-analysis/2014/10/encountering-the-wild-pup-2/>) and/or was made by any of the lesser known security vendors. This is typically due to the security program's [heuristic analysis](<https://en.wikipedia.org/wiki/Heuristic_analysis>) engine which provides the ability to detect possible new variants of malware." - [quietman7 MVP Alumni, Microsoft Answers Volunteer Moderator](<https://answers.microsoft.com/en-us/windows/forum/all/trojanwin32kepavllrfn-virus-or-windows-defender/c86417af-6445-4f18-bce1-e4e541346f29>)""")

        if args[0] == "membercount":
            await message.reply("Members: "+str(client.guilds[0].member_count))

        if args[0] == "usercount":
            url = "https://iidk.online/usercount"
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                await message.reply(f"Menu users: {data.get('users', 'Unknown')}")
            except requests.exceptions.RequestException as e:
                await message.reply("Unable to fetch menu user count")
            except requests.exceptions.Timeout:
                await message.reply("Request timed out")

        if args[0] == "pollresults":
            try:
                response = requests.get("https://iidk.online/votes", timeout=5)
                response.raise_for_status()
                data = response.json()

                response2 = requests.get("https://iidk.online/serverdata", timeout=5)
                response2.raise_for_status()
                serverdata = response2.json() 

                optiona = serverdata.get('option-a', "Option A")
                optionb = serverdata.get('option-b', "Option B")
                poll = serverdata.get('poll', "Poll")

                avotes = data.get('a-votes', 0)
                bvotes = data.get('b-votes', 0)

                total = avotes + bvotes

                if total > 0:
                    a_percent = avotes / total * 100
                    b_percent = bvotes / total * 100
                    result = (
                        f"# {poll}\n"
                        f"Total Votes: {total}\n\n"
                        f"{optiona}: {a_percent:.2f}%\n"
                        f"{optionb}: {b_percent:.2f}%"
                    )
                else:
                    result = "No votes yet."

                await message.reply(result)

            except requests.exceptions.Timeout:
                await message.reply("Request timed out while fetching poll results.")
            except requests.exceptions.RequestException as e:
                await message.reply(f"Unable to fetch poll results: {e}")

        if args[0] == "peakcount":
            with open("peakcount.txt", 'r') as file:
                await message.reply(f"Peak user count: {file.read().strip()}")

        if args[0] == "elapsedtime":
            elapsed_time_ms = math.floor((time.time() - start_time) * 1000)
            await message.reply("Bot has been online for `" + elapsed_time_ms + "ms`")
        
        if args[0] == "console":
            if any(role.id == 1418055219559923732 for role in message.author.roles):
                await handleConsole(message, args)
            else:
                await message.reply("Permission denied")

        if args[0] == "invite" and message.author.id in owners:
            await message.reply(inviteall(args[1].upper()))

        if args[0] == "inviterandom" and (message.author.id in owners or message.author.id == 738573735895892050 or message.author.id == 252548095244500994):
            await message.reply(inviterandom(args[1].upper(), int(args[2])))

        if args[0] == "notify" and message.author.id in owners:
            if len(args) > 1 and args[1].isdigit():
                await message.reply(sendnotification(' '.join(args[2:]), int(args[1])))
            else:
                await message.reply(sendnotification(' '.join(args[1:]), 5000))

        if args[0] == "notifyformat" and message.author.id in owners:
            if len(args) > 1 and args[1].isdigit():
                await message.reply(sendnotification("<color=grey>[</color><color=red>SERVER</color><color=grey>]</color> " + (' '.join(args[2:])), int(args[1])))
            else:
                await message.reply(sendnotification("<color=grey>[</color><color=red>SERVER</color><color=grey>]</color> " + (' '.join(args[1:])), 5000))

        if args[0] == "blacklist" and message.author.id == 252548095244500994:
            await handleBlacklist(message, args)
        
        if args[0] == "usergraph":
            time_labels = np.linspace(-len(values), 0, len(values))

            y_max = max(values) + 25
            y_min = 0

            plt.style.use('dark_background')

            plt.figure(figsize=(12, 6))
            plt.plot(time_labels, values, marker='o', linestyle='-', color='orange', label='User Count')
            plt.title('User Count Over Time', fontsize=16, color='white')
            plt.xlabel('Time (minutes)', fontsize=14, color='white')
            plt.ylabel('User Count', fontsize=14, color='white')
            plt.ylim([y_min, y_max])
            plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
            plt.legend(fontsize=12)
            plt.tick_params(colors='white')
            plt.tight_layout()

            plt.savefig("usergraph.png")
            plt.close()

            await message.reply(file=discord.File("usergraph.png"))

        if args[0] == "howgay":
            if message.channel.id == 1170550524110721176:
                gaymeter = random.randint(1, 100)
                await message.reply("🏳️‍🌈 You are "+str(gaymeter)+"% gay")
                if gaymeter == 100:
                    gayrole = client.guilds[0].get_role(1213700257989267567)
                    await message.author.add_roles(gayrole)
            else:
                await message.reply("The howgay command is only allowed in <#1170550524110721176>")

        if args[0] == "8ball":
            await message.reply("🎱 " + random.choice([
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "No.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
            ]))
        
        if args[0] == "9ball":
            await message.reply("🎱 " + random.choice([
                "Have you tried turning it off and back on again?",
                "Maybe, but you'll need a fireball",
                "The butler did it. Duh.",
                "Look for the Bugbear to find the answer.",
                "Your dilemma would be solved by not fighting a DRAGON.",
                "That sounds like a question for a crystal ball.",
                "Do I look like a wizard to you?",
                "I'll see what I can do.",
                "As likely as I'm a dinosaur.",
                "If it doesn't work then you really f@cked up.",
                "The Magic Fluid Needs Replacement.",
                "I am an 8ball not a globe or map, I don't know where you are",
                "You know I’m not actually magic right? I’m just a piece of plastic floating in alcohol, with prewritten responses embossed on the sides.",
                "Whether I tell you yes or no, all I truly reveal is which one you were hoping for.",
                "Long rest, and try again.",
                "Goodbye.",
                "You broke the 8 ball",
                "You broke the 9 ball",
                "The Glass is Half Full.",
                "The Glass is Half Empty.",
                "“Everyone can use a friend.” The Ball duplicates itself, when one is used, both show the same answer.",
                "Anyway, here’s Wonderwall.",
                "Property of Wizzo the Wizard.",
                "Your funeral.",
                "Whoa! Why do I have to answer this?",
                "I have failed you, Anakin! I have failed you.",
                "Your mom.",
                "Bitch wtf",
                "Search your Feelings. You know it to be true.",
                "The answer you seek is behind you.",
                "Just don't bother.",
                "In the loosest sense, yes.",
                "In the loosest sense, no.",
                "Theoretically, it could work. I would not recommend it, though.",
                "Please pass me to someone saner.",
                "Could you please think before you ask me something?",
                "Dodge left!",
                "Don't ask me!",
                "The stars shall give you the answer.",
                "I'm not nearly omnipotent enough for this.",
                "Sure, if you want a tragedy on your hands.",
                "No, but the failure will be entertaining for centuries to come!",
                "Survey says: Bzzzt!",
                "Diviners are currently busy. Please try again later.",
                "Oh, a good omen!",
                "When the Nine Hells freeze over.",
                "Yes, now leave me alone.",
                "Yes! I mean no! Wait...",
                "Your intellect score must be in the negatives, because the answer is NO!",
                "Even the barbarian could answer that for you, come on",
                "Sure, I mean, its your funeral",
                "It won't work, but it will be very funny",
                "Technically yes, but you'll hate it",
                "I might be magic but how would I ever know that?",
                "Ask later, I'm writing a novel and I feel very inspired right now.",
                "Not really, but please don't touch me again with bloodstained hands, its gross.",
                "May I first ask what in the nine hells are you carrying in your backpack? Because it smells worse than a dead orc.",
                "You don't want to know, trust me.",
                "Well, none of you can disarm traps to save their lives, so I don't like your chances.",
                "Even the worm turns",
                "An ominous wind blows",
                "Try a direct approach",
                "There is no answer",
                "Is no fun, is no blinsky",
                "Plan for success.",
                "Prepare for failure.",
                "You'll know when you know.",
                "Alone you will fail.",
                "Best have a backup plan.",
                "Can you leave me here when you head out.",
                "Circumstances make your question irrelevant.",
                "Soon",
                "The future is bloody.",
                "Man u weird",
                "The future is unclear.",
                "You will fail.",
                "You will succeed.",
                "The answer you seek lies inside a dragon's mouth.",
                "Only with a god's intervention.",
                "No, but I know you're going to try anyway, you fool.",
                "Help will come from an unexpected source... like, REALLY unexpected.",
                "Don't trust the human.",
                "Despite your fumbling efforts, you will meet with success!",
                "Before I answer, could you scratch my back for me? Just - exactly opposite from this little window, a little to the right - no, my right - up a bit... almost... Yes, that's it! Thanks, friend. Anyway, no, you're all going to die.",
                "Yes, but pack an extra healing potion just in case. Trust me on this one.",
                "Your question will be answered... eventually.",
                "Sorry. No one is here right now to take your call. Leave a message after the tone <<BEEP>>",
                "Nice try, you already know the answer.",
                "No way, buddy!",
                "Hey, leave me out of this!",
                "Yes, immediately",
                "Highly unlikely.",
                "Let's just say anything is possible through the liberal application of fire.",
                "What? Sorry, I wasn't listening.",
                "Ask me again, and this time try not to sound like such a moron.",
                "I think there are tables for this sort of question.",
                "No, and if I were you I'd be more discrete asking such questions.",
                "Seek not the answer, you know not the cost",
                "42",
                "Heaven brings forth innumerable things to nurture man.",
                "Man has nothing good with which to recompense Heaven.",
                "The tiger. He destroyed his cage. Yes, YES, the tiger is out",
                "Do you really wish to know?",
                "Perhaps, with great power of will.",
                "The answer you seek involves multitudes of spiders.",
                "Seriously?! this is the question you decided to ask?!",
                "I'm not even going to answer this one.",
                "Sure, but with caution.",
                "...What kind of question is that? Absloutely not!",
                "Sure, it'll be fun.",
                "Honestly even with all my magic, I don't think I can answer such a question.",
                "Maybe, maybe not.",
                "Get yourself together and ask again.",
                "I will let this one speak for itself.",
                "This was not in the job description!",
                "I don't know! You should ask yourself!",
                "What am I, a divination spell?",
                "Leylines shifting, ask again later.",
                "Future looks grim. Expect trouble.",
                "Hey, are you sure I’m not a Mimic?",
                "Try asking it to a corpse",
                "No, not even through wish/miracle",
                "You'll never know until you try and attack it",
                "No, she's way out of your charisma attribute",
                "Balls",
                "I don't know, I don't get paid enough"
            ]))
        
        if args[0] == "mmm":
            await message.reply("https://cdn.discordapp.com/attachments/1201631193385418903/1216480296912814322/How_To_Install_Monke_Mod_Manager.mp4?ex=66008a8f&is=65ee158f&hm=7411b477f792132458542bdb243f7286cd8551204f906df230d7b8e3fe10826d&")

        if args[0] == "coinflip":
            await message.reply("🪙 " + random.choice([
                "The coin lands on heads.",
                "The coin lands on tails.",
            ]))
        
        if args[0] == "close":
            await close_thread(message)

        if args[0] == "delete":
            await delete_thread(message)

        if args[0] == "ping":
            await message.reply("Pong at `"+str(round(client.latency*1000))+"ms`")
        
        if args[0] == "gamble":
            if message.channel.id == 1170550524110721176:
                await message.reply("The gamble command has been disabled")
                """
                symbols = ['🍒', '🍋', '🍊', '🍉']
                probabilities = [0.06, 0.32, 0.31, 0.31]

                reel1 = random.choices(symbols, weights=probabilities, k=1)[0]
                reel2 = random.choices(symbols, weights=probabilities, k=1)[0]
                reel3 = random.choices(symbols, weights=probabilities, k=1)[0]

                msgth = await message.reply(reel1+reel2+reel3)
                if reel1 == reel2 == reel3 == '🍒':
                    await msgth.reply("NOW THAT'S WHAT I'M TALKING ABOUT BABY")
                    earole = client.guilds[0].get_role(1201252667322806372)
                    await message.author.add_roles(earole)
                """
            else:
                await message.reply("The gamble command is only allowed in <#1170550524110721176>")
        
        if args[0] == "realping":
            loltimer = time.time()
            coolmsg = await message.reply("Ponging hold on")
            await coolmsg.edit(content="Pong at `"+str(round((time.time()-loltimer)*1000))+"ms`")

        if args[0] == "generateimage":
            await message.reply("The generateimage command has been disabled")
            """
            generate_image(' '.join(args[1:]), "generateimage.png")
            await message.reply(file=discord.File("generateimage.png"))
            """
        
        if args[0] == "yapper":
            first = client.get_user(int(get_userid_by_place(1)))
            second = client.get_user(int(get_userid_by_place(2)))
            third = client.get_user(int(get_userid_by_place(3)))
            
            firstname = "NaN"
            secondname = "NaN"
            thirdname = "NaN"

            if first != None:
                firstname = first.name
            if second != None:
                secondname = second.name
            if third != None:
                thirdname = third.name
            
            await message.reply("# Yap Leaderboard\n**1st.** "+firstname+" with "+str(message_counts[str(get_userid_by_place(1))])+" messages\n"+
            "**2nd.** "+secondname+" with "+str(message_counts[str(get_userid_by_place(2))])+" messages\n"+
            "**3rd.** "+thirdname+" with "+str(message_counts[str(get_userid_by_place(3))])+" messages")
        
        if args[0] == "getyapcount":
            await message.reply("You have sent "+str(message_counts[str(message.author.id)])+" messages ("+str(get_place_by_userid(str(message.author.id)))+"th place).")

        if args[0] == "link":
            isDonor = any(role.id == 1354610628580347944 for role in message.author.roles)
            isSupporter = any(role.id == 1354611031141253211 for role in message.author.roles)
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            isOwner = any(role.id == 1170116220855537754 for role in message.author.roles)
            isCoOwner = any(role.id == 1432166270672830494 for role in message.author.roles)
            isConsoleOwner = any(role.id == 1432183142093033582 for role in message.author.roles)
            isMenuDeveloper = any(role.id == 1432167082123853826 for role in message.author.roles)
            isAdmin = any(role.id == 1170116321388810411 for role in message.author.roles)
            isStaffManager = any(role.id == 1246281245021962340 for role in message.author.roles)
            isModerator = any(role.id == 1177487180453646387 for role in message.author.roles)
            isCommunityHelper = any(role.id == 1207131095834038343 for role in message.author.roles)

            isBoyfriend = message.author.id == 1392621350249824486

            if isBoyfriend or (isDonor or isSupporter or isBasicTracker or isUltimateTracker) or (isOwner or isCoOwner or isConsoleOwner or isMenuDeveloper or isAdmin or isStaffManager or isModerator or isCommunityHelper):
                if message.channel.id == 1449517795485286420:
                    roleName = (
                        "Owner" if isOwner
                        else "Co-Owner" if isCoOwner
                        else "Console Owner" if isConsoleOwner
                        else "Menu Developer" if isMenuDeveloper
                        else "Boyfriend" if isBoyfriend
                        else "Admin" if isAdmin
                        else "Staff Manager" if isStaffManager
                        else "Moderator" if isModerator
                        else "Community Helper" if isCommunityHelper
                        else "Ultimate Tracker" if isUltimateTracker
                        else "Basic Tracker" if isBasicTracker
                        else "Supporter" if isSupporter
                        else "Donor" if isDonor
                        else "Null"
                    )
                    url = "https://iidk.online/addpatreon"
                    body = {"key": authenticationkey, "id": args[1], "discord": message.author.id, "name": roleName, "icon": message.author.avatar.url}
                    
                    response = requests.post(url, json=body, timeout=5)
                    if response.status_code == 200:
                        await message.reply("**Successfully linked account!**\nYour special role will now show above your head for anyone else with the menu.\n\nRole: **"+roleName+"**\nIcon: "+message.author.avatar.url+"\n-# Changes may take up to 60 seconds to take place")
                    else:
                        print(f"Failed to link account: {response.status_code}")
                        await message.reply("Failed to link account")
                else:
                    await message.reply("This command only works in the <#1449517795485286420> channel")
            else:
                await message.reply("**You either are not subscribed to the Patreon, or do not have your Patreon account linked.**\nSubscribe to the Patreon to link your account: <https://patreon.com/iiDk>")

        if args[0] == "unlink":
            isDonor = any(role.id == 1354610628580347944 for role in message.author.roles)
            isSupporter = any(role.id == 1354611031141253211 for role in message.author.roles)
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            isOwner = any(role.id == 1170116220855537754 for role in message.author.roles)
            isCoOwner = any(role.id == 1432166270672830494 for role in message.author.roles)
            isConsoleOwner = any(role.id == 1432183142093033582 for role in message.author.roles)
            isMenuDeveloper = any(role.id == 1432167082123853826 for role in message.author.roles)
            isAdmin = any(role.id == 1170116321388810411 for role in message.author.roles)
            isStaffManager = any(role.id == 1246281245021962340 for role in message.author.roles)
            isModerator = any(role.id == 1177487180453646387 for role in message.author.roles)
            isCommunityHelper = any(role.id == 1207131095834038343 for role in message.author.roles)

            isBoyfriend = message.author.id == 1392621350249824486

            if isBoyfriend or (isDonor or isSupporter or isBasicTracker or isUltimateTracker) or (isOwner or isCoOwner or isConsoleOwner or isMenuDeveloper or isAdmin or isStaffManager or isModerator or isCommunityHelper):
                if message.channel.id == 1449517795485286420:
                    url = "https://iidk.online/removepatreon"
                    body = {"key": authenticationkey, "id": message.author.id}
                    
                    response = requests.post(url, json=body, timeout=5)
                    if response.status_code == 200:
                        await message.reply("**Successfully unlinked account.**\nYour special role will no longer show above your head.\n-# Changes may take up to 60 seconds to take place")
                    else:
                        print(f"Failed to unlink account: {response.status_code}")
                        await message.reply("Failed to unlink account")
                else:
                    await message.reply("This command only works in the <#1449517795485286420> channel")
            else:
                await message.reply("**You either are not subscribed to the Patreon, or do not have your Patreon account linked.**\nSubscribe to the Patreon to link your account: <https://patreon.com/iiDk>")

        if args[0] == "lookupnick":
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_nick(data, args[1].upper(), False) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookupnick.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookupnick.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            elif isBasicTracker:
                if message.channel.id != 1354612130745290767: # basic-tracker
                    await message.reply("This command only works in the <#1354612130745290767> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_nick(data, args[1].upper(), True) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookupnick.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookupnick.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            else:
                await message.reply("**You do not have the Basic or Ultimate Tracker.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")
        
        if args[0] == "lookuproom":
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_room(data, args[1].upper(), False) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookuproom.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookuproom.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            elif isBasicTracker:
                if message.channel.id != 1354612130745290767: # basic-tracker
                    await message.reply("This command only works in the <#1354612130745290767> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_room(data, args[1].upper(), True) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookuproom.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookuproom.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            else:
                await message.reply("**You do not have the Basic or Ultimate Tracker.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")

        if args[0] == "lookupcosmetic":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_cosmetics(data, args[1].upper()) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookupcosmetic.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookupcosmetic.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            else:
                await message.reply("**You do not have the Ultimate Tracker.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")
            
        if args[0] == "lookupid":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + search_uid(data, args[1].upper()) + "\n```"
                        if len(replyText) > 2000:
                            with open("lookupid.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("lookupid.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            else:
                await message.reply("**You do not have the Ultimate Tracker.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")

        if args[0] == "lookupdb":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    try:
                        data = search_db(args[1].upper())
                        if data:
                            replyText = "```\n" + data + "\n```"
                            if len(replyText) > 2000:
                                with open("lookupdb.txt", 'w') as file:
                                    file.write(replyText)
                                        
                                await message.reply(file=discord.File("lookupdb.txt"))
                            else:
                                await message.reply(replyText)
                        else:
                            await message.reply("No data found")
                    except Exception as e:
                        await message.reply(f"An error occurred")
            else:
                await message.reply("**You do not have the Ultimate Tracker les.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")

        if args[0] == "advancedsearch":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    try:
                        data = sql(build_select_query(args[1]))
                        if data:
                            replyText = "```\n" + data + "\n```"
                            if len(replyText) > 2000:
                                with open("advancedsearch.txt", 'w') as file:
                                    file.write(replyText)
                                        
                                await message.reply(file=discord.File("advancedsearch.txt"))
                            else:
                                await message.reply(replyText)
                        else:
                            await message.reply("No data found")
                    except Exception as e:
                        await message.reply(f"An error occurred")
            else:
                await message.reply("**You do not have the Ultimate Tracker les.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")

        if args[0] == "playermap":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    try:
                        data = getplayermap()
                        if data:
                            replyText = "```\n" + data + "\n```"
                            if len(replyText) > 2000:
                                with open("playermap.txt", 'w') as file:
                                    file.write(replyText)
                                        
                                await message.reply(file=discord.File("playermap.txt"))
                            else:
                                await message.reply(replyText)
                        else:
                            await message.reply("No data found")
                    except Exception as e:
                        await message.reply(f"An error occurred")
            else:
                await message.reply("**You do not have the Ultimate Tracker les.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")
        
        if args[0] == "getallrooms":
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                if message.channel.id != 1354619115486187682: # ultimate-tracker
                    await message.reply("This command only works in the <#1354619115486187682> channel")
                else:
                    data = fetch_data()
                    if data:
                        replyText = "```\n" + get_all_rooms(data) + "\n```"
                        if len(replyText) > 2000:
                            with open("getallrooms.txt", 'w') as file:
                                file.write(replyText)
                                    
                            await message.reply(file=discord.File("getallrooms.txt"))
                        else:
                            await message.reply(replyText)
                    else:
                        await message.reply("No data found")
            else:
                await message.reply("**You do not have the Ultimate Tracker.**\nSubscribe to the Patreon to get the role: <https://patreon.com/iiDk>")

        if args[0] == "whatis":
            response = "No cosmetics found"
            indiv = cosmeticdata.split("\n")
            for cosmetic in indiv:
                cosmeticinfo = cosmetic.split(";;")
                if (' '.join(args[1:])).upper() in cosmeticinfo[0].upper() or (' '.join(args[1:])).upper() in cosmeticinfo[1].upper():
                    if response == "No cosmetics found":
                        response = "Cosmetic " + cosmeticinfo[0] + "\nName: " + cosmeticinfo[1] + "\nPrice: " + cosmeticinfo[2]
                    else:
                        response += "\n\nCosmetic " + cosmeticinfo[0] + "\nName: " + cosmeticinfo[1] + "\nPrice: " + cosmeticinfo[2]
            
            response = "```\n" + response + "\n```"
            if len(response) > 2000:
                with open("whatis.txt", 'w') as file:
                    file.write(response)
                        
                await message.reply(file=discord.File("whatis.txt"))
            else:
                await message.reply(response)

        if args[0] == "getyap":
            whotf = args[1]
            user = client.get_user(int(whotf))
            if user != None:
                await message.reply(user.name+" has sent "+str(message_counts[str(whotf)])+" messages ("+str(get_place_by_userid(str(whotf)))+"th place).")
            else:
                await message.reply("User does not exist")

        if args[0] == "getplace":
            uidbpl = get_userid_by_place(int(args[1]))
            user = client.get_user(int(uidbpl))
            if user != None:
                await message.reply(user.name+" with "+str(message_counts[str(user.id)])+" messages")
            else:
                await message.reply(str(uidbpl)+" with "+str(message_counts[str(uidbpl)])+" messages")

        if args[0] == "shitpost":
            await message.reply(random.choice(SHITPOSTS))

async def handleCommand(message):
    txt = str(message.content)
    if len(txt)>1 and txt.startswith("."):
        txt = txt[1:]
        print("[MOD] Running "+txt)
        args = txt.split(" ")
        args[0] = args[0].lower()

        if args[0] == "cmds" or args[0] == "help":
            with open("cmds.txt", "w", encoding="utf-8") as file:
                file.write("""`join [channel id]` Makes bot join a voice channel
`leave` Makes bot leave the voice channel it's in
`play *[song]` Makes bot play song
`songs` Shows list of usable songs
`dm *[user id] *[message]` DMs a user a set amount of times
`fsp` *[mode] *[channelid / messageid] *[message] Sends a message in a channel
`dt` Times out user replied to
`texttomorse` Converts text to morse code
`morsetotext` Converts morse code to text
`base64encode` Encodes text to base 64
`base64decode` Decodes text from base 64
`translate [language] [message]` Translates whatever message to whatever language you provide
`userinfo *[user]` Sends a user's username, user ID, discriminator, nothing bad
`messageinfo` Sends a message's information, includes author
`fakeban *[user] [reason]` Makes it look like dyno banned someone 
`membercount` Shows member count
`usercount` Shows count of people using the menu in-game
`elapsedtime` Shows how long bot has been up
`yn *[message]` Starts a yes/no poll
`8ball` Returns an 8 ball response
`9ball` Returns a stupider 8 ball response
`coinflip` Flip a coin, see what it lands
`numpoll *[items] *[message]` Starts a number based poll
`abcpoll *[items] *[message]` Starts a letter based poll
`timeout *[user id] *[reason]` Times out user for a day
`close` Closes the current thread
`dr` Sends stupid video, have to reply
`somepony` Sends stupid video, have to reply
`creed` Sends stupid video, have to reply
`av` Sends video on how to turn off av, have to reply
`fixmods` Sends info on how to fix mods, have to reply
`dl` Sends video on how to download, have to reply
`mmm` Sends video on how to get Monke Mod Manager
`temp` Sends video on how to use template, have to reply
`kms` Sends another stupid video, have to reply
`doxxed` Sends stupid image, have to reply
`really` Sends stupid video, have to reply
`wtf` Sends stupid video, have to reply
`rage` Sends stupid image, have to reply
`idc/idfc` Sends stupid video, have to reply
`clown` Sends yet another stupid video, have to reply
`mb` Sends stupid video, have to reply
`faq` Sends a message to read the FAQ
`malware` Sends a message on how the menu isn't malicious
`falsepositive` Sends a message about the false positives
`quote *[reply]` Quotes whoever you reply to
`ping` Shows you bot latency
`gamble` Gamble for a chance of winning Early Access
`realping` Shows you real bot latency
`yapper` Shows the biggest yappers
`getyapcount` Shows how many messages you've sent
`download` Downloads and sends the menu to you
`installer` Sends the installer for the mod menu
`getyap *[user id]` Gets a user's message count
`getplace *[place]` Gets whoever is in a specific place
`shitpost [count]` Sends shitposts
`delshitpost [shitpost]` Deletes whatever shitpost link you attach
`yourgrammarsucks` yeah""")
            await message.author.send("# Bot Commands", file=discord.File("cmds.txt"))
            await message.add_reaction("<:thumbsup:1173741933005393920>")

        if args[0] == "join":
            if len(args) > 1:
                channel = discord.utils.get(client.guilds[0].voice_channels, id=int(args[1]))
                if not client.voice_clients:
                    await channel.connect()
                    await message.reply("Connected to <#"+str(channel.id)+">")
                else:
                    await message.reply("I'm already in <#"+str(discord.utils.get(client.voice_clients, guild=message.guild).channel.id)+">")
            else:
                channel = message.author.voice.channel
                if not client.voice_clients:
                    await channel.connect()
                    await message.reply("Connected to <#"+str(channel.id)+">")
                else:
                    await message.reply("I'm already in <#"+str(discord.utils.get(client.voice_clients, guild=message.guild).channel.id)+">")

        if args[0] == "leave":
            voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
            if voice_client is not None:
                chnid = discord.utils.get(client.voice_clients, guild=message.guild).channel.id
                await voice_client.disconnect()
                await message.reply("Disconnected from <#"+str(chnid)+">")
            else:
                await message.reply("I'm not in a voice channel")

        global FFMPEG_OPTIONS
        if args[0] == "loudasf" and message.author.id in owners:
            if args[1] == "true":
                FFMPEG_OPTIONS = {'options': '-af "volume=10.0"'}
                await message.reply("I'm gonna get timed out for mic spam")
            else:
                FFMPEG_OPTIONS = {'options': '-vn'}
                await message.reply("Reverted")
        
        if args[0] == "play":
            if not ".." in message.content:
                voice_client = discord.utils.get(client.voice_clients, guild=message.guild)

                fix = ' '.join(args[1:])

                source = discord.FFmpegPCMAudio('AllowedMusic/'+fix+".mp3", **FFMPEG_OPTIONS)
                voice_client.play(source)
                await message.reply("Playing "+fix+" from allowed music list")
            else:
                await  message.reply("Permission denied")
        
        if args[0] == "stop":
            voice_client = discord.utils.get(client.voice_clients, guild=message.guild)

            voice_client.stop()
            await message.reply("Stopping music")

        if args[0] == "neofetch":
            try:
                result = subprocess.run(["neofetch", "--stdout"], capture_output=True, text=True, check=True)
                output = result.stdout
            except FileNotFoundError as e:
                output = f"neofetch is not installed or not found: {e}"
            except subprocess.CalledProcessError as e:
                output = f"Failed to execute neofetch: {e.stderr}"
            except Exception as e:
                output = f"Unexpected error: {e}"

            await message.reply(f"```ansi\n{output}\n```")
        
        if args[0] == "songs":
            MUSIC_DIRECTORY = "AllowedMusic"
            music_files = [f for f in os.listdir(MUSIC_DIRECTORY) if os.path.isfile(os.path.join(MUSIC_DIRECTORY, f))]
            music_names = [os.path.splitext(f)[0] for f in music_files]
            music_names_string = '\n'.join(music_names)
            with open("music_names.txt", "w", encoding="utf-8") as file:
                file.write(music_names_string)
            await message.reply(file=discord.File("music_names.txt"))
        
        if args[0] == "uploadsong":
            for attachment in message.attachments:
                if attachment.filename.endswith('.mp3'):
                    file_path = os.path.join("AllowedMusic", attachment.filename)
                    await download_file(attachment.url, file_path)
                    await message.reply(f'File {attachment.filename} uploaded to AllowedMusic')
        
        if args[0] == "upload" and message.author.id in owners:
            for attachment in message.attachments:
                file_path = os.path.join(' '.join(args[1:]), attachment.filename)
                await download_file(attachment.url, file_path)
                await message.reply(f'File {attachment.filename} uploaded to '+' '.join(args[1:]))

        if args[0] == "sendfile" and message.author.id in owners:
            thedir = ' '.join(args[1:])
            if "token" not in thedir.lower():
                await message.reply(file=discord.File(thedir))
        
        if args[0] == "spotdl" and message.author.id in owners:
            fix = ' '.join(args[1:])
            try:
                DOWNLOAD_DIR = "AllowedMusic"
                command = ['spotdl', fix, '--output', f'{DOWNLOAD_DIR}/%(title)s.%(ext)s']
                subprocess.run(command, check=True)

                for file_name in os.listdir(DOWNLOAD_DIR):
                    if file_name.endswith('.mp3'):
                        file_path = os.path.join(DOWNLOAD_DIR, file_name)
                        
                        await message.reply(file=discord.File(file_path))
                        
                        break
                else:
                    await message.reply("Song download failed or couldn't find the file")
                    
            except subprocess.CalledProcessError as e:
                await message.reply(f"An error occurred during download")

        if args[0] == "ytdl" and message.author.id in owners:
            fix = ' '.join(args[1:])

            try:
                DOWNLOAD_DIR = "AllowedMusic"
                output_template = f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'quiet': True,
                    'outtmpl': output_template,
                    'noplaylist': True,  # Ensure single video download
                    'x': True,  # Extract audio
                    'no_mtime': True,  # Do not modify file timestamps
                    'audio_format': 'mp3',
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([fix])  # Download the video as audio

                # Find the most recent .mp3 file in the directory
                mp3_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.mp3')]
                if mp3_files:
                    latest_file = max(mp3_files, key=lambda f: os.path.getctime(os.path.join(DOWNLOAD_DIR, f)))
                    file_path = os.path.join(DOWNLOAD_DIR, latest_file)
                    await message.reply(file=discord.File(file_path))
                else:
                    await message.reply("Song download failed or couldn't find the file")

            except Exception as e:
                await message.reply("An error occurred during download")

        if args[0] == "invite" and message.author.id in owners:
            await message.reply(inviteall(args[1].upper()))

        if args[0] == "inviterandom" and (message.author.id in owners or message.author.id == 738573735895892050 or message.author.id == 252548095244500994):
            await message.reply(inviterandom(args[1].upper(), int(args[2])))

        if args[0] == "notify" and message.author.id in owners:
            if len(args) > 1 and args[1].isdigit():
                await message.reply(sendnotification(' '.join(args[2:]), int(args[1])))
            else:
                await message.reply(sendnotification(' '.join(args[1:]), 5000))

        if args[0] == "notifyformat" and message.author.id in owners:
            if len(args) > 1 and args[1].isdigit():
                await message.reply(sendnotification("<color=grey>[</color><color=red>SERVER</color><color=grey>]</color> " + (' '.join(args[2:])), int(args[1])))
            else:
                await message.reply(sendnotification("<color=grey>[</color><color=red>SERVER</color><color=grey>]</color> " + (' '.join(args[1:])), 5000))
        
        if args[0] == "dm" and not is_community_helper(message):
            if message.author.id not in owners:
                await message.reply("Not implemented")
                return

            fix = ' '.join(args[2:])
            await client.get_channel(1458530151318159421).send("Bot dm " + str(message.content) + " by " + str(message.author.id) + " -- " + str(message.author.name))
            user = client.get_user(int(args[1]))
            if user is None:
                await message.reply("User "+args[1]+" does not exist")
                return
            try:
                await user.send(fix)
                await message.reply("Message sent to "+user.name+" successfully")
            except:
                await message.reply("Could not send a message to "+user.name)
        
        blocked_command_prefixes = ("?", "!", "/", ".")

        blocked_commands = [
            "ban",
            "kick",
            "role",
            "mute",
            "unmute",
            "timeout",
            "purge",
        ]

        if args[0] == "fsp" and not is_community_helper(message):

            #if message.author.id not in owners:
            #    await message.reply("Not implemented")
            #    return

            message_content = ' '.join(args[3:])

            if "@here" in message_content or "@everyone" in message_content:
                    await message.reply("<@894348631904223232> <@252548095244500994> <@" + str(message.author.id) + "> tried to ping everyone/here with fsp command")
                    return

            for prefix in blocked_command_prefixes:
                for cmd in blocked_commands:
                    if message_content.startswith(f"{prefix}{cmd}") or message_content.startswith(f"{prefix}{cmd} "):
                        await message.reply("<@894348631904223232> <@252548095244500994> <@" + str(message.author.id) + "> tried to run bot commands with fsp command")
                        return

            mode = args[1]
            await client.get_channel(1458530151318159421).send("Bot fsp " + str(message.content) + " by " + str(message.author.id) + " -- " + str(message.author.name))
            if mode == 'send':
                channel_id = args[2]
                
                
                channel = client.get_channel(int(channel_id))
                if channel is None:
                    await message.reply("Channel not found")
                    return
                await channel.send(message_content)
                await message.reply(f"Message sent to channel <#{channel_id}>")
            elif mode == 'reply':
                channel_id, message_id = args[2].split('@')
                channel = client.get_channel(int(channel_id))
                if channel is None:
                    await message.reply("Channel not found")
                    return
                try:
                    message2 = await channel.fetch_message(int(message_id))
                except discord.NotFound:
                    await message.reply("Message not found")
                    return
                await message2.reply(message_content)
                await message.reply(f"Replied to message {message_id} in channel <#{channel_id}>")
            else:
                await message.reply("Invalid mode")
        
        if args[0] == "userdata":
            user = client.get_user(int(args[1]))
            if user is None:
                await message.reply("User "+args[1]+" does not exist")
            else:
                await message.reply("""```
Username          {uname}
Display Name      {dname}
Discriminator     {discrim}
User ID           {uid}
Avatar            {avatar}
Creation Date     {cdate}
Bot?              {isbot}
System?           {issys}```""".format(uname = user.name, dname = user.global_name, discrim = user.discriminator, uid = user.id, avatar = user.avatar.url, cdate = user.created_at, isbot = user.bot, issys = user.system))
        
        if args[0] == "msgdata":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            if replied_message is None:
                await message.channel.send("Message does not exist")
            else:
                user = replied_message.author
                await message.reply("""```
Author
    Username          {uname}
    Display Name      {dname}
    Discriminator     {discrim}
    User ID           {uid}
    Avatar            {avatar}
    Creation Date     {cdate}
    Bot?              {isbot}
    System?           {issys}
Content
	Channel ID        {chnid}
	Message ID        {msgid}
	Guild ID          {guildid}
    Creation Date     {cdatem}
	Text              {text}
	Attachments       {atts}
	Embeds            {embs}
	Components        {comps}
    Pinned?           {pinned}```""".format(uname = user.name, dname = user.global_name, discrim = user.discriminator, uid = user.id, avatar = user.avatar.url, cdate = user.created_at, isbot = user.bot, issys = user.system, chnid = replied_message.channel.id, msgid = replied_message.id, guildid = replied_message.guild.id, text = str(replied_message.content), atts = str(len(replied_message.attachments)), embs = str(len(replied_message.embeds)), comps = str(len(replied_message.components)), cdatem = replied_message.created_at, pinned = replied_message.pinned))

        if args[0] == "howgay":
            gaymeter = random.randint(1, 100)
            await message.reply("🏳️‍🌈 You are "+str(gaymeter)+"% gay")
            if gaymeter == 100:
                gayrole = client.guilds[0].get_role(1213700257989267567)
                await message.author.add_roles(gayrole)

        if args[0] == "8ball":
            await message.reply("🎱 " + random.choice([
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "No.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
            ]))
        
        if args[0] == "9ball":
            await message.reply("🎱 " + random.choice([
                "Have you tried turning it off and back on again?",
                "Maybe, but you'll need a fireball",
                "The butler did it. Duh.",
                "Look for the Bugbear to find the answer.",
                "Your dilemma would be solved by not fighting a DRAGON.",
                "That sounds like a question for a crystal ball.",
                "Do I look like a wizard to you?",
                "I'll see what I can do.",
                "As likely as I'm a dinosaur.",
                "If it doesn't work then you really f@cked up.",
                "The Magic Fluid Needs Replacement.",
                "I am an 8ball not a globe or map, I don't know where you are",
                "You know I’m not actually magic right? I’m just a piece of plastic floating in alcohol, with prewritten responses embossed on the sides.",
                "Whether I tell you yes or no, all I truly reveal is which one you were hoping for.",
                "Long rest, and try again.",
                "Goodbye.",
                "You broke the 8 ball",
                "You broke the 9 ball",
                "The Glass is Half Full.",
                "The Glass is Half Empty.",
                "“Everyone can use a friend.” The Ball duplicates itself, when one is used, both show the same answer.",
                "Anyway, here’s Wonderwall.",
                "Property of Wizzo the Wizard.",
                "Your funeral.",
                "Whoa! Why do I have to answer this?",
                "I have failed you, Anakin! I have failed you.",
                "Your mom.",
                "Bitch wtf",
                "Search your Feelings. You know it to be true.",
                "The answer you seek is behind you.",
                "Just don't bother.",
                "In the loosest sense, yes.",
                "In the loosest sense, no.",
                "Theoretically, it could work. I would not recommend it, though.",
                "Please pass me to someone saner.",
                "Could you please think before you ask me something?",
                "Dodge left!",
                "Don't ask me!",
                "The stars shall give you the answer.",
                "I'm not nearly omnipotent enough for this.",
                "Sure, if you want a tragedy on your hands.",
                "No, but the failure will be entertaining for centuries to come!",
                "Survey says: Bzzzt!",
                "Diviners are currently busy. Please try again later.",
                "Oh, a good omen!",
                "When the Nine Hells freeze over.",
                "Yes, now leave me alone.",
                "Yes! I mean no! Wait...",
                "Your intellect score must be in the negatives, because the answer is NO!",
                "Even the barbarian could answer that for you, come on",
                "Sure, I mean, its your funeral",
                "It won't work, but it will be very funny",
                "Technically yes, but you'll hate it",
                "I might be magic but how would I ever know that?",
                "Ask later, I'm writing a novel and I feel very inspired right now.",
                "Not really, but please don't touch me again with bloodstained hands, its gross.",
                "May I first ask what in the nine hells are you carrying in your backpack? Because it smells worse than a dead orc.",
                "You don't want to know, trust me.",
                "Well, none of you can disarm traps to save their lives, so I don't like your chances.",
                "Even the worm turns",
                "An ominous wind blows",
                "Try a direct approach",
                "There is no answer",
                "Is no fun, is no blinsky",
                "Plan for success.",
                "Prepare for failure.",
                "You'll know when you know.",
                "Alone you will fail.",
                "Best have a backup plan.",
                "Can you leave me here when you head out.",
                "Circumstances make your question irrelevant.",
                "Soon",
                "The future is bloody.",
                "Man u weird",
                "The future is unclear.",
                "You will fail.",
                "You will succeed.",
                "The answer you seek lies inside a dragon's mouth.",
                "Only with a god's intervention.",
                "No, but I know you're going to try anyway, you fool.",
                "Help will come from an unexpected source... like, REALLY unexpected.",
                "Don't trust the human.",
                "Despite your fumbling efforts, you will meet with success!",
                "Before I answer, could you scratch my back for me? Just - exactly opposite from this little window, a little to the right - no, my right - up a bit... almost... Yes, that's it! Thanks, friend. Anyway, no, you're all going to die.",
                "Yes, but pack an extra healing potion just in case. Trust me on this one.",
                "Your question will be answered... eventually.",
                "Sorry. No one is here right now to take your call. Leave a message after the tone <<BEEP>>",
                "Nice try, you already know the answer.",
                "No way, buddy!",
                "Hey, leave me out of this!",
                "Yes, immediately",
                "Highly unlikely.",
                "Let's just say anything is possible through the liberal application of fire.",
                "What? Sorry, I wasn't listening.",
                "Ask me again, and this time try not to sound like such a moron.",
                "I think there are tables for this sort of question.",
                "No, and if I were you I'd be more discrete asking such questions.",
                "Seek not the answer, you know not the cost",
                "42",
                "Heaven brings forth innumerable things to nurture man.",
                "Man has nothing good with which to recompense Heaven.",
                "The tiger. He destroyed his cage. Yes, YES, the tiger is out",
                "Do you really wish to know?",
                "Perhaps, with great power of will.",
                "The answer you seek involves multitudes of spiders.",
                "Seriously?! this is the question you decided to ask?!",
                "I'm not even going to answer this one.",
                "Sure, but with caution.",
                "...What kind of question is that? Absloutely not!",
                "Sure, it'll be fun.",
                "Honestly even with all my magic, I don't think I can answer such a question.",
                "Maybe, maybe not.",
                "Get yourself together and ask again.",
                "I will let this one speak for itself.",
                "This was not in the job description!",
                "I don't know! You should ask yourself!",
                "What am I, a divination spell?",
                "Leylines shifting, ask again later.",
                "Future looks grim. Expect trouble.",
                "Hey, are you sure I’m not a Mimic?",
                "Try asking it to a corpse",
                "No, not even through wish/miracle",
                "You'll never know until you try and attack it",
                "No, she's way out of your charisma attribute",
                "Balls",
                "I don't know, I don't get paid enough"
            ]))

        if args[0] == "coinflip":
            await message.reply("🪙 " + random.choice([
                "The coin lands on heads.",
                "The coin lands on tails.",
            ]))
        
        if args[0] == "avatar":
            user = client.get_user(int(args[1]))
            if user is None:
                await message.channel.send("User "+args[1]+" does not exist")
            else:
                await message.channel.send(user.avatar.url)

        if args[0] == "dt":
            fix = ' '.join(args[1:])

            replied_message = await message.channel.fetch_message(message.reference.message_id)
            author = replied_message.author
            await replied_message.delete()
            await author.timeout(timedelta(days=1), reason = fix)
            await author.send("You were timed out for a day: "+fix)
            await message.reply("Timed "+str(author.id))

        if args[0] == "kick":
            if len(args) < 2:
                return await message.reply("Usage: .kick userid [reason]")
            
            user = await client.fetch_user(args[1])
            reason = ' '.join(args[2:]) if len(args) > 2 else "No reason provided"
            
            member = message.guild.get_member(user.id)
            if member:
                await member.kick(reason=reason)
                await message.reply(f"Kicked {user.id} ({reason})")
            else:
                await message.reply("User not found in the server.")

        if args[0] == "ban" and not is_community_helper(message):
            if len(args) < 2:
                return await message.reply("Usage: .ban userid [time] [reason]")
            
            user = await client.fetch_user(args[1])
            ban_time = None
            reason = "No reason provided"
            
            if len(args) > 2:
                parsed_time = parse_time(args[2])
                if parsed_time:
                    ban_time = parsed_time
                    reason = ' '.join(args[3:]) if len(args) > 3 else "No reason provided"
                else:
                    reason = ' '.join(args[2:])
            
            member = message.guild.get_member(user.id)
            if member:
                await message.guild.ban(member, reason=reason)
                await message.reply(f"Banned {user.id} ({reason})")

            else:
                await message.reply("User not found in the server.")

        if args[0] == "mute":
            if len(args) < 3:
                return await message.reply("Usage: .mute userid time [reason]")
            
            user = await client.fetch_user(args[1])
            mute_time = parse_time(args[2])
            if mute_time is None:
                return await message.reply("Invalid time format. Use w/week, m/mo/mon/mont/month, d/da/day, or min.")
            
            reason = ' '.join(args[3:]) if len(args) > 3 else "No reason provided"
            member = message.guild.get_member(user.id)
            
            if member:
                await member.timeout(timedelta(minutes=mute_time), reason=reason)
                await message.reply(f"Muted {user.id} for {args[2]} ({reason})")
            else:
                await message.reply("User not found in the server.")
        
        if args[0] == "texttomorse":
            fix = ' '.join(args[1:])
            await message.reply(text_to_morse(fix))

        if args[0] == "morsetotext":
            fix = ' '.join(args[1:])
            await message.reply(morse_to_text(fix))

        if args[0] == "base64encode":
            fix = ' '.join(args[1:])
            encoded = base64.b64encode(fix.encode()).decode()
            await message.reply(encoded)

        if args[0] == "base64decode":
            fix = ' '.join(args[1:])
            await message.reply(base64.b64decode(fix))

        if args[0] == "translate":
            fix = ' '.join(args[2:])
            await message.reply(translate(args[1], fix))

        if args[0] == "console":
            if any(role.id == 1418055219559923732 for role in message.author.roles):
                await handleConsole(message, args)
            else:
                await message.reply("Permission denied")

        if args[0] == "setpoll" and message.author.id in owners:
            fix = ' '.join(args[1:])
            data = fix.split(";")

            url = "https://iidk.online/setpoll"
            body = {"key": authenticationkey, "poll": data[0], "a": data[1], "b": data[2]}
            
            response = requests.post(url, json=body, timeout=5)
            if response.status_code == 200:
                await message.reply("I did it are you proud of me")
            else:
                print(f"Failed to pollify: {response.status_code}")
                await message.reply("Yeah fuck you")

        if args[0] == "blacklist" and message.author.id in owners:
            await handleBlacklist(message, args)
        
        if args[0] == "fakeban":
            await message.delete()
            username = args[1]
            reason = "No reason given."
            if len(args) > 2:
                reason = ' '.join(args[2:])
            message_content = ""
            embed = {
                #"title": "title",
                "description": "<:dynoSuccess:1306044575118528603> ***" + username + " was banned.*** | "+reason,
                "color": (67 << 16) + (181 << 8) + 130,
                #"fields": [
                #    {"name": "Field 1", "value": "Value 1", "inline": True},
                #    {"name": "Field 2", "value": "Value 2", "inline": True}
                #]
            }
            global privwhurl
            send_discord_webhook(privwhurl, message_content, embed)
        
        if args[0] == "membercount":
            await message.reply("Members: "+str(client.guilds[0].member_count))

        if args[0] == "usercount":
            url = "https://iidk.online/usercount"
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                await message.reply(f"Menu users: {data.get('users', 'Unknown')}")
            except requests.exceptions.RequestException as e:
                await message.reply("Unable to fetch menu user count")
            except requests.exceptions.Timeout:
                await message.reply("Request timed out")

        if args[0] == "pollresults":
            try:
                response = requests.get("https://iidk.online/votes", timeout=5)
                response.raise_for_status()
                data = response.json()

                response2 = requests.get("https://iidk.online/serverdata", timeout=5)
                response2.raise_for_status()
                serverdata = response2.json()  # <- fixed, was using response.json()

                optiona = serverdata.get('option-a', "Option A")
                optionb = serverdata.get('option-b', "Option B")
                poll = serverdata.get('poll', "Poll")

                avotes = data.get('a-votes', 0)
                bvotes = data.get('b-votes', 0)

                total = avotes + bvotes

                if total > 0:
                    a_percent = avotes / total * 100
                    b_percent = bvotes / total * 100
                    result = (
                        f"# {poll}\n"
                        f"Total Votes: {total}\n\n"
                        f"{optiona}: {a_percent:.2f}%\n"
                        f"{optionb}: {b_percent:.2f}%"
                    )
                else:
                    result = "No votes yet."

                await message.reply(result)

            except requests.exceptions.Timeout:
                await message.reply("Request timed out while fetching poll results.")
            except requests.exceptions.RequestException as e:
                await message.reply(f"Unable to fetch poll results: {e}")

        if args[0] == "peakcount":
            with open("peakcount.txt", 'r') as file:
                await message.reply(f"Peak user count: {file.read().strip()}")


        if args[0] == "dbcount":
            url = "https://iidk.online/databasecount"
            try:
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                data = response.json()
                await message.reply(f"Users in database: {data.get('size', 'Unknown')}")
            except requests.exceptions.RequestException as e:
                await message.reply("Unable to fetch database user count")
            except requests.exceptions.Timeout:
                await message.reply("Request timed out")
        
        if args[0] == "lookupcosmetic":
            data = fetch_data()
            if data:
                replyText = "```\n" + search_cosmetics(data, args[1].upper()) + "\n```"
                if len(replyText) > 2000:
                    with open("lookupcosmetic.txt", 'w') as file:
                        file.write(replyText)
                            
                    await message.reply(file=discord.File("lookupcosmetic.txt"))
                else:
                    await message.reply(replyText)
            else:
                await message.reply("No data found")
            
        if (args[0] == "lookupid" or args[0] == "lookupuid"):
            data = fetch_data()
            if data:
                replyText = "```\n" + search_uid(data, args[1].upper()) + "\n```"
                if len(replyText) > 2000:
                    with open("lookupid.txt", 'w') as file:
                        file.write(replyText)
                            
                    await message.reply(file=discord.File("lookupid.txt"))
                else:
                    await message.reply(replyText)
            else:
                await message.reply("No data found")
        
        if args[0] == "link":
            isDonor = any(role.id == 1354610628580347944 for role in message.author.roles)
            isSupporter = any(role.id == 1354611031141253211 for role in message.author.roles)
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            isOwner = any(role.id == 1170116220855537754 for role in message.author.roles)
            isCoOwner = any(role.id == 1432166270672830494 for role in message.author.roles)
            isConsoleOwner = any(role.id == 1432183142093033582 for role in message.author.roles)
            isMenuDeveloper = any(role.id == 1432167082123853826 for role in message.author.roles)
            isAdmin = any(role.id == 1170116321388810411 for role in message.author.roles)
            isStaffManager = any(role.id == 1246281245021962340 for role in message.author.roles)
            isModerator = any(role.id == 1177487180453646387 for role in message.author.roles)
            isCommunityHelper = any(role.id == 1207131095834038343 for role in message.author.roles)

            isBoyfriend = message.author.id == 1392621350249824486

            roleName = (
                "Owner" if isOwner
                else "Co-Owner" if isCoOwner
                else "Console Owner" if isConsoleOwner
                else "Menu Developer" if isMenuDeveloper
                else "Boyfriend" if isBoyfriend
                else "Admin" if isAdmin
                else "Staff Manager" if isStaffManager
                else "Moderator" if isModerator
                else "Community Helper" if isCommunityHelper
                else "Ultimate Tracker" if isUltimateTracker
                else "Basic Tracker" if isBasicTracker
                else "Supporter" if isSupporter
                else "Donor" if isDonor
                else "Null"
            )
            url = "https://iidk.online/addpatreon"
            body = {"key": authenticationkey, "id": args[1], "discord": message.author.id, "name": roleName, "icon": message.author.avatar.url}
            
            response = requests.post(url, json=body, timeout=5)
            if response.status_code == 200:
                await message.reply("**Successfully linked account!**\nYour special role will now show above your head for anyone else with the menu.\n\nRole: **"+roleName+"**\nIcon: "+message.author.avatar.url+"\n-# Changes may take up to 60 seconds to take place")
            else:
                print(f"Failed to link account: {response.status_code}")
                await message.reply("Failed to link account")

        if args[0] == "unlink":
            url = "https://iidk.online/removepatreon"
            body = {"key": authenticationkey, "id": message.author.id}
            
            response = requests.post(url, json=body, timeout=5)
            if response.status_code == 200:
                await message.reply("**Successfully unlinked account.**\nYour special role will no longer show above your head.\n-# Changes may take up to 60 seconds to take place")
            else:
                print(f"Failed to unlink account: {response.status_code}")
                await message.reply("Failed to unlink account")

        if args[0] == "lookupnick":
            data = fetch_data()
            if data:
                replyText = "```\n" + search_nick(data, args[1].upper(), False) + "\n```"
                if len(replyText) > 2000:
                    with open("lookupnick.txt", 'w') as file:
                        file.write(replyText)
                            
                    await message.reply(file=discord.File("lookupnick.txt"))
                else:
                    await message.reply(replyText)
            else:
                await message.reply("No data found")
        
        if args[0] == "lookuproom":
            data = fetch_data()
            if data:
                replyText = "```\n" + search_room(data, args[1].upper(), False) + "\n```"
                if len(replyText) > 2000:
                    with open("lookuproom.txt", 'w') as file:
                        file.write(replyText)
                            
                    await message.reply(file=discord.File("lookuproom.txt"))
                else:
                    await message.reply(replyText)
            else:
                await message.reply("No data found")

        if args[0] == "lookupdb":
            try:
                data = search_db(args[1].upper())
                if data:
                    replyText = "```\n" + data + "\n```"
                    if len(replyText) > 2000:
                        with open("lookupdb.txt", 'w') as file:
                            file.write(replyText)
                                
                        await message.reply(file=discord.File("lookupdb.txt"))
                    else:
                        await message.reply(replyText)
                else:
                    await message.reply("No data found")
            except Exception as e:
                await message.reply(f"An error occurred")

        if args[0] == "advancedsearch":
            try:
                data = sql(build_select_query(args[1]))
                if data:
                    replyText = "```\n" + data + "\n```"
                    if len(replyText) > 2000:
                        with open("advancedsearch.txt", 'w') as file:
                            file.write(replyText)
                                
                        await message.reply(file=discord.File("advancedsearch.txt"))
                    else:
                        await message.reply(replyText)
                else:
                    await message.reply("No data found")
            except Exception as e:
                await message.reply(f"An error occurred")

        if args[0] == "playermap":
            try:
                data = getplayermap()
                if data:
                    replyText = "```\n" + data + "\n```"
                    if len(replyText) > 2000:
                        with open("playermap.txt", 'w') as file:
                            file.write(replyText)
                                
                        await message.reply(file=discord.File("playermap.txt"))
                    else:
                        await message.reply(replyText)
                else:
                    await message.reply("No data found")
            except Exception as e:
                await message.reply(f"An error occurred")
        
        if args[0] == "getallrooms":
            data = fetch_data()
            if data:
                replyText = "```\n" + get_all_rooms(data) + "\n```"
                if len(replyText) > 2000:
                    with open("getallrooms.txt", 'w') as file:
                        file.write(replyText)
                            
                    await message.reply(file=discord.File("getallrooms.txt"))
                else:
                    await message.reply(replyText)
            else:
                await message.reply("No data found")

        if args[0] == "whatis":
            response = "No cosmetics found"
            indiv = cosmeticdata.split("\n")
            for cosmetic in indiv:
                cosmeticinfo = cosmetic.split(";;")
                if (' '.join(args[1:])).upper() in cosmeticinfo[0].upper() or (' '.join(args[1:])).upper() in cosmeticinfo[1].upper():
                    if response == "No cosmetics found":
                        response = "Cosmetic " + cosmeticinfo[0] + "\nName: " + cosmeticinfo[1] + "\nPrice: " + cosmeticinfo[2]
                    else:
                        response += "\n\nCosmetic " + cosmeticinfo[0] + "\nName: " + cosmeticinfo[1] + "\nPrice: " + cosmeticinfo[2]
            
            response = "```\n" + response + "\n```"
            if len(response) > 2000:
                with open("whatis.txt", 'w') as file:
                    file.write(response)
                        
                await message.reply(file=discord.File("whatis.txt"))
            else:
                await message.reply(response)

        if args[0] == "elapsedtime":
            elapsed_time_ms = math.floor((time.time() - start_time) * 1000)
            await message.reply("Bot has been online for `" + elapsed_time_ms + "ms`")
            
        if args[0] == "usergraph":
            time_labels = np.linspace(-len(values), 0, len(values))

            y_max = max(values) + 25
            y_min = 0

            plt.style.use('dark_background')

            plt.figure(figsize=(12, 6))
            plt.plot(time_labels, values, marker='o', linestyle='-', color='orange', label='User Count')
            plt.title('User Count Over Time', fontsize=16, color='white')
            plt.xlabel('Time (minutes)', fontsize=14, color='white')
            plt.ylabel('User Count', fontsize=14, color='white')
            plt.ylim([y_min, y_max])
            plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
            plt.legend(fontsize=12)
            plt.tick_params(colors='white')
            plt.tight_layout()

            plt.savefig("usergraph.png")
            plt.close()

            await message.reply(file=discord.File("usergraph.png"))
        
        if args[0] == "yn":
            fix = ' '.join(args[1:])

            await message.delete()
            coolmsg = await message.channel.send("# YES OR NO\n"+fix)
            await coolmsg.add_reaction("✅")
            await coolmsg.add_reaction("❌")
        
        if args[0] == "numpoll":
            fix = ' '.join(args[2:])
            
            await message.delete()
            coolmsg = await message.channel.send("# POLL\n"+fix)
            number_emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']

            for i in range(min(int(args[1]), len(number_emojis))):
                await coolmsg.add_reaction(number_emojis[i])
            
        if args[0] == "abcpoll":
            fix = ' '.join(args[2:])
            
            await message.delete()
            coolmsg = await message.channel.send("# POLL\n"+fix)
            regional_indicator_emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']

            for i in range(min(int(args[1]), len(regional_indicator_emojis))):
                await coolmsg.add_reaction(regional_indicator_emojis[i])
        
        if args[0] == "timeout":
            fix = ' '.join(args[2:])

            thy = client.guilds[0].get_member(int(args[1]))
            await thy.timeout(timedelta(days=1), reason = fix)
            await thy.send("You were timed out for a day: "+fix)
            await message.reply("User was successfully timed out")
        
        if args[0] == "purgevc" and message.author.id in owners:
            voice_channel = client.guilds[0].get_channel(int(args[1]))

            count = 0
            if isinstance(voice_channel, discord.VoiceChannel):
                for member in voice_channel.members:
                    try:
                        await member.move_to(None)
                        count = count + 1
                    except discord.Forbidden:
                        await message.reply("Permission denied")
                    except Exception as e:
                        await message.reply(f"An error occurred: {e}")
                await message.reply("Successfully disconnected **"+str(count)+"** members from "+voice_channel.name)
            else:
                await message.reply("VC does not exist")
        
        if args[0] == "muteall" and message.author.id in owners:
            voice_channel = client.guilds[0].get_channel(int(args[1]))

            count = 0
            if isinstance(voice_channel, discord.VoiceChannel):
                for member in voice_channel.members:
                    try:
                        await member.edit(mute=True)
                        count = count + 1
                    except discord.Forbidden:
                        await message.reply("Permission denied")
                    except Exception as e:
                        await message.reply(f"An error occurred: {e}")
                await message.reply("Successfully muted **"+str(count)+"** members from "+voice_channel.name)
            else:
                await message.reply("VC does not exist")
        
        if args[0] == "os" and message.author.id in owners:
            await message.reply("Executing command")
            os.system(' '.join(args[1:]))

        if args[0] == "osverbal" and message.author.id in owners:
            try:
                result = subprocess.run(args[1:], capture_output=True, text=True, check=True, timeout=10)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = f"Command failed:\n{e.stderr}"
            except Exception as e:
                output = f"Unexpected error: {e}"

            await message.reply("```\n" + output + "```")

        if args[0] == "osverbalshell" and message.author.id in owners:
            try:
                result = subprocess.run(args[1:], shell=True, capture_output=True, text=True, check=True, timeout=10)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = f"Command failed:\n{e.stderr}"
            except Exception as e:
                output = f"Unexpected error: {e}"

            await message.reply("```\n" + output + "```")

        if (args[0] == "hardreboot" or args[0] == "hardrestart") and message.author.id in owners:
            with open("fromrestart.txt", 'w') as file:
                file.write(str(message.author.id))

            await message.reply("Bot is restarting, this could take a minute")
            os.system("sudo reboot")

        if (args[0] == "reboot" or args[0] == "restart") and message.author.id in owners:
            with open("fromrestart.txt", 'w') as file:
                file.write(str(message.author.id))

            await message.reply("Bot is restarting, this could take a minute")

            try:
                os.system("sudo systemctl restart iibot")
            except Exception as e:
                await message.reply(f"Failed to restart the bot: {e}")

        if args[0] == "synctree" and message.author.id in owners:
            await tree.sync()
            await message.reply("Synced bot slash command tree")

        if args[0] == "updatebot":
            if message.author.id in owners:
                for attachment in message.attachments:
                    if attachment.filename.endswith('.py'):
                        await download_file(attachment.url, 'script.py')
                        await message.reply(f'File {attachment.filename} has been downloaded and saved to script.py')
                        await message.channel.send('Restarting the machine...')
                        with open("fromrestart.txt", 'w') as file:
                            file.write(str(message.author.id))
                
                        if len(args) > 1:
                            if args[1] == "fast":
                                try:
                                    os.system("sudo systemctl restart iibot")
                                except Exception as e:
                                    await message.reply(f"Failed to restart the bot: {e}")
                        else:
                            subprocess.call('sudo reboot', shell=True)
        
        if args[0] == "botsrc":
            if message.author.id in owners:
                await message.reply(f"Here is the bot source:", file=discord.File("script.py"))

        if args[0] == "close":
            await close_thread(message)

        if args[0] == "unmuteall" and message.author.id in owners:
            voice_channel = client.guilds[0].get_channel(int(args[1]))

            count = 0
            if isinstance(voice_channel, discord.VoiceChannel):
                for member in voice_channel.members:
                    try:
                        await member.edit(mute=False)
                        count = count + 1
                    except discord.Forbidden:
                        await message.reply("Permission denied")
                    except Exception as e:
                        await message.reply(f"An error occurred: {e}")
                await message.reply("Successfully unmuted **"+str(count)+"** members from "+voice_channel.name)
            else:
                await message.reply("VC does not exist")

        if args[0] == "vcdata":
            voice_channel = client.guilds[0].get_channel(int(args[1]))

            stringthing = "```"
            if isinstance(voice_channel, discord.VoiceChannel):
                for member in voice_channel.members:
                    try:
                        stringthing += "\n" + member.name
                    except discord.Forbidden:
                        await message.reply("Permission denied")
                    except Exception as e:
                        await message.reply(f"An error occurred: {e}")
                await message.reply(stringthing+"\n```")
            else:
                await message.reply("VC does not exist")

        if args[0] == "dr":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170845739312742511/1208542841786212442/v0f044gc0000chlmehrc77u4h69aj9s0.mp4?ex=65e3aa3b&is=65d1353b&hm=d230b9a391440402826420c99b54ae96969665f2fa8c73ccfede91f0bc4ec5e5&")

        if args[0] == "somepony":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1257107211344285726/1381821634754777249/somepony.mp4?ex=6848e92e&is=684797ae&hm=18323e757b04c41604c9b5c09629c6b54ae8ca971cade3a1db2483815c5caf48&")
        
        if args[0] == "creed":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1299528878636797952/1382052267028381758/creed01.mp4?ex=6849bff9&is=68486e79&hm=baf159fbe8569f9ac20d11f8ff3b2549da98926fb2b58242acca0b4c778387ec&")

        if args[0] == "yourgrammarsucks":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1217291290077696081/1245537047629009047/your_grammar_sucks.mp4?ex=66591c45&is=6657cac5&hm=b611f7424cb05ff51fbd5d8ecd20c1cb0372c0e0d38c6e8f604d5f4e0225153b&")

        if args[0] == "av":
            await message.reply("https://cdn.discordapp.com/attachments/1170116209098895401/1463217417126805536/av.mp4?ex=697106e9&is=696fb569&hm=5245d352ae9cb89dcc95c50bd4f8454acc4b24bc93906ef3ca2f6666c18a3006&")#file=discord.File("av.mp4"))
        #await message.reply(file=discord.File("av.mp4"))

        if args[0] == "exclude":
            await message.reply(file=discord.File("exclude.mp4"))
        
        if args[0] == "fixmods":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await message.reply("If you are experiencing issues with mods, try using our installer.\nHere is the menu installer (automatically installs the menu):", file=discord.File("installer.bat"))
        
        if args[0] == "dl":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1201631193385418903/1216480295247675442/How_To_Install_Any_Mods_For_Gorilla_Tag.mp4?ex=66008a8f&is=65ee158f&hm=d8b40310215d715f3b44bc3e3e0bef1d997e892b057fc87493dac0e86eb3435a&")
    
        if args[0] == "mmm":
            await message.reply("https://cdn.discordapp.com/attachments/1201631193385418903/1216480296912814322/How_To_Install_Monke_Mod_Manager.mp4?ex=66008a8f&is=65ee158f&hm=7411b477f792132458542bdb243f7286cd8551204f906df230d7b8e3fe10826d&")
        
        if args[0] == "temp":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1201631193385418903/1216480298565501080/How_To_Make_Your_Own_Menu.mp4?ex=66008a90&is=65ee1590&hm=fd1d0a52b66bb3a913b2f2353fbd62d72d0f0cc3ee2e3b79d7d5c7eae8aa23d1&")
        
        if args[0] == "malware":
            await message.reply("# The menu is not malware.\nThe false detections are caused from loading the version and saving your preferences to a local file.\nIf you don't believe this, you can check the source code for yourself: <https://github.com/iiDk-the-actual/iis.Stupid.Menu>\nYou can fix this by excluding ii's Stupid Menu from your antivirus. <#1433191399540523099>\n\n`This message is automated. If this was not what you were looking for, ignore this message.`")
        
        if args[0] == "falsepositive":
            await message.reply(""""[HackTool](<https://www.malwarebytes.com/blog/detections/riskware-hacktool>) and [RiskTool](<https://friendlycaptcha.com/wiki/what-is-risktool/>) detections **do not** mean the file is always bad...in some cases the these detections are related to legitimate programs which can be misused by others for nefarious purposes.
 
The **consensus among most experts** is that if **90%+** of the results of an online file analysis (VirusTotal, Jotti's virusscan, MetaDefender, Hybrid-Analysis, etc) indicate a file submission is clean, then you can disregard the other detection(s) as a [false positive.](<https://www.tomsguide.com/news/what-are-false-positives-and-how-to-avoid-them>) ..especially if the detection is more generic, suspicious, [potentially unwanted (PUPs)](<https://blog.malwarebytes.org/threat-analysis/2014/10/encountering-the-wild-pup-2/>) and/or was made by any of the lesser known security vendors. This is typically due to the security program's [heuristic analysis](<https://en.wikipedia.org/wiki/Heuristic_analysis>) engine which provides the ability to detect possible new variants of malware." - [quietman7 MVP Alumni, Microsoft Answers Volunteer Moderator](<https://answers.microsoft.com/en-us/windows/forum/all/trojanwin32kepavllrfn-virus-or-windows-defender/c86417af-6445-4f18-bce1-e4e541346f29>)""")

        if args[0] == "malwarecheck":
            folder_path = 'malwarecheck'
            os.makedirs(folder_path, exist_ok=True)
            
            for attachment in message.attachments:
                if attachment.size < 1024000:  # 100 KB limit
                    file_path = os.path.join(folder_path, attachment.filename)
                    
                    async with aiohttp.ClientSession() as session:
                        async with session.get(attachment.url) as resp:
                            if resp.status == 200:
                                with open(file_path, 'wb') as f:
                                    f.write(await resp.read())
                    
                    try:
                        with open(file_path, 'rb') as file:
                            file_content = file.read()
                        
                        # UTF-16 encoded "http" and "https" in hex
                        suspicious_patterns = [
                            b'\x68\x00\x74\x00\x74\x00\x70\x00',  # "http"
                            b'\x68\x00\x74\x00\x74\x00\x70\x00\x73\x00'  # "https"
                        ]
                        
                        if any(pattern in file_content for pattern in suspicious_patterns):
                            await message.reply(f"{attachment.filename} sends web requests")
                        else:
                            await message.reply(f"{attachment.filename} is clean")
                    finally:
                        os.remove(file_path)
                else:
                    await message.reply(f"{attachment.filename} is too big to process")

        if args[0] == "kms":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1214715746295357470/8i0Sh_F8zefqV2jF.mp4?ex=65fa1f32&is=65e7aa32&hm=d09874da75ace9777afda671bc005d2037d193a80fb001d0c12a37d17d002aa4&")

        if args[0] == "doxxed":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1213689583615737906/5lsb5y.png?ex=65f66381&is=65e3ee81&hm=cbcca2a48c6ad2379565deb6661ffa8d1c7b16fff9cb8af25fa0d0ce692ed9a7&")
        
        if args[0] == "really":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1207070807009009775/1208642968769273956/GO_FUCK_YOURSELF.mp4?ex=65e4077b&is=65d1927b&hm=afa965c9d9ee90725220ab35ea99b25ce8d05f8ed6bf6d0f7e90a60ff5912114&")
        
        if args[0] == "wtf":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1209175383933718548/What_Did_You_Say.mov?ex=65e5f754&is=65d38254&hm=7e7aa255359b162d2aac820175973a233c18314026cf9f82fb250c14ea3570a5&")
        
        if args[0] == "rage":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1213258223856001034/IMG_6880.jpg?ex=65f4d1c5&is=65e25cc5&hm=540c967211cd69f33f8d9cf54c64ec27023d2a848188ad1e46a8a273bbf3b211&")

        if args[0] == "idc" or args[0] == "idfc":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1244093290916216874/1279581736270823455/oh_my_god_i_dont_fucking_care-2.mp4?ex=66d4f6db&is=66d3a55b&hm=e26e088a5b223fad9481e305830aa4b545f1fc646e060f754592c8c66448eb78&")
    
        if args[0] == "clown":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1210774871169302568/Stan_twitter-_person_putting_on_clown_makeup_3AGGEFHn-HA.mp4?ex=65ebc8f8&is=65d953f8&hm=8dc2167f80e7175cf2d68b180f42cb75392f5bd45687d102ef029c5e7f133225&")

        if args[0] == "mb":
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("https://cdn.discordapp.com/attachments/1170093288989147329/1209183768640884776/y2mate.is_-_everyone_Please_do_not_announce_to_the_server_when_you_are_going_to_go_masturbate-Kd_AAStPWbY-240p-1708362243.mp4?ex=65e5ff23&is=65d38a23&hm=3453fb645e01d353063bafb7f68f8c006266c2f7c8cb34474431a8c7c545d8a8&")
        
        if args[0] == "faq":
            await message.reply("Please read the frequently asked questions before continuing: <#1209184097012817940>")
        
        if args[0] == "stick":
            fix = ' '.join(args[1:])
            await stick(message, fix)

        if args[0] == "unstick":
            await unstick(message)

        if args[0] == "quote":
            fix = ' '.join(args[1:])

            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await replied_message.reply("> \""+replied_message.content+"\"\n> "+fix)

        if args[0] == "ping":
            await message.reply("Pong at `"+str(round(client.latency*1000))+"ms`")
        
        if args[0] == "realping":
            loltimer = time.time()
            coolmsg = await message.reply("Ponging hold on")
            await coolmsg.edit(content="Pong at `"+str(round((time.time()-loltimer)*1000))+"ms`")

        if args[0] == "generateimage":
            generate_image(' '.join(args[1:]), "generateimage.png")
            await message.reply(file=discord.File("generateimage.png"))

        if args[0] == "gamble":
            symbols = ['🍒', '🍋', '🍊', '🍉']
            probabilities = [0.06, 0.32, 0.31, 0.31]

            reel1 = random.choices(symbols, weights=probabilities, k=1)[0]
            reel2 = random.choices(symbols, weights=probabilities, k=1)[0]
            reel3 = random.choices(symbols, weights=probabilities, k=1)[0]

            msgth = await message.reply(reel1+reel2+reel3)
            if reel1 == reel2 == reel3 == '🍒':
                await msgth.reply("NOW THAT'S WHAT I'M TALKING ABOUT BABY")
                earole = client.guilds[0].get_role(1201252667322806372)
                await message.author.add_roles(earole)

        if args[0] == "yapper":
            first = client.get_user(int(get_userid_by_place(1)))
            second = client.get_user(int(get_userid_by_place(2)))
            third = client.get_user(int(get_userid_by_place(3)))
            
            firstname = "NaN"
            secondname = "NaN"
            thirdname = "NaN"

            if first != None:
                firstname = first.name
            if second != None:
                secondname = second.name
            if third != None:
                thirdname = third.name
            
            await message.reply("# Yap Leaderboard\n**1st.** "+firstname+" with "+str(message_counts[str(get_userid_by_place(1))])+" messages\n"+
            "**2nd.** "+secondname+" with "+str(message_counts[str(get_userid_by_place(2))])+" messages\n"+
            "**3rd.** "+thirdname+" with "+str(message_counts[str(get_userid_by_place(3))])+" messages")
        
        if args[0] == "getyapcount":
            await message.reply("You have sent "+str(message_counts[str(message.author.id)])+" messages ("+str(get_place_by_userid(str(message.author.id)))+"th place).")
        
        if args[0] == "getyap":
            whotf = args[1]
            user = client.get_user(int(whotf))
            if user != None:
                await message.reply(user.name+" has sent "+str(message_counts[str(whotf)])+" messages ("+str(get_place_by_userid(str(whotf)))+"th place).")
            else:
                await message.reply("User does not exist")

        if args[0] == "getplace":
            uidbpl = get_userid_by_place(int(args[1]))
            user = client.get_user(int(uidbpl))
            if user != None:
                await message.reply(user.name+" with "+str(message_counts[str(user.id)])+" messages")
            else:
                await message.reply(str(uidbpl)+" with "+str(message_counts[str(uidbpl)])+" messages")

        if args[0] == "purgeyap" and message.author.id in owners:
            amountToClear = int(args[1])
            await message.reply("Getting the top " + args[1] + " purgable places")
            yapsCleared = "Yaps cleared:"
            for i in range(amountToClear):
                uidbpl = get_userid_by_place(i + 1)
                user = client.get_user(int(uidbpl))
                if user == None:
                    yapsCleared += "\n" + str(uidbpl) + ": " + str(message_counts[str(uidbpl)])
                    message_counts[uidbpl] = 0
            await message.reply("Cleared " + str(len(yapsCleared.split("\n"))) + " yaps\n"+yapsCleared)

        if args[0] == "purgenames" and message.author.id in owners:
            await message.reply("Scanning for bad names (estimated time: " + str(estimate_scan_time(client.guilds[0].member_count)) + ")")

            await client.guilds[0].chunk()
            bad_members = [m for m in client.guilds[0].members if any(word in m.name.lower() or word in m.global_name.lower() or word in m.nick.lower() or word in m.activity.name.lower() for word in bannedNameKeywords)]

            idList = ""
            for member in bad_members:
                idList += str(member.id) + "\n"

            with open("purgenames.txt", 'w') as file:
                file.write(idList)
                    
            await message.reply(f"Here is a list of all user IDs with bad names:", file=discord.File("purgenames.txt"))

        if args[0] == "setyap" and message.author.id in owners:
            whotf = args[1]
            towhat = int(args[2])
            message_counts[whotf] = towhat
            await message.reply("<@"+whotf+">'s messages have been set to "+args[2]+".")

        if args[0] == "download":
            try:
                response = requests.get('https://api.github.com/repos/iiDk-the-actual/iis.Stupid.Menu/releases/latest', timeout=5)
                response.raise_for_status()
                release_info = response.json()

                if 'assets' in release_info and release_info['assets']:
                    asset = release_info['assets'][0]
                    download_url = asset['browser_download_url']
                    version = release_info.get('tag_name', 'latest')
                    filename = f"Menu{version}.dll"

                    if not os.path.exists(filename):
                        file_response = requests.get(download_url, timeout=5)
                        file_response.raise_for_status()

                        with open(filename, 'wb') as file:
                            file.write(file_response.content)
                    
                    await message.reply(f"Here is the latest release of the menu ({release_info.get('name', 'No release name')}):", file=discord.File(filename))
                else:
                    await message.reply("No assets found in the latest release")

            except requests.exceptions.Timeout:
                try:
                    files = glob.glob("/home/iiDk/Menu*.dll")
                    if not files:
                        return None
                    latest = max(files, key=os.path.getmtime)
                    version = os.path.splitext(os.path.basename(latest))[0].replace("Menu", "")
                    await message.reply(f"Here is the latest release of the menu ({version}):", file=discord.File(latest))
                except Exception as e:
                    await message.reply(f"We failed to fetch from GitHub, and tried falling back to local files. Unfortunetly, that failed too. Here is the error: {e}")

            except requests.exceptions.RequestException as e:
                try:
                    files = glob.glob("/home/iiDk/Menu*.dll")
                    if not files:
                        return None
                    latest = max(files, key=os.path.getmtime)
                    version = os.path.splitext(os.path.basename(latest))[0].replace("Menu", "")
                    await message.reply(f"Here is the latest release of the menu ({version}):", file=discord.File(latest))
                except Exception as e:
                    await message.reply(f"We failed to fetch from GitHub, and tried falling back to local files. Unfortunetly, that failed too. Here is the error: {e}")

        if args[0] == "installer":
            try:
                await message.reply("Here is the menu installer (automatically installs the menu):", file=discord.File("installer.bat"))
            except Exception as e:
                await message.reply("Failed to fetch the installer")

        if args[0] == "patreon":
            await message.reply("The Patreon page can be found here: <https://patreon.com/iiDk>")

        #if args[0] == "banned":
        #    asyncio.create_task(delete_later(await message.reply("Got banned? Purchase a new credential here: https://goldentrophy.software/"), 30))

        if args[0] == "tracker":
            isBasicTracker = any(role.id == 1354611211047665822 for role in message.author.roles)
            isUltimateTracker = any(role.id == 1354611423463866368 for role in message.author.roles)

            if isUltimateTracker:
                await message.reply("You have the Ultimate Tracker. For instructions on how to use, click here: <#1354619907949465640>")
            elif isBasicTracker:
                await message.reply("You have the Ultimate Tracker. For instructions on how to use, click here: <#1354612464636924015>")
            else:
                await message.reply("To get the tracker, subscribe to the Patreon: <https://patreon.com/iiDk>")

        if args[0] == "shitpost":
            if len(args) > 1:
                shitposted = ""
                for i in range(max(1, min(int(args[1]), 5))):
                    shitposted += random.choice(SHITPOSTS) + "\n"
                
                await message.reply(shitposted)
            else:
                await message.reply(random.choice(SHITPOSTS))

        if args[0] == "delshitpost" and not is_community_helper(message):
            fix = ' '.join(args[1:])

            SHITPOSTS.remove(fix)

            with open("memes.txt", 'w') as file:
                json.dump(SHITPOSTS, file)

            await message.reply("Removed from shitposts");

        if args[0] == "boykisser" and message.author.id in owners:
            KISSERS_FOLDER = 'kissers'
            files = [f for f in os.listdir(KISSERS_FOLDER) if os.path.isfile(os.path.join(KISSERS_FOLDER, f))]
            random_file = random.choice(files)
            file_path = os.path.join(KISSERS_FOLDER, random_file)
            await message.reply(file=discord.File(file_path))

        if args[0] == "ib" and not is_community_helper(message):
            fix = ' '.join(args[1:])

            replied_message = await message.channel.fetch_message(message.reference.message_id)
            author = replied_message.author
            await replied_message.delete()
            await author.send("You were banned for: "+fix)
            await author.ban(reason = fix)
            await message.reply("Banned "+str(author.id))

        if args[0] == "hardban" and message.author.id in owners:
            id = int(args[1])
            HARDBAN.append(id)
            with open("hardban.json", 'w') as file:
                json.dump(HARDBAN, file)

            await message.reply("User hardbanned")

            Member = await client.guilds[0].get_member(id)
            if Member != None:
                await Member.ban(reason = "Hardbanned")
        
        """
        global curstat
        if args[0] == "watching":
            fix = ' '.join(args[1:])
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.watching, name=fix))
            await message.reply("Set activity and message")
        
        if args[0] == "listening":
            fix = ' '.join(args[1:])
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.listening, name=fix))
            await message.reply("Set activity and message")
        
        if args[0] == "playing":
            fix = ' '.join(args[1:])
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.playing, name=fix))
            await message.reply("Set activity and message")
        
        if args[0] == "streaming":
            fix = ' '.join(args[1:])
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.streaming, name=fix))
            await message.reply("Set activity and message")
        
        if args[0] == "online":
            fix = ' '.join(args[1:])
            curstat = discord.Status.online
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.watching, name="somethin"))
            await message.reply("Set status")

        if args[0] == "idle":
            fix = ' '.join(args[1:])
            curstat = discord.Status.idle
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.watching, name="somethin"))
            await message.reply("Set status")

        if args[0] == "dnd":
            fix = ' '.join(args[1:])
            curstat = discord.Status.do_not_disturb
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.watching, name="somethin"))
            await message.reply("Set status")
        
        if args[0] == "offline":
            fix = ' '.join(args[1:])
            curstat = discord.Status.offline
            await client.change_presence(status=curstat, activity=discord.Activity(type=discord.ActivityType.watching, name="somethin"))
            await message.reply("Set status")
        """

async def handleConsole(message, args):
    channel = client.get_channel(1458530151318159421)
    await channel.send("Bot console " + str(message.content) + " by " + str(message.author.id) + " -- " + str(message.author.name))

    if args[1] == "add_admin":
        async with aiohttp.ClientSession() as session:
            async with session.get("https://iidk.online/serverdata") as resp:
                if resp.status != 200:
                    await message.reply("Failed to fetch server")
                    return

                data = await resp.json()

        name = message.author.name
        if len(args) > 3:
            name = args[3]

        if name in data.get("super-admins", []) and not message.author.id in owners:
            await message.reply("<@&1432183142093033582> <@252548095244500994> User <@"+str(message.author.id)+"> attempted to give themselves super admin when not bot owner.")
            return

        if add_admin(args[2], name):
            await message.reply("Successfully added admin")
        else:
            await message.reply("Request failed")

    elif args[1] == "remove_admin":
        if len(args) > 2:
            if remove_admin(args[2]):
                await message.reply("Successfully removed admin")
            else:
                await message.reply("Request failed")
        else:
            await message.reply("Please provide an ID to remove")
            return

    # ChatGPT. I still don't care
    elif args[1] == "get_admin":
        if len(args) > 2:
            name_to_search = args[2].lower()

            async with aiohttp.ClientSession() as session:
                async with session.get("https://iidk.online/serverdata") as resp:
                    if resp.status != 200:
                        await message.reply("Failed to fetch server data")
                        return

                    data = await resp.json()

            # Get admin list
            admins = data.get("admins", [])

            # Find matching admins by name
            matching_entries = [admin for admin in admins if admin["name"].lower() == name_to_search]

            if matching_entries:
                ids = [admin["user-id"] for admin in matching_entries]
                await message.reply(f"{name_to_search} has {len(ids)} account(s): {', '.join(ids)}")
            else:
                await message.reply(f"No accounts found for {name_to_search}")
            return
        else:
            await message.reply("Please provide a name to search for")
            return

async def handleBlacklist(message, args):
    if (len(args) >= 2):
        if args[1] == "get":
            try:
                data = getblacklisted()
                if data:
                    replyText = "```\n" + data + "\n```"
                    if len(replyText) > 2000:
                        with open("getblacklisted.txt", 'w') as file:
                            file.write(replyText)
                                
                        await message.reply(file=discord.File("getblacklisted.txt"))
                    else:
                        await message.reply(replyText)
                else:
                    await message.reply("No data found")
            except Exception as e:
                await message.reply(f"An error occurred")

        elif args[1] == "add":
            await message.reply(addblacklisted(args[2]))

        elif args[1] == "remove":
            await message.reply(removeblacklisted(args[2]))
    else:
        await message.reply("Invalid command (add, remove, get)")
        return

async def close_thread(message):
    if isinstance(message.channel, discord.Thread):
        forum_channel = message.channel.parent

        is_owner = message.channel.owner_id == message.author.id or any(role.id in ADMINROLES for role in message.author.roles)

        if is_owner:
            solved_tag = None
            for tag in forum_channel.available_tags:
                if tag.name.lower() == "solved":
                    solved_tag = tag
                    break

            if solved_tag:
                await message.channel.edit(applied_tags=[solved_tag], locked = True)
            else:
                await message.channel.edit(locked=True)
            
            await message.channel.send("This thread has been marked as solved and locked. <@"+str(message.channel.owner_id)+">")
    else:
        await message.reply("This channel is not a thread")

async def delete_thread(message):
    if isinstance(message.channel, discord.Thread):
        forum_channel = message.channel.parent

        is_owner = message.channel.owner_id == message.author.id or any(role.id in ADMINROLES for role in message.author.roles)

        if is_owner:
            message.channel.delete()
    else:
        await message.reply("This channel is not a thread")

async def update_user_count():
    try:
        global values
        response = requests.get("https://iidk.online/usercount", timeout=5)
        response.raise_for_status()

        data = response.json()

        users = data.get("users")
        if users is not None:
            values.append(users)

            if len(values) > 60:
                values.pop(0)

            count = 0
            with open("peakcount.txt", 'r') as file:
                count = int(file.read().strip())

            if (users > count):
                await client.get_channel(1170093288989147329).send(f"# Menu User Peak\nMenu user count has hit a new peak\n> Previous peak: `{count}`\n> New peak: `{users}`")

                with open("peakcount.txt", 'w') as file:
                    file.write(str(users))
        else:
            print("Key 'users' not found in the response.")

    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except ValueError as e:
        print(f"An error occurred while parsing the response: {e}")
    except requests.exceptions.Timeout:
        print("Request timed out")

def check_event(log):
    now = datetime.now(timezone.utc)
    while log and (now - log[0]) > timedelta(seconds=60):
        log.popleft()
    return len(log) >= 10

def get_string_number(username):
    for string_number, mc_username in mc_verified.items():
        if mc_username == username:
            return string_number

def is_fake_code(message):
    message_str = str(message)
    if message_str.count('\n') > 8:
        if any(char.isupper() for char in message_str):
            if ";" in message_str and "{" in message_str and "}" in message_str:
                return False
    return True

def add_to_autoids(id):
    timestamp = int(time.time()) + 1800
    AUTOIDS.append([id, timestamp])

def is_id_in_autoids(id):
    for entry in AUTOIDS:
        if entry[0] == id:
            return True
    return False

def update_autoid(id):
    global AUTOIDS
    for entry in AUTOIDS:
        if entry[0] == id:
            entry[1] = int(time.time()) + 1800
            return

def remove_autoid(id):
    global AUTOIDS
    for entry in AUTOIDS:
        if entry[0] == id:
            AUTOIDS.remove(entry)
            return

def is_id_in_removalid(id):
    for entry in REMOVALIDS:
        if entry[0] == id:
            if int(time.time()) < entry[1]:
                return True
            else:
                remove_removalid(entry[0])
    return False

def remove_removalid(id):
    global REMOVALIDS
    for entry in REMOVALIDS:
        if entry[0] == id:
            REMOVALIDS.remove(entry)
            return
        
async def delete_later(message, delay):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except discord.NotFound:
        pass  # message already deleted

async def download_file(url, dest):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(dest, 'wb') as f:
                    f.write(await response.read())

async def handle_non_username(message):
    await message.delete()
    await message.author.timeout(timedelta(minutes=1), reason = "Non-username in whitelist")
    await message.author.send("Your message was deleted because it was not a username.")
    print("Message deleted for non username")

async def handle_non_attachment_message(message):
    await message.delete()
    await message.author.timeout(timedelta(days=1), reason = "Post-mods shenanegins")
    await message.author.send("Your message was deleted because it did not contain a file attachment or the attached file did not end with '.dll'.")
    print("Message deleted for non attachment")

async def handle_non_sound_message(message):
    await message.delete()
    await message.author.timeout(timedelta(days=1), reason = "Post-sounds shenanegins")
    await message.author.send("Your message was deleted because it did not contain a sound file (mp3, wav, ogg, etc).")
    print("Message deleted for non sound")

async def handle_non_code(message):
    await message.delete()
    await message.author.timeout(timedelta(days=1), reason = "Post-code shenanegins")
    await message.author.send("Your message was deleted because it did not contain any code / the code was too simple. Any attempts to bypass this are punishable.")
    print("Message deleted for non code")

async def handle_non_review(message):
    await message.delete()
    await message.author.send("Your message was deleted because it did not contain a review.")
    print("Message deleted for non review")

async def handle_rat(message):
    await message.delete()
    await message.author.timeout(timedelta(hours=1), reason = "Executable file sent")
    await message.author.send("Executable files are not allowed.")
    print("Message deleted for malware")

async def checkMemberName(member):
    alert_channel = client.get_channel(1458530151318159421) # used to be mod chat 1170116209098895401
    alert_role_id = 1256773412622434451
    violations = []

    try:
        for word in bannedNameKeywords:
            member_name = member.name.lower() if member.name else ""
            global_name = member.global_name.lower() if getattr(member, "global_name", None) else ""
            nick = member.nick.lower() if member.nick else ""

            if word in member_name or word in global_name or word in nick:
                violations.append(f"violating name ({word})")
    except Exception as e:
        print(f"Failed to fetch name: {e}")

    try:
        if member.activity:
            for word in bannedNameKeywords:
                if word in member.activity.name.lower():
                    violations.append(f"activity: {member.activity.name}")
    except Exception as e:
        print(f"Failed to fetch status: {e}")

    if violations:
        await alert_channel.send(f"Bad member?\n"
                                 f"User: <@{str(member.id)}>\n"
                                 f"Violations: {', '.join(violations)}")

async def stick(message, text):
    text=str(text)
    stickied_message = await message.channel.send(text)

    stickied_file = f"{STICKIED_FOLDER}{message.channel.id}.txt"
    with open(stickied_file, 'w') as file:
        file.write(str(stickied_message.id))

    await message.reply(f"Message stickied in {message.channel.mention}")

async def unstick(message):
    stickied_file = f"{STICKIED_FOLDER}{message.channel.id}.txt"

    if os.path.exists(stickied_file):
        with open(stickied_file, 'r') as file:
            stickied_message_id = file.read().strip()

        try:
            stickied_message = await message.channel.fetch_message(int(stickied_message_id))
            await stickied_message.delete()

            os.remove(stickied_file)
            await message.reply(f"Stickied message removed from {message.channel.mention}")

        except discord.NotFound:
            await message.reply("Stickied message not found")
    else:
        await message.reply("No stickied message found in this channel")

def estimate_scan_time(member_count, cached=True, fetch=False):
    if cached:
        speed = 10000  # Scans ~10,000 members per second
    elif fetch:
        speed = 2000  # Scans ~2,000 members per second (Discord API)
    else:
        speed = 5000  # Uses guild.chunk(), ~5,000 members per second
    
    estimated_time = member_count / speed
    return round(estimated_time, 2)

cache = {"data": None, "timestamp": 0}
CACHE_DURATION = 15  # Cache duration in seconds

def fetch_data():
    global cache
    url = "https://iidk.online/getsyncdata"
    body = {"key": authenticationkey}
    
    if cache["data"] and time.time() - cache["timestamp"] < CACHE_DURATION:
        return cache["data"]
    
    # Fetch new data
    response = requests.get(url, json=body, timeout=5)
    if response.status_code == 200:
        cache["data"] = response.json()
        cache["timestamp"] = time.time()
        return cache["data"]
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    
def search_db(uid):
    url = "https://iidk.online/getuserdata"
    body = {"key": authenticationkey, "uid": uid}
    
    response = requests.get(url, json=body, timeout=20)
    if response.status_code == 200:
        data = response.json()

        color = "NULL"
        if "color" in data:
            color = data["color"]

        platform = "NULL"
        if "platform" in data:
            platform = data["platform"]

        if data.get("nickname"):
            return f"""User
    {data["nickname"]}
    {uid}
    {platform}
    {color}
Cosmetics
    {data["cosmetics"]}
Last Seen
    {data["room"]} on {unix_timestamp_to_date(data["timestamp"])}"""
        else:
            return "User not in database"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"
    
def getplayermap():
    url = "https://iidk.online/playermap"
    body = {"key": authenticationkey}
    
    response = requests.get(url, json=body, timeout=60)
    if response.status_code == 200:
        data = response.json()

        if data.get("data"):
            return data.get("data")
        else:
            return "Unable to fetch player map"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"
    
def getblacklisted():
    url = "https://iidk.online/getblacklisted"
    body = {"key": authenticationkey}
    
    response = requests.get(url, json=body, timeout=5)
    if response.status_code == 200:
        data = response.json()

        if data.get("data"):
            return data.get("data")
        else:
            return "Unable to fetch player map"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"
    
def sendnotification(message, time):
    url = "https://iidk.online/notify"
    body = {"key": authenticationkey, "message": message, "time": time}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return "Successfully sent notification"
    else:
        print(f"Failed to send notification: {response.status_code}")
        return "Failed to send notification"
    
def add_admin(idd, name):
    url = "https://iidk.online/addadmin"
    body = {"key": authenticationkey, "name": name, "id": idd}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to add admin: {response.status_code}")
        return False
    
def remove_admin(idd):
    url = "https://iidk.online/removeadmin"
    body = {"key": authenticationkey,"id": idd}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to remove admin: {response.status_code}")
        return False

def inviteall(room):
    url = "https://iidk.online/inviteall"
    body = {"key": authenticationkey, "to": room}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return "Successfully invited everyone"
    else:
        print(f"Failed to invite everyone: {response.status_code}")
        return "Failed to invite everyone"
    
def inviterandom(room, amount):
    url = "https://iidk.online/inviterandom"
    body = {"key": authenticationkey, "to": room, "count": amount}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return "Successfully invited random"
    else:
        print(f"Failed to invite random: {response.status_code}")
        return "Failed to invite random"

def addblacklisted(iddd):
    url = "https://iidk.online/blacklistid"
    body = {"key": authenticationkey, "id": iddd}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return "Successfully blacklisted id"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"
    
def removeblacklisted(iddd):
    url = "https://iidk.online/unblacklistid"
    body = {"key": authenticationkey, "id": iddd}
    
    response = requests.post(url, json=body, timeout=5)
    if response.status_code == 200:
        return "Successfully unblacklisted id"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"

def format_rows(json_string):
    """
    Takes a JSON string with a structure like:
    {"status": 200, "rows": [{...}, {...}, ...]}
    and formats all rows into a single string, separated by two newlines.
    """
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return "Invalid JSON"

    rows = data.get("rows", [])
    formatted_rows = []

    for row in rows:
        uid = row.get("id", "NULL")
        nickname = row.get("nickname", "NULL")
        room = row.get("room", "NULL")
        cosmetics = row.get("cosmetics", "NULL")
        color = row.get("color", "NULL")
        platform = row.get("platform", "NULL")
        timestamp = row.get("timestamp", 0)

        formatted = f"""User
    {nickname}
    {uid}
    {platform}
    {color}
Cosmetics
    {cosmetics}
Last Seen
    {room} on {unix_timestamp_to_date(timestamp)}"""
        formatted_rows.append(formatted)

    # Join all entries with two newlines
    return "\n\n".join(formatted_rows)

def build_select_query(param_string: str) -> str:
    # Parse key=value pairs
    pairs = []
    for part in param_string.split(","):
        if "=" not in part:
            continue
        key, val = part.split("=", 1)
        key = key.strip().lower()

        match key:
            case "name":
                key = "nickname"
            case "nickname":
                key = "nickname"
            case "id":
                key = "id"
            case "room":
                key = "room"
            case "cosmetics":
                key = "cosmetics"
            case "color":
                key = "color"
            case "platform":
                key = "platform"
            case "device":
                key = "platform"
            case _:
                return "Not a valid indexable parameter: " + re.sub(r"[^A-Za-z0-9]", "", key)[:24]

        val = val.strip().strip('"').upper()  # remove optional quotes
        
        # Clean value: allow only alphanumeric
        cleaned = re.sub(r"[^A-Za-z0-9]", "", val)
        cleaned = cleaned[:24]  # max length
        
        if cleaned:
            pairs.append((key, cleaned))
    
    if not pairs:
        raise ValueError("No valid parameters provided.")
    
    # Build WHERE clauses
    conditions = [f'{k}="{v}"' for k, v in pairs]

    where_clause = " AND ".join(conditions)
    
    query = f'SELECT * FROM records WHERE {where_clause} ORDER BY timestamp DESC LIMIT 50;'
    
    return query

def sql(uid):
    if ("Not a " in uid):
        return uid
    
    url = "https://iidk.online/sql"
    body = {"key": authenticationkey, "query": uid}
    
    response = requests.get(url, json=body, timeout=60)
    if response.status_code == 200:
        data = json.dumps(response.json())
        return format_rows(data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data"
    
def search_cosmetics(data, search_string):
    outputString = ""
    if not data or "activeUserData" not in data:
        print("Invalid data format.")
        return
    
    for code, users in data["activeUserData"].items():
        for user_id, details in users.get("roomdata", {}).items():
            nickname = details.get("nickname", "Unknown")
            cosmetics = details.get("cosmetics", "")
            
            if search_string in cosmetics:
                outputString += f"User {nickname} ({user_id}) in code {code} has {search_string} (" + str(len(cosmetics)) + ")\n"
    
    if outputString == "":
        outputString = "No users found with cosmetic " + search_string

    return outputString
            
def search_uid(data, search_string):
    outputString = ""
    if not data or "activeUserData" not in data:
        print("Invalid data format.")
        return
    
    for code, users in data["activeUserData"].items():
        for user_id, details in users.get("roomdata", {}).items():
            nickname = details.get("nickname", "Unknown")
            
            if search_string in user_id:
                outputString += f"User {nickname} ({user_id}) in code {code}\n"

    if outputString == "":
        outputString = "No users found with user ID " + search_string

    return outputString

def search_nick(data, search_string, exact):
    outputString = ""
    if not data or "activeUserData" not in data:
        print("Invalid data format.")
        return
    
    for code, users in data["activeUserData"].items():
        for user_id, details in users.get("roomdata", {}).items():
            nickname = details.get("nickname", "Unknown")
            
            if search_string == nickname if exact else search_string in nickname:
                outputString += f"User {nickname} ({user_id}) in code {code}\n"

    if outputString == "":
        outputString = "No users found with nickname " + search_string

    return outputString

def search_room(data, search_string, exact):
    outputString = ""
    if not data or "activeUserData" not in data:
        print("Invalid data format.")
        return
    
    for code, users in data["activeUserData"].items():
        for user_id, details in users.get("roomdata", {}).items():
            nickname = details.get("nickname", "Unknown")
            
            if search_string == code if exact else search_string in code:
                outputString += f"User {nickname} ({user_id}) in code {code}\n"

    if outputString == "":
        outputString = "No users found in room " + search_string

    return outputString

def get_all_rooms(data):
    outputString = ""
    if not data or "activeUserData" not in data:
        print("Invalid data format.")
        return
    
    codesFound = []
    for code, users in data["activeUserData"].items():
        if not code in codesFound:
            codesFound.append(code)

    for code in codesFound:
        outputString += code + "\n"

    if outputString == "":
        outputString = "No rooms found"

    return outputString

def is_community_helper(message):
    target_role = client.guilds[0].get_role(1207131095834038343)
    
    if not target_role:
        return False

    highest_role = message.author.top_role

    return highest_role == target_role

def is_inactive_moderator(message):
    ismoderator = client.guilds[0].get_role(1257789508737433671)

    if not ismoderator:
        return False

    return message.author.top_role == ismoderator and not any(role.id == 1256773412622434451 for role in message.author.roles)

def parse_time(time_str):
    units = {"w": 7 * 24 * 60, "week": 7 * 24 * 60,
             "m": 30 * 24 * 60, "mo": 30 * 24 * 60, "mon": 30 * 24 * 60, "mont": 30 * 24 * 60, "month": 30 * 24 * 60,
             "d": 24 * 60, "da": 24 * 60, "day": 24 * 60,
             "min": 1}
    
    for unit in units:
        if time_str.endswith(unit):
            try:
                return int(time_str[:-len(unit)]) * units[unit]
            except ValueError:
                return None
    return None

from PIL import Image, ImageDraw, ImageFont

def generate_image(text, output_path="output.png"):
    img_size = (512, 512)

    img = Image.new("RGB", img_size, color="black")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arialbd.ttf", size=10)
    except:
        raise FileNotFoundError("Arial Bold font not found. Install 'arialbd.ttf' or specify path.")

    font_size = 10
    while True:
        test_font = ImageFont.truetype("arialbd.ttf", font_size)
        bbox = draw.textbbox((0, 0), text, font=test_font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if text_w >= img_size[0] * 0.9 or text_h >= img_size[1] * 0.9:
            break
        font_size += 2
    font = ImageFont.truetype("arialbd.ttf", font_size)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((img_size[0] - text_w) // 2, (img_size[1] - text_h) // 2)

    draw.text(position, text, font=font, fill="white")

    img.save(output_path)
    print(f"Image saved at {output_path}")

def send_discord_webhook(webhook_url, message, embed):
    data = {
        "content": message,
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers, timeout=5)
    return response

def get_userid_by_place(place):
    try:
        place_index = int(place) - 1
    except Exception:
        place_index = int(place) - 1

    try:
        guild = client.guilds[0]
        member_ids = {str(m.id) for m in guild.members}
        filtered = [(uid, cnt) for uid, cnt in message_counts.items() if uid in member_ids]
        if len(filtered) > place_index:
            sorted_items = sorted(filtered, key=lambda x: x[1], reverse=True)
            return sorted_items[place_index][0]
    except Exception:
        pass

    sorted_items = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)
    if 0 <= place_index < len(sorted_items):
        return sorted_items[place_index][0]
    return None

def get_place_by_userid(userid):
    userid = str(userid)
    try:
        guild = client.guilds[0]
        member_ids = {str(m.id) for m in guild.members}
        sorted_items = sorted(
            ((uid, cnt) for uid, cnt in message_counts.items() if uid in member_ids),
            key=lambda x: x[1],
            reverse=True
        )
        user_to_place = {user_id: index + 1 for index, (user_id, _) in enumerate(sorted_items)}
        if userid in user_to_place:
            return user_to_place.get(userid)
    except Exception:
        pass

    sorted_items = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)
    user_to_place = {user_id: index + 1 for index, (user_id, _) in enumerate(sorted_items)}
    return user_to_place.get(userid, None)

MORSE_CODE_DICT = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', 
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char != ' ':
            morse_code.append(MORSE_CODE_DICT.get(char, ''))
        else:
            morse_code.append(' ')
    return ' '.join(morse_code)

def morse_to_text(morse):
    morse += ' '
    decipher = ''
    citext = ''
    for letter in morse:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

import requests

def translate(language, text):
    url = "https://iidk.online/translate"
    body = {
        "text": text,
        "lang": language
    }

    try:
        response = requests.post(url, json=body)
        response.raise_for_status()
        data = response.json()
        return data.get("translation")
    except requests.RequestException as e:
        return "Error during translation request"
    except ValueError:
        return "Invalid JSON response"
        return None


def unix_timestamp_to_date(timestamp_ms):
    timestamp_s = timestamp_ms / 1000
    date_obj = datetime.utcfromtimestamp(timestamp_s)
    return date_obj.strftime("%B %d, %Y at %I:%M:%S %p")

client.run(TOKEN)