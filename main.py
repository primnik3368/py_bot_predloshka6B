print("open from terminal!")
print("""вас приветствует бот предложка 6в!
setup...""")
import time
import os
from datetime import datetime
time.sleep(0.1)
print("""telegram-api setup...""")
import telebot
import colorama
from colorama import Fore, Style, init, Back
from telegram import Update
bot = telebot.TeleBot('7599452620:AAEtHEVjsHyibtEp_rAU-y2_l9v-zrJhUHM')
from telebot import types
time.sleep(0.1)
init(autoreset=True)
print(f"{Fore.BLUE}setup is done!")
time.sleep(0.1)
print(f"{Fore.GREEN}bot activated...")
print(f"""{Fore.RED}
==================================================
  e88",8,  Y8b Y88888P   888                  d8
 d888  "    Y8b Y888P    888 88e   e88 88e   d88
C8888 88e    Y8b Y8P     888 888b d888 888b d88888
 Y888 888D    Y8b Y      888 888P Y888 888P  888
  "88 88"      Y8P       888 88"   "88 88"   888
==================================================

""")
print(f"""{Fore.RED}бот успешно запущен!
для остановки бота используйте клавиши ctrl+C.""")
global old_timestamp
def antispam_fun(message):
    print(f"{Fore.LIGHTBLACK_EX}called antispam_fun.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    threshold_time = time.time() - 16
    message = message.from_user
    with open('timelist.txt', 'r') as file:
        lines = file.readlines()
    filtered_lines = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                unix_time = float(parts[0])
                if unix_time >= threshold_time:
                    filtered_lines.append(line)
            except ValueError:
                continue
    with open('timelist.txt', 'w') as file:
        file.writelines(filtered_lines)
    with open('timelist.txt', 'r') as file:
        time_contents = file.read()
    global timelist
    timelist = time_contents.split()
    time_to_write = str(message.date) + ' ' + str(message.chat.id)
    with open('timelist.txt', 'a') as file:
        file.write(f'{time_to_write} ')
def remove_number_from_file(number_to_remove):
    message = message.from_user
    print(f"{Fore.LIGHTBLACK_EX}called remove_number_from_file.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    try:
        with open('banlist.txt', 'r') as file:
            lines = file.readlines()
        number_to_remove_with_space = number_to_remove + ' '
        lines = [line.replace(number_to_remove_with_space, '') for line in lines]
        with open('banlist.txt', 'w') as file:
            file.writelines(lines)
    except:
        bot.send_message(message.chat.id, "файл banlist.txt не найден")
@bot.message_handler(commands=['start'])
def handle_start(message):
    print(f"{Fore.MAGENTA}called /start & handle_start command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    bot.send_message(message.chat.id, """
░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░
░░░░█████████░░░░███████████░░░░░░░
░░░██░░░░░░░██░░░█░░░░░░░░░██░░░░░░
░░░█░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░
░░░█░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░
░░░██████████░░░░███████████░░░░░░░
░░░██░░░░░░░██░░░█░░░░░░░░░██░░░░░░
░░░█░░░░░░░░░█░░░█░░░░░░░░░░█░░░░░░
░░░█░░░░░░░░░█░░░█░░░░░░░░░░█░░░░░░
░░░██░░░░░░░██░░░█░░░░░░░░░██░░░░░░
░░░░█████████░░░░███████████░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
===================================
вас приветствует бот предложка 6В!
автор бота: primnik3368
id автора: 5854237707
===================================
бот предложка - нацелен на ваш кон-
тент,который будет рассмотрен адми-
нистрацией выложен в телеграм канал
6в.
===================================
в боте запрещён спам.
сообщения стоит отправлять с интер-
валом в минимум 15 секунд.
сообщения отправленные до прошеств-
ия 15 секунд не будут отправленны и
зачтут дополнительные 15 секунд.
если вы видите сообщение от бота:
"сообщение успешно отправлено✅"
значит ваше сообщение отправленно
администрации телеграм канала 6в.
если вы его не видите - значит вы
либо заблокированы, либо бот сейчас
не активен и ваше сообщение будет
доставленно позже, либо вам нужно
подождать 15 секунд перед отправкой
сообщения боту.
===================================""")
@bot.message_handler(commands=['~help'])
def handle_help(message):
    print(f"{Fore.MAGENTA}called /~help & handle_help command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) == 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                bot.send_message(message.chat.id, """список команд:
~help - список команд.

~ban {user_id} - бан пользователя и обновление бан листа.

~unban {user_id} - анбан пользователя и обновление бан листа.

~update - обновление бан листа.
""")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
@bot.message_handler(commands=['~ban'])
def handle_ban(message):
    print(f"{Fore.MAGENTA}called /~ban & handle_ban command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) < 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                ban_id = str(message.text.split()[1])
                with open('banlist.txt', 'a') as file:
                    file.write(f'{ban_id} ')
                global banlist
                with open('banlist.txt', 'r') as file:
                    ban_contents = file.read()
                banlist = ban_contents.split()
                global prim
                prim = "asd"
                bot.send_message(message.chat.id, "пользователь успешно заблокирован ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")

@bot.message_handler(commands=['~unban'])
def handle_unban(message):
    print(f"{Fore.MAGENTA}called /~unban & handle_unban command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) < 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                number_to_remove = str(message.text.split()[1])
                remove_number_from_file(number_to_remove)
                global banlist
                with open('banlist.txt', 'r') as file:
                    ban_contents = file.read()
                banlist = ban_contents.split()
                global prim
                prim = "asd"
                bot.send_message(message.chat.id, "пользователь успешно разблокирован ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
with open('banlist.txt', 'r') as file:
    ban_contents = file.read()
global banlist
banlist = ban_contents.split()
@bot.message_handler(commands=['~update'])
def handle_update(message):
    print(f"{Fore.MAGENTA}called /~update & handle_update command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) == 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                global banlist
                with open('banlist.txt', 'r') as file:
                    ban_contents = file.read()
                banlist = ban_contents.split()
                global prim
                prim = "asd"
                bot.send_message(message.chat.id, "банлист успешно обновлён ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
global prim
prim = "asd"
global ban_z
ban_z = "."
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(f"{Fore.GREEN}called handle_text.\n{Fore.RED}text: *{message.text}*.\n{Fore.GREEN}calling user: {str(message.from_user.id)} time: {time.time()}.")
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    global prim
    global ban_z
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name

        if message.entities:
            text_with_links = message.text
            offset = 0
            for entity in message.entities:
                if entity.type == 'text_link':
                    link_text = message.text[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_message('-1002314004246', text=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_message('-1002314004246', text=message.text)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    print(f"{Fore.GREEN}called handle_photo.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        file_id = message.photo[-1].file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_photo('-1002314004246', file_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_photo('-1002314004246', file_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_photo('-1002314004246', file_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print(f"{Fore.GREEN}called handle_sticker.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        sticker_file_id = message.sticker.file_id
        bot.send_sticker('-1002314004246', sticker_file_id)
        bot.send_message('-1002314004246', soob)
        bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['animation'])
def handle_gif(message):
    print(f"{Fore.GREEN}called handle_gif.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        gif_file_id = message.animation.file_id
        bot.send_animation('-1002314004246', gif_file_id)
        bot.send_message('-1002314004246', soob)
        bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    print(f"{Fore.GREEN}called handle_audio.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        audio_id = message.audio.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_audio('-1002314004246', audio_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_audio('-1002314004246', audio_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_audio('-1002314004246', audio_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['document'])
def handle_document(message):
    print(f"{Fore.GREEN}called handle_document.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        document_id = message.document.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_document('-1002314004246', document_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_document('-1002314004246', document_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_document('-1002314004246', document_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['video'])
def handle_video(message):
    print(f"{Fore.GREEN}called handle_video.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        video_id = message.video.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_video('-1002314004246', video_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_video('-1002314004246', video_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_video('-1002314004246', video_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    print(f"{Fore.GREEN}called handle_voice.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        voice_id = message.voice.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_voice('-1002314004246', voice_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_voice('-1002314004246', voice_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_voice('-1002314004246', voice_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
@bot.message_handler(content_types=['video_note'])
def handle_video_note(message):
    print(f"{Fore.GREEN}called handle_video_note.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    global prim
    global ban_z
    antispam_fun(message)
    time_z = "."
    for item in timelist:
        if item == str(message.from_user.id):
            time_z = "spam"
            break
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id and time_z != "spam":
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        video_note_id = message.video.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            offset = 0
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = (text_with_links[:entity.offset + offset] + markdown_link + text_with_links[entity.offset + entity.length + offset:])
                    offset += len(markdown_link) - len(link_text)
            print(f"{Fore.RED}markdown caption with links: *{text_with_links}*.")
            bot.send_video_note('-1002314004246', video_note_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_video_note('-1002314004246', video_note_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        else:
            bot.send_video_note('-1002314004246', video_note_id)
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
bot.polling(none_stop=True, interval=0, timeout=60)
