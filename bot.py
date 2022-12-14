import asyncio, pytz
from selfCipherX import Client, models, handlers, methods
from requests import get
import json
import re
import os.path
import logging
from random import choice as ch
import sys
import io, traceback
import sqlite3
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import threading
from os import system as cmd

logging.basicConfig(level=logging.ERROR)

db = sqlite3.connect('CipherX.db')

#db.execute('CREATE TABLE Answer (chat_id TEXT, matn TEXT, javab TEXT)')

#                                       #


lock     = []
dontlock = []
enemy    = []
wanted   = []
mute     = []
game     = []
grou     = []
run      = []

#                                       #


async def main():
    #session = stringSession.StringSession()
    #session.insert(auth='olfviqqyfdeofwesoeiztqjuzquqrfct', guid=None, user_agent=None, phone_number=None)
    async with Client(session='self-bot') as client:
        @client.on(handlers.MessageUpdates())
        async def self(event):
            text = event.raw_text
            if text == None:
                pass
            else:
                objects = event.object_guid
                guid = event.author_guid
                reply = event.reply_message_id
                admin = await client.get_me()
                admins = "u0DJq8b0a3aee63712982de0241d32a0"
                message_id = event.message.message_id
                if text== ".help" and guid == admins:
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        url2 = get("https://api.codebazan.ir/ping/?url=www.google.com").text
                        help_text = f"""
πΎππ₯πππ§π-π½ππ | {url['result']['time']}

β β’ βπππ‘ β¬ (.help) -> Ψ―Ψ³ΨͺΩΨ±Ψ§Ψͺ
β β’ ππ ππ β¬ (.mode) -> ΩΩΨ― ΩΨ§
β β’ ππ π ππ€ β¬ (.tools) -> Ψ§Ψ¨Ψ²Ψ§Ψ± ΩΨ§
β β’ πΌππππͺ β¬ (.enemy) -> Ψ­Ψ§ΩΨͺ Ψ―Ψ΄ΩΩ


α΄Ήα΅ α΄΅α΄° @{admin.user.username}

ππΌππΊ β¬ {url2} ππ΄
"""
                        await event.reply(help_text)
                    except:
                        pass
                if text == ".mode" and guid == admins:
                    try:
                        await event.reply("""
β’ ππ€ππ πππ£πͺ β’

β¬ .time   π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΩΩΨ― ΨͺΨ§ΫΩ
β¬ .tag    π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΩΨ΄ΨͺΪ―
β¬ .emoje  π π - π ππ ->  Ψ­Ψ§ΩΨͺ Ψ§ΫΩΩΨ¬Ϋ
β¬ .emset  π π - π ππ ->  Ψ³Ψͺ Ψ§ΫΩΩΨ¬Ϋ
β¬ .lock   π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΩΩΩ ΩΎΫ ΩΫ
β¬ .copy   π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΩΨͺΩ Ϊ©ΩΎΫ
β¬ .seen   π π - π ππ ->  Ψ­Ψ§ΩΨͺ Ψ³ΫΩ Ψ?ΩΨ―Ϊ©Ψ§Ψ±
β¬ .text1  π π - π ππ -> ΨͺΪ©Ψ³Ψͺ ΩΩΨ―  1
β¬ .group  π π - π ππ -> ΩΨ―Ψ±ΫΨͺ Ϊ―Ψ±ΩΩ
β¬ .text2  π π - π ππ -> ΨͺΪ©Ψ³Ψͺ ΩΩΨ―  2
β¬ .hyper  π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΩΨ§ΫΩΎΨ±
β¬ .Typing π π - π ππ ->  Ψ­Ψ§ΩΨͺ ΨͺΨ§ΫΩΎ Ψ?ΩΨ―Ϊ©Ψ§Ψ±
β¬ .game   π π - π ππ -> Ψ¨Ψ§Ψ²Ϋ Ψ¬ Ψ­
β¬ .timep  π π - π ππ -> ΨͺΨ§ΫΩ ΩΎΨ±ΩΩ
========================


""")
                    except:
                        pass
                if text == ".tools" and guid == admins:
                    try:
                        await event.reply("""
β’ ππ€π€π‘π¨ πππ£πͺ β’

β¬ .font
β¬ .ping
β¬ .bio
β¬ .getlink
β¬ .card
β¬ .date
β¬ .jok
β¬ .pin
β¬ .upin
β¬ .set
β¬ .list
β¬ .clear
β¬ .lock
β¬ .for   | Ψ±ΫΩΎΩΫ
β¬ .py    | Ϊ©Ψ― ΩΎΨ§ΫΨͺΩΩ
β¬ .rmute | Ψ±ΫΩΎΩΫ
β¬ .dmute | Ψ±ΫΩΎΩΫ
β¬ .renemy| Ψ±ΫΩΎΫΩΫ
β¬ .rdel  | Ψ±ΫΩΎΩΫ
β¬ .gad   | Ψ§ΩΨ²ΩΨ―Ω Ψ¨Ω Ψ¨Ψ§Ψ²Ϋ
β¬ .rm    | Ψ­Ψ°Ω Ψ¨Ψ§Ψ²ΫΪ©Ω Ψ§Ψ² Ψ¨Ψ§Ψ²Ϋ
β¬ .msg   | ΩΎΫΨ§Ω Ψ§Ψ―ΩΫΩ
β¬ .getlink | Ψ―Ψ±ΫΨ§ΩΨͺ ΩΫΩΪ© Ϊ―Ψ±ΩΩ
β¬ .deleted | Ψ­Ψ°Ω 25 βΩΎΫΨ§Ω Ψ§Ψ?ΫΨ±
β¬ .answer | Ψ§ΩΨ²ΩΨ―Ω ΩΨͺΩ Ψ¨Ω Ψ¨Ψ§Ψͺ
β¬ .delanswer | Ψ­Ψ°Ω ΩΨͺΩ Ψ§Ψ² Ψ±Ψ¨Ψ§Ψͺ

=================

πΉHELP ANSWER πΉ


β­ .answer Ψ³ΩΨ§Ω:ΪΨ·ΩΨ±Ϋ

πΉ Ψ³ΩΨ§Ω Ψ¨Ω ΨΉΩΩΨ§Ω ΩΨͺΩΫ Ϊ©Ω Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΫΨ?ΩΨ§Ψ― Ψ¨Ϊ―Ω ΩΨ³Ψͺ
πΉ Ω
πΉ ΪΨ·ΩΨ±Ϋ Ψ¨Ω ΨΉΩΩΨ§Ω Ψ¬ΩΨ§Ψ¨ Ψ±Ψ¨Ψ§Ψͺ
πΉ ΨͺΩΫ ΩΨ± Ϊ―Ψ±ΩΩΫ Ψ¨Ψ²ΩΫΨ― Ψ§ΩΩΨ¬Ψ§ ΩΨͺΩ Ψ«Ψ¨Ψͺ ΩΫΨ΄Ω



β­ .delanswer Ψ³ΩΨ§Ω

πΉ ΩΨͺΩΫ Ϊ©Ω ΩΨ¨ΩΨ§ Ψ³ΫΩ Ϊ©Ψ±Ψ―ΫΨ―Ω ΩΎΨ§Ϊ© ΩΫΪ©ΩΩ
πΉ Ψ―Ψ§Ψ?Ω ΩΩΩΩ Ϊ―Ψ±ΩΩ Ψ¨Ψ²ΩΫΨ― Ϊ©Ω ΩΨͺΩΩ ΨͺΩΨ΄ Ψ²Ψ―ΫΨ―

=================
1 - .font [TEXT]

2 - .ping [SITE] google.com

3 - .bio > Bio Random

4 - .card [NUMBER]

5 - .data > Time and Data

6 - .jok > JOK Random

7 - .pin [REPLY]

8 - .unpin [REPLY]

9 - set > SET Group

10 - .list > Llist On Mode

11 - .clear > Clear All Mode On - Off

12 - lock [ON - OFF]

13 - .for [REPLY] > Forwarded Your Post

14 - .py [CODE python Run]

15 - .rmute > Mute Group is @USERNAME

16 - .dmute > unMute Group is @USERNAME

17 - .renemy > Set (Enemy) is [REPLY]

18 - .rdel > unSet (Enemy) is [REPLY]
                        """)
                    except:
                        pass
                if text == ".enemy" and guid == admins:
                    try:
                        await event.reply("""
β’ ππ£ππ’π? πππ£πͺ β’

β¬ .senemy -> Ψ§ΩΨ²ΩΨ―Ω Ψ¨Ω Ψ§ΩΩΫ Ψ¨Ψ§ Ψ§ΫΨ―Ϋ
β¬ .renemy -> Ψ§ΩΨ²ΩΨ―Ω Ψ¨Ω Ψ§ΩΩΫ Ψ¨Ψ§ Ψ±ΫΩΎΩΫ
β¬ .rdel -> Ψ­Ψ°Ω Ψ§ΩΩΫ Ψ¨Ψ§ Ψ±ΫΩΎΩΫ
β¬ .mute -> ΩΫΩΨͺ Ψ¨Ψ§ Ψ§ΫΨ―Ϋ
β¬ .delenemy -> Ψ­Ψ°Ω Ψ§ΩΩΫ Ψ¨Ψ§ Ψ§ΫΨ―Ϋ
β¬ .delmute -> Ψ­Ψ°Ω ΩΫΩΨͺ Ψ¨Ψ§ Ψ§ΫΨ―Ϋ
                        """)
                    except:
                        pass

    #               [  ENEMY  ]                 #

                if text.startswith(".senemy") and guid == admins:
                    command = text.replace(".senemy","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        enemy.append(us.user.user_guid)
                        await event.reply(f"πππ πππ£ππ’π?\n{command}")
                    except:
                        pass
                if guid in enemy:
                    try:
                        with open('Enemy/Fosh', 'r') as foshE:
                            ask = ch(foshE.readlines()).strip()
                            await event.reply(ask)
                    except:
                        pass
                if text.startswith(".delenemy") and guid == admins:
                    command = text.replace(".delenemy","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        enemy.remove(us.user.user_guid)
                        await event.reply(f"ππ£ππ’π? πΏππ‘ππππΏ\n{command}")
                    except:
                        await event.reply(f"ππ¨ππ§π£ππ’π ππ€π© πππ£π\n{command}")
                if text.startswith(".renemy") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        enemy.append(us.user.user_guid)
                        await event.reply(f"πππ πππ£ππ’π?\n@{us.user.username}")
                    except:
                        pass
                if text.startswith(".rdel") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        enemy.remove(us.user.user_guid)
                        await event.reply(f"ππ£ππ’π? πΏππ‘ππππΏ\n@{us.user.username}")
                    except:
                        await event.reply(f"ππ¨ππ§π£ππ’π ππ€π© πππ£π\n@{us.user.username}")


            #       [ MODE ]     #

                if os.path.exists("Mode/Bold"):
                    mode = open("Mode/Bold").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"**{text}**") # BOLD MODE
                    except:
                        pass
                if text.startswith(".bold") and guid == admins:
                    command = text.replace(".bold","").strip()
                    if command == "on" or "off":
                        open("Mode/Bold","w").write(command)
                        await event.reply(f"**BOLD** ππ€ππ {command}")

                if os.path.exists("Mode/Hyper"):
                    mode = open("Mode/Hyper").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "Group":
                            if event.message.reply_to_message_id:
                                us = await client(methods.messages.GetMessagesByID(objects,message_ids=event.message.reply_to_message_id))
                                await event.edit(f"[{text}]({us.messages[0].author_object_guid})")
                            else:
                                await event.edit(f"[{text}]({guid})")
                    except:
                        pass
                if text.startswith(".hyper") and event.type == "Group" and guid == admins:
                    command = text.replace(".hyper","").strip()
                    if command == "on" or "off":
                        open("Mode/Hyper","w").write(command)
                        await event.reply(f"[HyperS]({guid}) ππ€ππ {command}")

                if os.path.exists("Mode/copy"):
                    mode = open("Mode/copy").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"`{text}`")
                    except:
                        pass
                if text.startswith(".copy") and guid == admins:
                    command = text.replace(".copy","").strip()
                    if command == "on" or "off":
                        open("Mode/copy","w").write(command)
                        await event.reply(f"`CopyEs` ππ€ππ {command}")

                if os.path.exists("Mode/Typing"):
                    mode = open("Mode/Typing").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if text:
                            await client(methods.chats.SendChatActivity(objects))
                    except:
                        pass
                if text.startswith(".typing") and guid == admins:
                    command = text.replace(".typing","").strip()
                    if command == "on" or "off":
                        open("Mode/Typing","w").write(command)
                        await event.reply(f"**Typing** ππ€ππ {command}")

                if os.path.exists("Mode/TIME"):
                    mode = open("Mode/TIME").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.edit(f"~> {url['result']['time']} <~ \n{text}")
                    except:
                        pass

                if text.startswith(".time") and guid == admins:
                    command = text.replace(".time","").strip()
                    if command == "on" or "off":
                        open("Mode/TIME","w").write(command)
                        await event.reply(f"**TIME** ππ€ππ {command}")

                if os.path.exists("Mode/Tags"):
                    mode = open("Mode/Tags").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        texts = re.sub(" ","_",text)
                        await event.edit(f"#{texts}")
                    except:
                        pass

                if text.startswith(".tag") and guid == admins:
                    command = text.replace(".tag","").strip()
                    if command == "on" or "off":
                        open("Mode/Tags","w").write(command)
                        await event.reply(f"#TAGS ππ€ππ {command}")

                if os.path.exists("Mode/Emoje"):
                    mode = open("Mode/Emoje").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        items = open("Mode/SetEm").read()
                        await event.edit(f"{text} {items}")
                    except:
                        pass
                if text.startswith(".emoje") and guid == admins:
                    command = text.replace(".emoje","").strip()
                    if command == "on" or "off":
                        open("Mode/Emoje","w").write(command)
                        await event.reply(f"**EMOJES**ππΏ ππ€ππ {command}")
                if text.startswith(".emset"):
                    command = text.replace(".emset", "")
                    open("Mode/SetEm","w").write(command)
                    await event.reply(f"ππ’π€πππ¨ πππ {command}")

                if os.path.exists("Mode/:)"):
                    mode = open("Mode/:)").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"{text} `:)`")
                    except:
                        pass
                if text.startswith(".text1") and guid == admins:
                    command = text.replace(".text1","").strip()
                    if command == "on" or "off":
                        open("Mode/:)","w").write(command)
                        await event.reply(f":) ππ€ππ {command}")
                if os.path.exists("Mode/Seen"):
                    mode = open("Mode/Seen").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "User" or event.type == "Group":
                            try:
                                await event.seen()
                            except:
                                pass
                    except:
                        pass
                if text.startswith(".seen") and guid == admins:
                    command = text.replace(".seen","").strip()
                    if command == "on" or "off":
                        open("Mode/Seen","w").write(command)
                        await event.reply(f"**SEEN** ππ€ππ {command}")

                if os.path.exists("Mode/Game"):
                    mode = open("Mode/Game").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "Group":
                            try:
                                if event.object_guid in grou:
                                    if text == "Ψ¨ΩΎΨ±Ψ³":
                                        print(f"{objects} => {text}")
                                        if guid in game:
                                            with open('game.txt', 'r') as games:
                                                ask = ch(games.readlines()).strip()
                                                await event.reply(ask)
                            except:
                                pass
                    except:
                        pass
                if text.startswith(".game") and guid == admins:
                    command = text.replace(".game","").strip()
                    if command == "on" or "off":
                        open("Mode/Game","w").write(command)
                        await event.reply(f"**GAMES** ππ€ππ {command}")

                if text == ".gad" and guid == admins:
                    try:
                        grou.append(objects)
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        game.append(us.user.user_guid)
                        await event.delete_messages()
                        await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ¨Ω Ψ¨Ψ§Ψ²Ϋ Ψ§ΨΆΨ§ΩΩ Ψ΄Ψ―

Ψ¨Ψ±Ψ§Ϋ ΩΎΨ±Ψ³Ψ΄ Ψ§Ψ² Ϊ©ΩΩΩ ( Ψ¨ΩΎΨ±Ψ³ ) Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ϊ©ΩΫΨ―
    """,reply_to_message_id=event.message.reply_to_message_id))
                    except:
                        pass

                if text == ".rm" and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        game.remove(us.user.user_guid)
                        await event.delete_messages()
                        await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ§Ψ² Ψ¨Ψ§Ψ²Ϋ Ψ­Ψ°Ω Ψ΄Ψ―
    """,reply_to_message_id=event.message.reply_to_message_id))
                    except:
                        pass

                if text.startswith("Ϊ©Ϋ Ϊ©ΩΩΫΩ") and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"Ψ§ΫΩ [ {name}]({random.member_guid}) Ϊ©ΩΩΫΩ πΆββοΈπ")

                    except:
                        pass

                if text.startswith("Ϊ©Ϋ Ψ?Ψ±Ω") and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"Ψ§ΫΩ [ {name}]({random.member_guid}) Ψ?Ψ±Ω ππ")

                    except:
                        pass
                if text == "Ϊ©Ϋ Ψ¨Ψ§ Ϊ©Ϋ Ψ±Ω ΩΫΨ²ΩΩ" or text == "Ϊ©ΫΨ§ Ψ±Ω ΩΫΨ²ΩΩ" or text == "Ϊ©Ϋ Ψ¨Ψ§ Ϊ©Ϋ Ψ±Ω ΩΫΨ²ΩΨΉ" or text == "Ϊ©Ϋ Ψ¨Ψ§ΨΉ Ϊ©Ϋ Ψ±Ω ΩΫΨ²ΩΨΉ" and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        for i in range(2):
                            random = ch(dialogs.in_chat_members)
                            random1 = ch(dialogs.in_chat_members)
                            name = random.first_name
                            name1 = random1.first_name
                        if name == name1:
                            await event.delete_messages()
                        else:
                            await event.reply(f"""
Ψ§ΫΩ [ {name}]({random.member_guid})

Ψ¨Ψ§ Ψ§ΫΩ [ {name1}]({random1.member_guid})

Ψ±Ω ΩΫΨ²ΩΩ β€οΈπΏ
                        """)
                    except:
                        pass

                if text == "Ϊ©Ϋ Ϊ©ΫΩ ΩΫΪ©ΩΩ" or text == "Ϊ©Ϋ ΩΫΪ©ΩΩ" or text == "Ϊ©Ϋ Ψ§ΩΩ ΫΪ©ΫΩ ΩΫΪ©ΩΩ" or text == "Ϊ©Ϋ Ϊ©ΫΩ ΩΫΪ©ΩΨΉ" and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        for i in range(2):
                            random = ch(dialogs.in_chat_members)
                            random1 = ch(dialogs.in_chat_members)
                            name = random.first_name
                            name1 = random1.first_name
                        if name == name1:
                            await event.delete_messages()
                        else:
                            await event.reply(f"""
Ψ§ΫΩ [ {name}]({random.member_guid})

Ψ§ΫΩΩ ΩΫΪ©ΩΩ [ {name1}]({random1.member_guid}) π¦

                        """)
                    except:
                        pass

                if text == "Ϊ©Ϋ Ψ¨Ψ§Ω Ψ±Ω ΩΫΨ²ΩΩ" or text == "Ϊ©Ϋ Ψ¨Ψ§ΩΨ§Ω Ψ±Ω ΩΫΨ²ΩΨΉ" or text == "Ϊ©Ϋ Ψ¨Ψ§ΩΨ§Ω Ψ±Ω ΩΫΨ²ΩΩ" or text == "Ϊ©Ϋ Ψ±Ω ΩΫΨ²ΩΩ" or text == "Ϊ©Ϋ Ψ¨Ψ§Ω Ψ±Ω ΩΫΨ²ΩΨΉ":
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"Ψ§ΫΩ [ {name}]({random.member_guid}) Ψ¨Ψ§ΩΨ§Ψͺ Ψ±Ω ΩΫΨ²ΩΩ")
                    except:
                        pass

                if os.path.exists("Mode/text2"):
                    mode = open("Mode/text2").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"{text} `:/`")
                    except:
                        pass
                if text.startswith(".text2") and guid == admins:
                    command = text.replace(".text2","").strip()
                    if command == "on" or "off":
                        open("Mode/text2","w").write(command)
                        await event.reply(f":/ ππ€ππ {command}")

                if os.path.exists("Mode/Lock"):
                    mode = open("Mode/Lock").read()
                else:
                    mode = "off"
                if mode == "on":
                    if event.type == "User" and not guid == admins:
                        salm = dontlock.count(event.object_guid)
                        if salm == 1:
                            pass
                        else:
                            lock.append(event.object_guid)
                            us = await client(methods.users.GetUserInfo(event.object_guid))
                            t = lock.count(event.object_guid)
                            if t == 1:
                                await event.reply(f"β’ πΎππ₯πππ§π-π½ππ β’\nΨ§Ψ?Ψ·Ψ§Ψ± (1/5) β\n\nΪ©Ψ§Ψ±Ψ¨Ψ± @{us.user.username}\nΨ§Ψ² Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω Ψ?ΩΨ―Ψ―Ψ§Ψ±Ϋ Ϊ©ΩΫΨ―. Ψ―Ψ± ΨΊΫΨ± Ψ§ΫΩ Ψ΅ΩΨ±Ψͺ Ψ΄ΩΨ§ Ψ¨ΩΨ§Ϊ© Ψ?ΩΨ§ΩΫΨ― Ψ΄Ψ―.")
                            if t == 2:
                                await event.reply(f"β’ πΎππ₯πππ§π-π½ππ β’\nΨ§Ψ?Ψ·Ψ§Ψ± (2/5) β\n\nΪ©Ψ§Ψ±Ψ¨Ψ± @{us.user.username}\nΨ§Ψ² Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω Ψ?ΩΨ―Ψ―Ψ§Ψ±Ϋ Ϊ©ΩΫΨ―. Ψ―Ψ± ΨΊΫΨ± Ψ§ΫΩ Ψ΅ΩΨ±Ψͺ Ψ΄ΩΨ§ Ψ¨ΩΨ§Ϊ© Ψ?ΩΨ§ΩΫΨ― Ψ΄Ψ―.")
                            if t == 3:
                                await event.reply(f"β’ πΎππ₯πππ§π-π½ππ β’\nΨ§Ψ?Ψ·Ψ§Ψ± (3/5) β\n\nΪ©Ψ§Ψ±Ψ¨Ψ± @{us.user.username}\nΨ§Ψ² Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω Ψ?ΩΨ―Ψ―Ψ§Ψ±Ϋ Ϊ©ΩΫΨ―. Ψ―Ψ± ΨΊΫΨ± Ψ§ΫΩ Ψ΅ΩΨ±Ψͺ Ψ΄ΩΨ§ Ψ¨ΩΨ§Ϊ© Ψ?ΩΨ§ΩΫΨ― Ψ΄Ψ―.")
                            if t == 4:
                                await event.reply(f"β’ πΎππ₯πππ§π-π½ππ β’\nΨ§Ψ?Ψ·Ψ§Ψ± (4/5) β\n\nΪ©Ψ§Ψ±Ψ¨Ψ± @{us.user.username}\nΨ§Ψ² Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω Ψ?ΩΨ―Ψ―Ψ§Ψ±Ϋ Ϊ©ΩΫΨ―. Ψ―Ψ± ΨΊΫΨ± Ψ§ΫΩ Ψ΅ΩΨ±Ψͺ Ψ΄ΩΨ§ Ψ¨ΩΨ§Ϊ© Ψ?ΩΨ§ΩΫΨ― Ψ΄Ψ―.")
                            if t == 5:
                                await event.reply(f"Ϊ©Ψ§Ψ±Ψ¨Ψ± @{us.user.username}\nΨ¨Ω Ψ―ΩΫΩ Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω ΩΪ©Ψ±Ψ± Ψ¨ΩΨ§Ϊ© Ψ΄Ψ―.")
                                await client(methods.users.SetBlockUser(event.object_guid))
                if text.startswith(".lock") and guid == admins:
                    command = text.replace(".lock","").strip()
                    if command == "on" or "off":
                        open("Mode/Lock","w").write(command)
                        await event.reply(f"**LOCK** ππ€ππ {command}")
                if text.startswith("Unlock") and guid == admins:
                    try:
                        dontlock.append(objects)
                        us = await client(methods.users.GetUserInfo(objects))
                        await event.reply(f"Ϊ©Ψ§Ψ±Ψ¨Ψ± [ @{us.user.username} ]\nΩΫΨͺΩΨ§ΩΫΨ― ΩΎΫΨ§Ω Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― .")
                    except:
                        pass
                if text.startswith("Lock") and guid == admins:
                    try:
                        dontlock.remove(objects)
                        await event.delete_messages()
                    except:
                        pass
                if text.startswith(f"@{admin.user.username}") and event.type == "Group":
                    try:
                        await event.reply(f"[Bal ?]({guid})")
                        await client(methods.messages.ForwardMessages(objects, admin.user.user_guid, message_ids=event.message_id))
                    except:
                        pass

    #           [ Group ]       #


                if text.startswith(".set") and guid == admins:
                    try:
                        open("Mode/Set","w").write(event.object_guid)
                        await event.reply("ππ§π€πͺπ₯ πππ ππ€π€π‘π¨ βοΈ")
                    except:
                        pass

                if text.startswith(".group") and guid == admins:
                    try:
                        command = text.replace(".group","").strip()
                        open("Mode/Group","w").write(command)
                        await event.reply(f"ππ§π€πͺπ₯ ππ€πΏπ {command}")
                    except:
                        pass
                if os.path.exists("Mode/Group"):
                    mode = open("Mode/Group").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        chat_id = open("Mode/Set").read()
                        if objects == chat_id:

                            if event.find_keys(keys=['event_data']):
                                try:
                                    if event.message.event_data.type == "RemoveGroupMembers":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})
Ψ§Ψ² Ϊ―Ψ±ΩΩ Ψ¨Ω Ψ΄Ψ― .
    """)
                                    if event.message.event_data.type == "AddedGroupMembers":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        groups = await client(methods.groups.GetGroupInfo(event.object_guid))
                                        #print(group.jsonify(indent=2))
                                        await event.reply(f"""
Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})
Ψ¨Ω Ϊ―Ψ±ΩΩ ΩΨ§ Ψ?ΩΨ΄ Ψ§ΩΩΨ―Ϋ .
    """)
                                    if event.message.event_data.type == "LeaveGroup":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
Ψ―Ψ§Ψ΄ [{us.user.first_name}]({us.user.user_guid})
Ψ¨ Ϊ©ΫΨ±Ω Ϊ© ΩΩ Ψ―Ψ§Ψ―Ϋ :/
                                        """)
                                    if event.message.event_data.type == "JoinedGroupByLink":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
Ϊ©Ψ§Ψ±Ψ¨Ψ± [{us.user.first_name}]({us.user.user_guid})
Ψ¨Ω Ϊ―Ψ±ΩΩ ΩΨ§ Ψ?ΩΨ΄ Ψ§ΩΩΨ―Ϋ .

                                        """)
                                except:
                                    pass
                            g = re.findall(r"https://rubika.ir/joing/\w{32}",text)
                            for gr in g:
                                await event.delete_messages()
                            c = re.findall(r"https://rubika.ir/joinc/\w{32}",text)
                            for cr in c:
                                await event.delete_messages()
                    except:
                        pass

                if text.startswith("Ψ§Ψ?Ψ·Ψ§Ψ±") and event.type == "Group" and guid == admins:
                    try:

                        command = text.replace("Ψ§Ψ?Ψ·Ψ§Ψ±","").strip()
                        await event.delete_messages()
                        info = await client(methods.messages.GetMessagesByID(objects,event.message.reply_to_message_id))
                        us = await client(methods.users.GetUserInfo(info.author_object_guid))
                        wanted.append(us.user.user_guid)
                        total = wanted.count(us.user.user_guid)
                        if total == 1:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ―ΩΫΩ : {command}


βΊβΊβΊ Ψ΄ΩΨ§ [ 1/3 ] Ψ§Ψ?Ψ·Ψ§Ψ± Ψ―Ψ±ΫΨ§ΩΨͺ Ϊ©Ψ±Ψ―ΫΨ―.
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 2:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ―ΩΫΩ : {command}


βΊβΊβΊ Ψ΄ΩΨ§ [ 2/3 ] Ψ§Ψ?Ψ·Ψ§Ψ± Ψ―Ψ±ΫΨ§ΩΨͺ Ϊ©Ψ±Ψ―ΫΨ―.
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 3:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ―ΩΫΩ : {command}


βΊβΊβΊ Ψ΄ΩΨ§ [ 3/3 ] Ψ§Ψ?Ψ·Ψ§Ψ± Ψ―Ψ±ΫΨ§ΩΨͺ Ϊ©Ψ±Ψ―ΫΨ―.

βΊβΊβΊβΊ Ψ¨Ω Ψ―ΩΫΩ Ψ―Ψ±ΫΨ§ΩΨͺ [ 3 ] Ψ§Ψ?Ψ·Ψ§Ψ± ΩΫΩΨͺ ΩΫΨ΄ΩΫΨ―
    """,reply_to_message_id=event.message.reply_to_message_id))
                                mute.append(us.user.user_guid)
                            except:
                                pass
                    except:
                        pass
                if text.startswith("Ψ­Ψ°Ω Ψ§Ψ?Ψ·Ψ§Ψ±") and guid == admins:
                    try:
                        info = await client(methods.messages.GetMessagesByID(objects,event.message.reply_to_message_id))
                        us = await client(methods.users.GetUserInfo(info.author_object_guid))
                        wanted.remove(us.user.user_guid)
                        total = wanted.count(us.user.user_guid)

                        if total == 0:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ§Ψ?Ψ·Ψ§Ψ± ΩΨ§Ϋ Ψ΄ΩΨ§ [ 0/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 1:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ§Ψ?Ψ·Ψ§Ψ± ΩΨ§Ϋ Ψ΄ΩΨ§ [ 1/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 2:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ§Ψ?Ψ·Ψ§Ψ± ΩΨ§Ϋ Ψ΄ΩΨ§ [ 2/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 3:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
βΊ Ϊ©Ψ§Ψ±Ψ¨Ψ± [ {us.user.first_name}]({us.user.user_guid})

βΊβΊ Ψ§Ψ?Ψ·Ψ§Ψ± ΩΨ§Ϋ Ψ΄ΩΨ§ [ 3/3 ]

βΊβΊβΊ Ψ¨Ω ΩΩΫΩ Ψ―ΩΫΩ Ψ΄ΩΨ§ Ψ§Ψ?Ψ±Ψ§Ψ¬ ΩΫΨ΄ΩΫΨ― .
    """,reply_to_message_id=event.message.reply_to_message_id))

                            except:
                                pass
                    except:
                        pass
                if text.startswith(".mute ") and guid == admins:
                    command = text.replace(".mute","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        mute.append(us.user.user_guid)
                        await event.reply(f"ππͺππ πππ\n{command}")
                    except:
                        pass
                if guid in mute:
                    try:
                        if event.type == "Group":
                            us = await client(methods.users.GetUserInfo(event.message.author_object_guid))
                            await event.delete_messages()
                            print(f"{us.user.first_name} \033[32mPAK \033[35mSHOD => \033[31m {text}")
                    except:
                        pass
                if text.startswith(".delmute ") and guid == admins:
                    command = text.replace(".delmute ","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        mute.remove(us.user.user_guid)
                        await event.reply(f"ππͺππ πΏππ‘ππππΏ\n{command}")
                    except:
                        pass
                if text.startswith(".rmute") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        mute.append(us.user.user_guid)
                        await event.reply(f"ππͺππ πππ\n@{us.user.username}")
                    except:
                        pass
                if text.startswith(".rdmute") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        mute.remove(us.user.user_guid)
                        await event.reply(f"ππͺππ πΏππ‘ππππΏ\n@{us.user.username}")
                    except:
                        pass


    #               [ TOOLS ]         #


                if text.startswith("Ψ§Ψ―") and guid == admins:
                    try:
                        if event.type == "Group":
                            ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                            us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                            await client(methods.groups.SetGroupAdmin(objects,us.user.user_guid,access_list=['PinMessages','DeleteGlobalAllMessages']))
                            await event.reply(f"[ {us.user.first_name}]({us.user.user_guid}) Ψ§Ψ― Ψ΄Ψ―Ϋ ππ«")
                    except:
                        pass

                if text.startswith(".id") and guid == admins:
                    try:
                        if event.type == "Group":
                            ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                            us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                            await event.reply(f"`{us.user.user_guid}`\n[ {us.user.first_name}]({us.user.user_guid})")
                        if event.type == "User":
                            us = await client(methods.users.GetUserInfo(objects))
                            await event.reply(f'`{us.user.user_guid}`')
                    except:
                        pass

                if text.startswith(".getlink") and guid == admins:
                    try:
                        if event.type == "Group":
                            links = await client(methods.groups.GetGroupLink(objects))
                            await event.reply(f"""
ΩΫΩΪ© Ϊ―Ψ±ΩΩ ππ«

**LINKS** {links.join_link}
    """)
                    except:
                        pass

                if text.startswith(".info") and guid == admins:
                    try:
                        groups = await client(methods.groups.GetGroupInfo(objects))
                        if groups.group.event_messages == True:
                            texts = "Yes"
                        else:
                            texts = "No"
                        await event.reply(f"""
β’ ππ―π¬π²π πππ±π β’

βπππ: {groups.group.group_title}
ππππππ£π€: {groups.group.count_members}
π»ππ€ππ£ππ‘π₯ππ π: {groups.group.description}
πππ©π₯ π»π ππ₯ ππππ: {groups.chat.count_unseen}
πΈππππ€π€ πππ€π€πππ: {texts}
πππ π¨ ππ ππ: {groups.group.slow_mode}s
    """)
                    except:
                        pass
                if text.startswith(".ping") and guid == admins:
                    try:
                        ping = get(f"https://api.codebazan.ir/ping/?url=www.{text.replace('.ping ','').strip()}").text
                        await event.reply(f"πππ£ππ¨ ππππ : {ping}π π")
                    except:
                        pass
                if text.startswith(".bio") and guid == admins:
                    try:
                        url = get("https://api.codebazan.ir/bio/").text
                        await event.reply(f"β’ π½ππ€ πππ£πΏπ€π’ β’ \n{url}")
                    except:
                        pass

                if text.startswith(".font ") and guid == admins:
                    try:
                        url = get(f"https://api.codebazan.ir/font/?text={text.replace('.font','')}").json()
                        await event.reply(f"\n".join(list(url["result"].values())[:110]))
                    except:
                        pass
                if text.startswith(".date") and guid == admins:
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.reply(f"""
β’ ππ¦ππ’π ππππ’ β’

ππππΌπ€: {url['result']['time']}
π»πππ: {url['result']['date']}
π½ππ€π: {url['result']['fasl']}
πππ: {url['result']['mahname']}
ππππβπππ: {url['result']['weekname']}

                    """)
                    except:
                        pass
                if text.startswith(".list") and guid == admins:
                    try:
                        hyper = open("Mode/Hyper").read()
                        copy  = open("Mode/copy").read()
                        Group = open("Mode/Group").read()
                        Lock  = open("Mode/Lock").read()
                        Tags  = open("Mode/Tags").read()
                        Text2 = open("Mode/text2").read()
                        TIME  = open("Mode/TIME").read()
                        Bold  = open("Mode/Bold").read()
                        seens = open("Mode/Seen").read()
                        games = open("Mode/Game").read()

                        tping = open("Mode/Typing").read()
                        await event.reply(f"""
β’ π π²π»π ππΆππ β’

π·π’πππ: {hyper}
π²πππ’: {copy}
πΆππππ: {Group}
π»πππ: {Lock}
ππππ: {Tags}
πππ‘ππΈ: {Text2}
πππΌπ: {TIME}
π±πππ: {Bold}
**SEEN**: {seens}
**Typing**: {tping}
    """)
                    except:
                        pass
                if text.startswith(".clear"):
                    try:
                        hyper = open("Mode/Hyper","w").write("off")
                        copy  = open("Mode/copy","w").write("off")
                        Group = open("Mode/Group","w").write("off")
                        Lock  = open("Mode/Lock","w").write("off")
                        Tags  = open("Mode/Tags","w").write("off")
                        Text2 = open("Mode/text2","w").write("off")
                        TIME  = open("Mode/TIME","w").write("off")
                        Bold  = open("Mode/Bold","w").write("off")
                        seens = open("Mode/Seen","w").write("off")
                        games = open("Mode/Game","w").write("off")
                        tping = open("Mode/Typing","w").write("off")
                        await event.reply(f"""
β’ Clear All Methods CIPHER-X


β’ Successfully β’

β’ π π²π»π β’

π·π’πππ: off
π²πππ’: off
πΆππππ: off
π»πππ: off
ππππ: off
πππ‘ππΈ: off
πππΌπ: off
π±πππ: off
**SEEN**: off
**Typing**: off
""")

                    except:
                        pass
                if text.startswith(".for"):
                    dialogs = await client(methods.chats.GetChats(start_id=None))
                    if dialogs.chats:
                        total = len(dialogs.chats)
                        successful = 0
                        unsuccessful = 0
                        message = await event.reply(f'ΨͺΨΉΨ―Ψ§Ψ― {total} ΪΨͺ ΩΎΫΨ―Ψ§ Ψ΄Ψ― Ψ΄Ψ±ΩΨΉ ΩΨ±Ψ§ΫΩΨ― Ψ§Ψ±Ψ³Ψ§Ω ...')
                        for index, dialog in enumerate(dialogs.chats, start=1):
                            if methods.groups.SendMessages in dialog.access:
                                try:
                                    if event.type == "Group" or event.type == "User":
                                        await event.forwards(dialog.object_guid, message_ids=event.reply_message_id)
                                        successful += 1

                                except Exception:
                                    unsuccessful += 1

                                progress = '|'
                                filled = int(index * 15 / total)
                                progress += 'β' * filled
                                progress += '-' * (15 - filled)
                                progress += '| βββ'
                                progress += f' [{int(index * 100 / total):,}%]'

                                await message.reply(
                                    f'ΨͺΨΉΨ―Ψ§Ψ― {index:,} ΪΨͺ Ψ§Ψ² {total:,} ΪΨͺ Ψ¨Ψ±Ψ±Ψ³Ϋ Ψ΄Ψ―Ω Ψ§Ψ³Ψͺ'
                                    f'\nΩΩΩΩ : {successful:,}\nΩΨ§ΩΩΩΩ: {unsuccessful:,}\n\n{progress}'
                                )
                    else:
                        await event.reply('Ψ―Ψ± Ψ¬Ψ³ΨͺΨ¬ΩΫ ΪΨͺ ΩΨ§ Ψ¨Ψ§ Ψ΄Ϊ©Ψ³Ψͺ ΩΩΨ§Ψ¬ΨΉΩ Ψ΄Ψ―')
                if text.startswith(".run") and guid == admins:
                    try:
                        run.append(objects)
                        await event.reply(event)

                    except:
                        print("ERR line 958")
                if objects in run:
                    try:
                        print(event)
                    except:
                        print("ERR")
                if text.startswith(".sid"):
                    command = text.replace(".sid","").strip()
                    await client(methods.settings.UpdateUsername(username=command))
                    await event.reply(f"**SET Your ID** -> `{command}`")

                if text.startswith(".py") and guid == admins:
                    Code = text.replace(".py\n","")
                    old_stderr = sys.stderr
                    old_stdout = sys.stdout
                    redirected_output = sys.stdout = io.StringIO()
                    redirected_error = sys.stderr = io.StringIO()
                    stdout, stderr, exc = None, None, None
                    async def aexec(code, event):
                        exec(
                        f"async def __aexec(event, client): "
                        + "\n chatid = event.object_guid"
                        + "".join(f"\n {l}" for l in code.split("\n")),
                        )
                        return await locals()['__aexec'](event,client)
                    try:
                        returned = await aexec(Code,event)
                    except Exception:
                        exc = traceback.format_exc()
                    stdout = redirected_output.getvalue().strip()
                    stderr = redirected_error.getvalue().strip()
                    sys.stdout = old_stdout
                    sys.stderr = old_stderr
                    evaluation = exc or stderr or stdout or returned
                    try:
                        if evaluation:
                            await event.reply("**Query**πΉ \n\n"
                            f"{Code}\n"
                            "\n**Result** πΊ \n\n"
                            f"{evaluation}"
                            "")
                        else:
                            await event.reply("**Query**:\n\n"
                            f"{Code}"
                            "\nResult: \nNo Result Returned/False")
                    except Exception as err:
                        await event.reply("**Query** π·\n"
                        f"{Code}"
                        "\nException πΊ\n"
                        f"{err}")
                if text.startswith(".answer") and guid == admins:
                    try:
                        command = text.replace(".answer", "").strip()
                        MyA = command.split(":")
                        db.execute('INSERT INTO Answer (chat_id, matn, javab) VALUES (?, ?, ?)', (event.object_guid, MyA[0], MyA[1]))
                        db.commit()
                        await event.reply(f'πΉ ΩΨͺΩ Ψ¬Ψ―ΫΨ― Ψ¨Ψ§ ΩΩΩΩΫΨͺ Ψ§ΩΨ²ΩΨ―Ω Ψ΄Ψ― πΉ\nπΊ ΩΨͺΩ :β {MyA[0]}\nπΊ Ψ¬ΩΨ§Ψ¨ : {MyA[1]}')
                    except:
                        pass
                data_Answer = db.execute('SELECT * FROM Answer').fetchall()
                for OyA in data_Answer:
                    if text == OyA[1] and event.object_guid in OyA[0]:
                        if event.type == "Group" and not guid == admins:
                            await event.reply(OyA[2])


                if text.startswith('.delanswer') and guid == admins:
                    try:
                        command = text.replace(".delanswer", "")
                        db.execute(f'DELETE from Answer WHERE matn = "%s" ' %command)
                        db.commit()
                        await event.reply("πΉ Ϊ©ΩΩΩ ΩΩΨ±Ψ― ΩΨΈΨ± ΩΎΨ§Ϊ© Ψ΄Ψ― πΉ")
                    except:
                        pass
                if text.startswith('.listanswer') and guid == admins:
                    try:
                        Lists = db.execute('SELECT * FROM Answer').fetchall()
                        for LiA in Lists:
                            matn = LiA[1]
                            javab = LiA[2]
                            await event.reply(f'πΉ ΩΫΨ³Ψͺ ΩΎΨ§Ψ³Ψ? ΩΨ§ πΉ\n\nΩΨͺΩ : {matn}\nΨ¬ΩΨ§Ψ¨ : {javab}')
                    except:
                        pass
                if text.startswith(".Shot") and guid == admins:
                    try:
                        command = text.replace(".Shot", "")
                        await client.sendImage(event.object_guid, url=f'https://api.otherapi.tk/carbon?type=create&code={command}')
                    except:
                        pass
                if text.startswith('.deleted') and guid == admins:
                    try:
                        message_ids_dele = await client(methods.messages.GetMessages(event.object_guid, sort='FromMax',min_id=None, max_id=None, type=None))
                        for item_deleted in message_ids_dele.messages:
                            await client(methods.messages.DeleteMessages(event.object_guid, message_ids=item_deleted.message_id))
                        await event.reply('πΉ %s ΩΎΫΨ§Ω Ψ§Ψ?ΫΨ± ΩΎΨ§Ϊ© Ψ΄Ψ― πΉ' %25)
                    except:
                        pass
                if text.startswith('.msg') and guid == admins:
                    try:
                        site = get('http://cipherx0991505.blogfa.com/post/2')
                        soup = BeautifulSoup(site.content, 'html.parser')
                        matn = soup.find('div', {'class':'postcontent'})
                        textApp = matn.find('p').text
                        await event.reply(f'πΉ ΩΨ³ΫΨ¬ Ψ§Ψ―ΩΫΩ πΉ\n\nπ° {textApp}')
                        open('Mode/Status', 'w').write(textApp)
                    except:
                        pass

                if text.startswith('.prof') and guid == admins:
                    try:
                        open('Image/TimeOn', 'w').write(text.replace('.prof', '').strip())
                        await event.reply(f"**TIME PROFILE** __{text.replace('.prof', '')}__")
                    except:
                        pass
                if os.path.exists('Image/TimeOn'):
                    mode = open('Image/TimeOn').read()
                else:
                    mode = 'off'
                if mode == 'on':
                    ir = pytz.timezone("Asia/Tehran")
                    time = f"""{datetime.now(ir).strftime("%H:%M")}"""
                    if os.path.exists('Image/Time'):
                        time_old = open('Image/Time').read()
                    if time_old == time:
                        pass
                    else:
                        open('Image/Time', 'w').write(time)
                        font = ImageFont.truetype(f"Image/1.otf", 70)
                        img = Image.open('Image/1.jpg')
                        draw = ImageDraw.Draw(img)
                        draw.text((200, 350),f"{time}", font=font)
                        img.save('Image/ProFile.jpg')
                        file = await client.upload(file='Image/ProFile.jpg')
                        file_id = file.file_id
                        c = await client(methods.chats.GetAvatars(admins))
                        avatar_id = c.avatars[0].avatar_id
                        await client(methods.chats.DeleteAvatar(admins, avatar_id))
                        await client(methods.chats.UploadAvatar(admins, main_file_id=file_id, thumbnail_file_id=file_id))
                else:
                    pass
        await client.run_until_disconnected()

asyncio.run(main())
