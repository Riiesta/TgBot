import telebot
import csv
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Инициализация индекса текущего слова
current_index = 0

# Чтение данных из CSV файла
with open(r'C:\Users\Счастье\PycharmProjects\tgbot\Лист Microsoft Excel.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')  # Указываем разделитель как ';'
    next(reader)  # Пропустите заголовок
    words = list(reader)

# Функция для отправки слова и перевода
def send_word_translation(chat_id):
    global current_index
    try:
        word, transcription, translation = words[current_index]
        bot.send_message(chat_id, f"{word} ({transcription}) - {translation}")
        current_index += 1
        if current_index >= len(words):
            current_index = 0
            bot.send_message(chat_id, "Вернулись к началу списка слов!")
    except ValueError:
        bot.send_message(chat_id, f"Ошибка в строке {current_index}: {words[current_index]}")
        current_index += 1

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text.lower() == "дальше":
        send_word_translation(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Нажмите 'Дальше' чтобы получить следующее слово!")

if __name__ == "__main__":
    bot.polling()
