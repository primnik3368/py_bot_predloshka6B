import time
hello_message0 = list("вас приветствует бот предложка 7в!/")
i = 0
while hello_message0[i] != hello_message0[-1]:
    print(hello_message0[i], end="")
    i += 1
    time.sleep(0.1)
import os
import asyncio
from datetime import datetime
import telebot
import colorama
from colorama import Fore, Style, init, Back
from telegram import Update
with open('bot_api_id.txt', 'r') as file:
    api_id = file.read().strip()
bot = telebot.TeleBot(str(api_id))
from telebot import types
init(autoreset=True)
print(f"""{Fore.RED}
==================================================
███████╗██╗   ██╗    ██████╗  ██████╗ ████████╗
╚════██║██║   ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██╔╝██║   ██║    ██████╔╝██║   ██║   ██║   
   ██╔╝ ╚██╗ ██╔╝    ██╔══██╗██║   ██║   ██║   
   ██║   ╚████╔╝     ██████╔╝╚██████╔╝   ██║   
   ╚═╝    ╚═══╝      ╚═════╝  ╚═════╝    ╚═╝   
==================================================

""")
hello_message1 = list("""бот успешно запущен! 
для его остановки используйте клавиши ctrl+C./""")
i = 0
while hello_message1[i] != hello_message1[-1]:
    print(f"""{Fore.RED}{hello_message1[i]}""", end="")
    i += 1
    time.sleep(0.1)

async def process_message(chat_id):
    await bot.send_message(chat_id=chat_id, text="записываю...")
    await asyncio.sleep(5)
    await bot.send_message(chat_id=chat_id, text="сообщение успешно отправлено✅")


global old_timestamp
def antispam_fun(message):
    print(f"{Fore.LIGHTBLACK_EX}called antispam_fun.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    threshold_time = time.time() - 16
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
    bot.send_message(message.chat.id, '[информация о боте](https://telegra.ph/Predlozhka-Telegram-kanala-7V-06-14)', parse_mode='MarkdownV2')
@bot.message_handler(commands=['help'])
def handle_help(message):
    print(f"{Fore.MAGENTA}called /help & handle_help command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) == 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                bot.send_message(message.chat.id, """список команд:
send {user_id} [сообщение] - отправка пользователю сообщения.

help - список команд.

ban {user_id} - бан пользователя и обновление бан листа.

unban {user_id} - анбан пользователя и обновление бан листа.

update - обновление бан листа.
""")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
@bot.message_handler(commands=['send'])
def handle_ban(message):
    print(f"{Fore.MAGENTA}called /send & handle_send command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) < 3:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                user_id = str(message.text.split()[1])
                text_mes = ' '.join(message.text.split()[2:])
                bot.send_message(user_id, text_mes)
                bot.send_message('-1002314004246', "сообщение успешно отправлено✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")


@bot.message_handler(commands=['ban'])
def handle_ban(message):
    print(f"{Fore.MAGENTA}called /ban & handle_ban command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
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

@bot.message_handler(commands=['unban'])
def handle_unban(message):
    print(f"{Fore.MAGENTA}called /unban & handle_unban command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) < 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                number_to_remove = str(message.text.split()[1])
                remove_number_from_file(number_to_remove)
                print(f"{Fore.LIGHTBLACK_EX}called remove_number_from_file.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
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
@bot.message_handler(commands=['update'])
def handle_update(message):
    print(f"{Fore.MAGENTA}called /update & handle_update command.\ncalling user: {str(message.from_user.id)} time: {time.time()}.")
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
            process_message(message.chat.id)
        else:
            bot.send_message('-1002314004246', text=message.text)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_photo('-1002314004246', file_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_photo('-1002314004246', file_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
        process_message(message.chat.id)
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
        process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_audio('-1002314004246', audio_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_audio('-1002314004246', audio_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_document('-1002314004246', document_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_document('-1002314004246', document_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_video('-1002314004246', video_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_video('-1002314004246', video_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_voice('-1002314004246', voice_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_voice('-1002314004246', voice_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
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
            process_message(message.chat.id)
        elif caption:
            print(f"{Fore.RED}caption: *{caption}*.")
            bot.send_video_note('-1002314004246', video_note_id, caption=caption)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
        else:
            bot.send_video_note('-1002314004246', video_note_id)
            bot.send_message('-1002314004246', soob)
            process_message(message.chat.id)
    elif message.chat.type == 'private' and ban_z == "ban" and prim != message.chat.id:
        bot.send_message(message.chat.id, "пользователь заблокирован🚫")
        prim = message.chat.id
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=60)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(0.3)



