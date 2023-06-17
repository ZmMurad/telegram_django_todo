from aiogram.fsm.state import StatesGroup, State

class InSystem(StatesGroup):
    login=State()
    logout=State()
    wait=State()