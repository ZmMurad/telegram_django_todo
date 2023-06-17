from aiogram import types, Router, Bot
from aiogram.filters.command import Command
from keypad import startmarkup, does_markup
from aiogram.fsm.context import FSMContext
import logging

logging.basicConfig(level=logging.INFO)



router=Router()




@router.message(Command("start"))
async def cmd_start(message:types.Message, bot:Bot, state:FSMContext):
    s= await state.get_state()
    if not str(s)=="InSystem:login":
        await message.answer(f"Привествую вас {message.from_user.first_name}, пожалуйста авторизуйтесь чтобы войти в систему", reply_markup=startmarkup)
    else:
        await message.answer(f"Вы уже авторизованы", reply_markup=does_markup)