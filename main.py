from aiogram import executor
from loader import dp
from utils import on_startup, on_shutdown
import handlers


if __name__ == '__main__':
    # Continuously ask for updates
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
