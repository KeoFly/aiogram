import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await message.answer(text=f'Привет!', reply_markup=kb.main_inline)

@router.callback_query(F.data == 'catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы открыли каталог',
                                  reply_markup=await kb.catalog())

@router.message(F.text == 'Корзина')
async def basket(message: Message):
    await message.answer('Ваша корзина пуста!')

@router.message(Command('test'))
async def cmd_test(message: Message):
    await message.bot.send_message(chat_id=message.chat.id,
                                   message_thread_id=message.message_thread_id,
                                   text='OK')

@router.message(Command('help'))
async def help(message:Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?')

@router.message(Command('get'))
async def get(message: Message, command: CommandObject):
    if not command.args:
        await message.answer('Аргументы не переданы!!!')
    else:
        await message.answer(f'Вы ввели команду get с аргрументом {command.args}')

@router.message(F.text == 'привет')
async def echo(message: Message):
    await message.reply('приветтт')
    await message.answer(f'Ваш ID: {message.from_user.id}')

@router.message(F.photo)
async def echo(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(2)
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)

@router.message(F.document)
async def echo(message: Message):
    await message.answer_document(document=message.document.file_id)

@router.message(F.audio)
async def echo(message: Message):
    await message.answer_audio(audio=message.audio.file_id)

@router.message(F.animation)
async def echo(message: Message):
    await message.answer_animation(animation=message.animation.file_id)
    await message.answer(text='Вы прислали гифку')

@router.message(F.from_user.id == 1081091327)
async def echo(message: Message):
    await message.answer(f'Написал определенный юзер с ID {message.from_user.id}')
