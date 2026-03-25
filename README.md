# Русский

# Telegram Bot (Books Parser)

## 📌 Описание

Бот парсит сайт с книгами и показывает пользователю топ книг по цене.

## ⚙️ Функции

* Парсинг сайта books.toscrape.com
* Фильтрация по рейтингу (4 и 5)
* Сортировка по цене
* Кнопки для выбора количества книг (3, 5, 10)
* Красивый вывод в Telegram

## 🛠 Технологии

* Python
* aiogram
* requests
* BeautifulSoup

## 🚀 Как запустить

1. Установить зависимости:
   pip install aiogram requests beautifulsoup4

2. Вставить свой TOKEN

3. Запустить:
   python bot.py

## 💡 Команды

/start
/top
/update

# English
# Telegram Bot (Books Parser)

## 📌 Description

This Telegram bot parses data from the website https://books.toscrape.com and shows users a list of top-rated books sorted by price.

## ⚙️ Features

* Parses multiple pages of the website
* Filters books with rating **4 and 5**
* Sorts books by price
* Interactive buttons to choose number of books (3, 5, 10)
* Clean and formatted output in Telegram
* Data caching via local file (fast response)

## 🛠 Technologies

* Python
* aiogram
* requests
* BeautifulSoup

## 🚀 How to Run

1. Install dependencies:
   pip install aiogram requests beautifulsoup4

2. Insert your Telegram bot token in the code:
   TOKEN = "your_token_here"

3. Run the bot:
   python bot.py

## 💡 Commands

/start – start the bot
/top – choose how many books to display
/update – update book data from the website

## 📸 Example Output

The bot displays:

* Book title
* Price
* Rating

Example:
📚 Book Name
💰 £10.00
⭐ Four

## 📁 Project Structure

* bot.py — main bot logic
* books.csv — cached data (generated automatically)

## 👨‍💻 Author

Telegram bot developed as a learning project for web scraping and bot development.
