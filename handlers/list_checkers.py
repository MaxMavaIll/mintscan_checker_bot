from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('list_checkers'))
async def list_my_validators(message: types.Message, state: FSMContext):
    """List all registered validators"""

    data = await state.get_data()
    validators = data.get('validators')

    if validators:
        validators_str = 'I\'m checking the following validators:\n\n'
        for i, validator in validators.items():
            validators_str += f'{i + 1}. {validator["chain"]} {validator["operator_address"]}\n'
    else:
        validators_str = 'No checkers are currently running. ' \
                         'You can add checker with /create_checker command'

    await message.answer(validators_str)
