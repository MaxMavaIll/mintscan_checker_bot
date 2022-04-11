from aiogram import Bot, executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from environs import Env

# Read environs
env = Env()
env.read_env()

# Bot token from .env
API_KEY = env.str('API_KEY')

# Instance bot and dispatcher with FSM storage
bot = Bot(API_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


if __name__ == '__main__':
    # Continuously ask for updates
    executor.start_polling(dp)
