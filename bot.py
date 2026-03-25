import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils import keyboard
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

TOKEN = "your_token_here"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def update_books():
    books_data = []

    url = "https://books.toscrape.com/"

    while True:
        response = requests.get(url)
        content = BeautifulSoup(response.content, features="html.parser")

        books = content.find_all("article", class_="product_pod")

        for book in books:
            title = book.find("h3").find("a")["title"]

            price = book.find("p", class_="price_color").text
            price = float(price.replace("£", ""))

            rating = book.find("p", class_="star-rating")["class"][1]

            if rating not in ["Four", "Five"]:
                continue

            books_data.append({
                "title": title,
                "price": price,
                "rating": rating
            })

        next_page = content.find("li", class_="next")

        if next_page:
            page = next_page.find("a")["href"]
            url = urljoin(url, page)
        else:
            break

    # сортировка
    books_data.sort(key=lambda x: x["price"])

    # запись
    with open("books.csv", "w", encoding="utf-8") as file:
        for book in books_data:
            file.write(f"{book['title']},£{book['price']},{book['rating']}\n")

def read_books(value):
    try:
        with open("books.csv", "r", encoding="utf-8") as file:
            content = file.read().splitlines()
            return content[:value]
    except FileNotFoundError:
            return []

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой бот.")


@dp.message(Command("top"))
async def send_top(message: Message):
    builder = keyboard.InlineKeyboardBuilder()

    for index in [3,5,10]:
        builder.button(text=f"Топ {index}", callback_data=f"top_{index}")

    await message.answer("Выберите количество",reply_markup=builder.as_markup())

@dp.message(Command("update"))
async def update_message(message: Message):
    await message.answer("Обновляю данные")
    update_books()
    await message.answer("Готово")

@dp.callback_query()
async def handle_buttons(callback: CallbackQuery):
    data = callback.data.split("_")
    count = int(data[1])

    top_books = read_books(count)

    if not top_books:
        text = "Данные отсутствуют, напишите /update"
    else:
        text = f"🔥 <b>Топ {count} книг:</b>\n\n"

        for line in top_books:
            line = line.rsplit(",", 2)
            title, price, rating = line[0], line[1].replace("£", ""), line[2]

            text += f"📚 <b>{title}</b>\n"
            text += f"💰 Цена: <code>£{float(price):.2f}</code>\n"
            text += f"⭐ Рейтинг: <i>{rating}</i>\n\n"

    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())