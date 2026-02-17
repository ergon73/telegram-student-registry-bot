import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from bot.states import Form
from bot.db import init_db, insert_student

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("cancel"), StateFilter("*"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Ввод данных отменён.")


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "Команды:\n"
        "/start — начать регистрацию (имя, возраст, класс)\n"
        "/cancel — отменить ввод на любом шаге\n"
        "/help — эта справка"
    )


@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer("Привет! Как тебя зовут?")


@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("Сколько тебе лет?")


@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext) -> None:
    text = message.text
    try:
        age = int(text)
    except ValueError:
        await message.answer("Введи число от 1 до 120.")
        return
    if age < 1 or age > 120:
        await message.answer("Введи число от 1 до 120.")
        return
    await state.update_data(age=age)
    await state.set_state(Form.grade)
    await message.answer("В каком ты классе?")


@dp.message(Form.grade)
async def process_grade(message: Message, state: FSMContext) -> None:
    await state.update_data(grade=message.text)
    user_data = await state.get_data()
    name = user_data["name"]
    age = user_data["age"]
    grade = user_data["grade"]
    row_id = insert_student(name=name, age=age, grade=grade)
    await state.clear()
    await message.answer(f"Данные сохранены. id записи: {row_id}")


async def main() -> None:
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
