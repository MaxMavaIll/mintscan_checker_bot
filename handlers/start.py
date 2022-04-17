from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        f'Hello, {message.chat.first_name}! \n'
        '\n'
        'You can add validator checker through /create_checker command. \n'
        'This will make me check this validator for missing blocks. \n'
        'You can add any as many validators as you like. \n'
        '\n'
        'I work with any network available at mintscan.io.'
    )
