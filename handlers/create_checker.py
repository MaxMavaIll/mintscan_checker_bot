from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from states.create_checker import CreateChecker

from loader import dp


@dp.message_handler(Command('create_checker'))
async def create_checker(message: types.Message, state: FSMContext):
    """Entry point for create checker conversation"""

    await message.answer(
        'Let\'s see...\n'
        'What\'s your validator\'s network again?'
    )

    await CreateChecker.chain.set()


@dp.message_handler(state=CreateChecker.chain)
async def enter_chain(message: types.Message, state: FSMContext):
    """Enter chain name handler"""

    async with state.proxy() as data:
        data['chain'] = message.text

    await CreateChecker.operator_address.set()
    await message.answer(
        'Okay, now I need the operator address of this validator'
    )


@dp.message_handler(state=CreateChecker.operator_address)
async def enter_operator_address(message: types.Message, state: FSMContext):
    """Enter validator's operator address"""

    data = await state.get_data()
    chain = data.pop('chain')

    async with state.proxy() as data:
        data.setdefault('validators', {})
        i = len(data.get('validators'))
        data['validators'][i] = {
            'chain': chain,
            'operator_address': message.text
        }

    await message.answer(
        'Nice! Now I\'ll be checking this validator all day long '
        'till the end of time👌'
    )

    await state.reset_state(with_data=False)
