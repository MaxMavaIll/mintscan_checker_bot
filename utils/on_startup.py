from aiogram import Dispatcher

from loader import ADMIN


async def on_startup(dp: Dispatcher):
    print('THe bot is running')
    await dp.bot.send_message(chat_id=ADMIN, text='I\'m running')
