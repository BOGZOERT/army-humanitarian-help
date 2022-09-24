import telebot

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['new_chat_members'])
def remove_info(message):
    bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(content_types=['new_chat_members'])
def remove_info(message):
    bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True)