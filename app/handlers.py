from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject

router = Router()


@router.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
async def cmd_start(message: Message, command: CommandObject):
    await message.answer(text=f'Привет! Ты пришел от {command.args}')

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
