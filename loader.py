from aiogram import Bot, Dispatcher
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
