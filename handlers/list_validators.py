from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('list_my_validators'))
async def list_my_validators(message: types.Message, state: FSMContext):
    """List all registered validators"""

    data = await state.get_data()
    chain = data.get('chain')
    operator_address = data.get('operator_address')

    await message.answer(
        'I\'m checking the following validators:\n'
        f'1. {chain} {operator_address}'
    )
