from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder





list_start=[[types.KeyboardButton(text="Авторизоваться по токену")]]

startmarkup=types.ReplyKeyboardMarkup(keyboard=list_start,resize_keyboard=True)



does_list=[[types.KeyboardButton(text="Посмотреть все записи"), types.KeyboardButton(text="Добавить запись")]]

does_markup=types.ReplyKeyboardMarkup(keyboard=does_list,resize_keyboard=True)

does_action=InlineKeyboardBuilder()
does_action.add(types.InlineKeyboardButton(text="Удалить запись",callback_data="delete_do"))
does_action.add(types.InlineKeyboardButton(text="Назад в меню",callback_data="history_finish"))
does_action.adjust(1)