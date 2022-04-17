from aiogram import executor
from loader import dp
import handlers

if __name__ == '__main__':
    # Continuously ask for updates
    executor.start_polling(dp)
