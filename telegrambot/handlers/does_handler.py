from aiogram.fsm.context import FSMContext
from aiogram import types, Router, Bot,F
from aiogram.fsm.state import StatesGroup, State
from keypad import startmarkup, does_markup,does_action
from aiogram.filters import Text
from states import InSystem
from api_views import get_does,get_do, delete_do_f, add_do_f


router=Router()


@router.message(Text("Добавить запись"), InSystem.login)
async def add_do(message:types.Message, bot:Bot, state:FSMContext):
    await message.answer("Введите заголовок для своего дела")
    await state.update_data(status_add="title")
    




@router.message(Text("Посмотреть все записи"), InSystem.login)
async def get_does_t(message:types.Message, bot:Bot, state:FSMContext):
    data=await state.get_data()
    result=get_does(data["token"])["data"]
    if len(result)==0:
        await message.answer(text="У вас нет записей", reply_markup=does_markup)
        return
    await message.answer(text=f"Всего у вас записей {len(result)}", reply_markup=does_markup)
    row_number=0
    list_out=[result[i:i + 5] for i in range(0, len(result), 5)]
    string=""
    do_num=[]
    for value in list_out[row_number]:
        do_num.append(value["id"])
        string+=f"Запись№ {value['id']}\nЗаголовок: \n{value['title']}\nТекст:\n{value['text']}\n {'➖'*12}\n"
    await message.answer(f"{string}", reply_markup=get_keyboard([0,len(list_out),do_num]))
    await state.update_data(li=list_out)
    await state.update_data(row_number=row_number)
    
    
    
def get_keyboard(state:FSMContext=None):
    buttons = [
        [],
        [types.InlineKeyboardButton(text="Закрыть", callback_data="history_finish")],
    ]
    if state and state[0]!=0:
        buttons[0].append(types.InlineKeyboardButton(text="<", callback_data="history_left"))
    if state and state[1]!=state[0]:
        buttons[0].append(types.InlineKeyboardButton(text=">", callback_data="history_right"))
    for do_num in state[2]:
        buttons.insert(-1,[types.InlineKeyboardButton(text=f"#{do_num}", callback_data=f"history_{do_num}")])
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@router.callback_query(F.data=="delete_do")
async def delete_do_t(callback:types.CallbackQuery, bot:Bot, state:FSMContext):
    data=await state.get_data()
    do_id=data["do_id"]
    result=delete_do_f(data["token"], do_id)
    if result["status"]=="success":
        await callback.message.edit_text("🙌")
        await callback.message.answer(text="Меню",reply_markup=does_markup)
    else:
        await callback.message.edit_text("Произошла неизвестная ошибка", reply_markup=does_action.as_markup())
    await callback.answer()

@router.callback_query(Text(startswith="history_"))
async def callbacks_num(callback:types.CallbackQuery, state:FSMContext, bot:Bot):
    data=await state.get_data()
    action=callback.data.split("_")[1]
    li= data["li"]
    row_number=data["row_number"]
    if action=="right" and row_number<len(li)-1:
        row_number+=1
        await state.update_data(row_number=row_number)
        await show_does(callback, row_number, li)
    elif action=="left" and row_number>0:
        row_number-=1
        await state.update_data(row_number=row_number)
        await show_does(callback, row_number, li)
    elif  action=="finish":    
        await callback.message.edit_text("🙌")
        await callback.message.answer(text="Меню",reply_markup=does_markup)
        await callback.answer()
    else:
        result=get_do(data["token"], action)["data"]
        string=f"Запись№ {result['id']}\nЗаголовок: \n{result['title']}\nТекст:\n{result['text']}\n {'➖'*12}\n"
        await callback.message.edit_text(string, reply_markup=does_action.as_markup())        
        await state.update_data(do_id=result["id"])
        await callback.answer()

        
    
async def show_does(callback:types.CallbackQuery, new_value:int , li):
    string=""
    do_num=[]
    for value in li[new_value]:
        do_num.append(value["id"])
        string+=f"Запись№ {value['id']}\nЗаголовок: \n{value['title']}\nТекст:\n{value['text']}\n {'➖'*12}\n"
    await callback.message.edit_text(f"{string}", reply_markup=get_keyboard([new_value,len(li)-1,do_num]))
    await callback.answer()
        

@router.message()
async def add_title_do(message:types.Message, bot:Bot, state:FSMContext):
    data = await state.get_data()
    if "status_add" in data.keys() and data["status_add"]=="title":
        await message.answer("Теперь пришли текст вашего дела")
        await state.update_data(status_add="text", title=message.text)
    elif "status_add" in data.keys() and data["status_add"]=="text":
        result=add_do_f(data["token"],{"title":data["title"],"text":message.text})
        await message.answer(f"Ваша запись успешно добавлена {result}")
        await state.update_data(status_add=None)
    else:
        await message.answer("Я не расспознал вашу команду")
        
