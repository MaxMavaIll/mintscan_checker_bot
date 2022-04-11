from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from states.create_checker import CreateChecker

from loader import dp


@dp.message_handler(Command('create_checker'))
async def create_checker(message: types.Message):
    """Entry point for create checker conversation"""

    await message.answer(
        'Hello there! Let\'s see...\n'
        'What\'s your validator\'s chain name again?'
    )

    await CreateChecker.chain.set()


@dp.message_handler(state=CreateChecker.chain)
async def enter_chain(message: types.Message, state: FSMContext):
    """Enter chain name handler"""

    async with state.proxy() as data:
        data['chain'] = message.text

    await CreateChecker.operator_address.set()
    await message.answer(
        'Okay, now I need your validator operator address,'
        'if you can find it)'
    )


@dp.message_handler(state=CreateChecker.operator_address)
async def enter_operator_address(message: types.Message, state: FSMContext):
    """Enter validator's operator address"""

    async with state.proxy() as data:
        data['operator_address'] = message.text

    await state.finish()

