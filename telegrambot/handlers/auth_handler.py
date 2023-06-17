from aiogram import types, Router, Bot,F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from states import InSystem
from keypad import startmarkup, does_markup
from aiogram.filters import Text
from api_views import send_token

router=Router()




@router.message(Text("Авторизоваться по токену"))
async def auth_token(message:types.Message, bot:Bot, state:FSMContext):
    await message.answer(text=f"Пожалуйста пришлите свой токен для авторизации, перейдите на главную страницу сайта",reply_markup=startmarkup)
    await state.set_state(InSystem.wait)
    
    
@router.message(F.text, InSystem.wait)
async def get_toket(message:types.Message,bot:Bot, state:FSMContext):
    status=send_token(message.text)    
    if status:
        await message.answer("Поздравляю вы в системе",reply_markup=does_markup)
        await state.set_state(InSystem.login)
        await state.update_data(token=message.text)
    else:
        await message.answer("Вы ввели неправильный токент", reply_markup=startmarkup)
        await state.set_state(InSystem.logout)
        
    