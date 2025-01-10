from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты', request_contact=True)]
],
resize_keyboard=True,
input_field_placeholder='Выберите меню.')

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

open_youtube = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открыть Ютуб', web_app=WebAppInfo(url='https://youtube.com'))]
])

async def catalog():
    all_data = ('Nike', 'adidas', 'reebok')

    keyboard = ReplyKeyboardBuilder()

    for data in all_data:
        keyboard.add(KeyboardButton(text=data))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)