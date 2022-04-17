from aiogram import Dispatcher

from loader import ADMIN


async def on_shutdown(dp: Dispatcher):
    await dp.bot.send_message(chat_id=ADMIN, text='I stopped')
