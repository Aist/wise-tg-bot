from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import BotCommand
from handlers.common import register_handlers_common

TOKEN = config('TOKEN')
 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/get", description='Get your balance from Wise'),        
    ]
    await bot.set_my_commands(commands)

async def on_startup(_):
    register_handlers_common(dp)
    await set_commands(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)