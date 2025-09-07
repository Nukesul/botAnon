import telebot

TOKEN = "8429936435:AAE_QB-paPE_acvIkYc4DvwXrjpaS_yXZgE"
ADMIN_ID = 871269397

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'sticker', 'animation', 'video', 'document', 'voice'])
def forward_to_admin(message):
    try:
        if message.content_type == 'text':
            bot.send_message(ADMIN_ID, f"Анонимное сообщение:\n{message.text}")
        elif message.content_type == 'photo':
            bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption="Анонимная фотография")
        elif message.content_type == 'sticker':
            bot.send_sticker(ADMIN_ID, message.sticker.file_id)
        elif message.content_type == 'animation':
            bot.send_animation(ADMIN_ID, message.animation.file_id, caption="Анонимная гифка")
        elif message.content_type == 'video':
            bot.send_video(ADMIN_ID, message.video.file_id, caption="Анонимное видео")
        elif message.content_type == 'document':
            bot.send_document(ADMIN_ID, message.document.file_id, caption="Анонимный документ")
        elif message.content_type == 'voice':
            bot.send_voice(ADMIN_ID, message.voice.file_id, caption="Анонимное голосовое сообщение")

        bot.reply_to(message, "Ваше сообщение доставлено анонимно ✅")
    except Exception as e:
        print(f"Ошибка при пересылке сообщения: {e}")
        bot.reply_to(message, "Произошла ошибка при доставке сообщения ❌")

print("Бот запущен и готов к приему сообщений...")
bot.polling()
