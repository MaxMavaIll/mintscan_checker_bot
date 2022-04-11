from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from states.create_checker import CreateChecker

from loader import dp


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello! The bot is running')

