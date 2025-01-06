import telebot
import os
import time
bot = telebot.TeleBot('7599452620:AAEtHEVjsHyibtEp_rAU-y2_l9v-zrJhUHM')
from telebot import types
global old_timestamp
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
@bot.message_handler(commands=['~help'])
def handle_ban(message):
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
                bot.send_message(message.chat.id, "пользователь успешно заблокирован ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")

@bot.message_handler(commands=['~unban'])
def handle_unban(message):
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) < 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                number_to_remove = str(message.text.split()[1])
                remove_number_from_file(number_to_remove)
                with open('banlist.txt', 'r') as file:
                    ban_contents = file.read()
                banlist = ban_contents.split()
                bot.send_message(message.chat.id, "пользователь успешно разблокирован ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
with open('banlist.txt', 'r') as file:
    ban_contents = file.read()
banlist = ban_contents.split()
@bot.message_handler(commands=['~update'])
def handle_update(message):
    if message.chat.type == 'supergroup':
        if message.chat.id == -1002314004246:
            if len(message.text.split()) == 2 or len(message.text.split()) > 2:
                bot.send_message(message.chat.id, "ошибка синтаксиса команды")
            else:
                bot.send_message(message.chat.id, "банлист успешно обновлён ✅")
        else:
            bot.send_message(message.chat.id, "у тебя нету прав")
    else:
        bot.send_message(message.chat.id, "у тебя нету прав")
prim = "asd"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name

        if message.entities:
            text_with_links = message.text
            for entity in message.entities:
                if entity.type == 'text_link':
                    link_text = message.text[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        file_id = message.photo[-1].file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_photo('-1002314004246', file_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        audio_id = message.audio.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_audio('-1002314004246', audio_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        document_id = message.document.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_document('-1002314004246', document_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        video_id = message.video.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_video('-1002314004246', video_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        voice_id = message.voice.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_voice('-1002314004246', voice_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
    global prim
    ban_z = "z"
    for item in banlist:
        if item == str(message.from_user.id):
            ban_z = "ban"
            break
    if message.chat.type == 'private' and ban_z != "ban" and prim != message.chat.id:
        user = message.from_user
        if user.username:
            soob = "id пользователя: " + str(user.id) + " \nusername пользователя: @" + user.username + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        else:
            soob = "id пользователя: " + str(user.id) + " \nПервый никнейм: " + user.first_name + " \nПоследний никнейм: " + user.first_name
        video_note_id = message.video.file_id
        caption = message.caption
        if caption and message.caption_entities:
            text_with_links = caption
            for entity in message.caption_entities:
                if entity.type == 'text_link':
                    link_text = caption[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{link_text}]({url})"
                    text_with_links = text_with_links.replace(link_text, markdown_link)
            bot.send_video_note('-1002314004246', video_note_id, caption=text_with_links, parse_mode='Markdown')
            bot.send_message('-1002314004246', soob)
            bot.send_message(message.chat.id, "сообщение успешно отправлено✅")
        elif caption:
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
