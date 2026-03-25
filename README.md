# 📚 Telegram Books Parser Bot

## English

### 📌 Description

This Telegram bot parses book data from the website https://books.toscrape.com and allows users to view top-rated books directly in Telegram.

The bot collects data, filters books by rating, sorts them by price, and displays results using interactive buttons.

### ⚙️ Features

* Web scraping from multiple pages
* Filtering books with rating **4 and 5**
* Sorting books by price
* Interactive buttons to choose number of books (3, 5, 10)
* Fast responses using cached data (`books.csv`)
* Manual data update via command

### 🛠 Technologies

* Python
* aiogram
* requests
* BeautifulSoup

### 🚀 How to Run

1. Install dependencies:
   pip install aiogram requests beautifulsoup4

2. Insert your Telegram bot token:
   TOKEN = "your_token_here"

3. Run the bot:
   python bot.py

### 💡 Commands

/start – start the bot
/top – choose number of books
/update – update data from the website

### 📸 Example

1. Choose number of books:
   "Top 3", "Top 5", "Top 10"

2. Output:

```id="m2b7ok"
📚 Book Name
💰 £10.00
⭐ Four
```

### 📁 Project Structure

* bot.py — main bot logic
* books.csv — cached parsed data

---

## Русский

### 📌 Описание

Этот Telegram-бот парсит данные о книгах с сайта https://books.toscrape.com и позволяет пользователю получать список лучших книг прямо в Telegram.

Бот собирает данные, фильтрует книги по рейтингу, сортирует по цене и выводит результат с помощью кнопок.

### ⚙️ Функции

* Парсинг сайта (несколько страниц)
* Фильтрация книг с рейтингом **4 и 5**
* Сортировка по цене
* Кнопки выбора количества книг (3, 5, 10)
* Быстрый ответ за счёт кэша (`books.csv`)
* Обновление данных через команду

### 🛠 Технологии

* Python
* aiogram
* requests
* BeautifulSoup

### 🚀 Как запустить

1. Установить зависимости:
   pip install aiogram requests beautifulsoup4

2. Вставить токен бота:
   TOKEN = "your_token_here"

3. Запустить:
   python bot.py

### 💡 Команды

/start – запуск бота
/top – выбор количества книг
/update – обновление данных

### 📸 Пример

1. Выбор:
   "Топ 3", "Топ 5", "Топ 10"

2. Вывод:

```id="k5k2km"
📚 Название книги
💰 £10.00
⭐ Four
```

### 📁 Структура проекта

* bot.py — логика бота
* books.csv — сохранённые данные

---

## 👨‍💻 Author

This project was created as a learning project to practice web scraping and Telegram bot development.
