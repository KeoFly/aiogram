from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Filter

admin = Router()

ADMINS = [1081091327, 67890]

class AdminProtect(Filter):
    def __init__(self):
        self.admins = ADMINS

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins

@admin.message(AdminProtect(), Command('apanel'))
async def cmd_panel(message: Message):
    await message.answer('Это админ-панель')