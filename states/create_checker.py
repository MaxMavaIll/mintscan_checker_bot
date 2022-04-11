from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateChecker(StatesGroup):
    """States for checker creating form"""

    chain = State()
    operator_address = State()
