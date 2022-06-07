from aiogram import Dispatcher, types
from wise import Wise
from decouple import config

USERS_ID = config('USERS_ID')

async def cmd_get(message: types.Message):    
    if (str(message.from_user.id) in USERS_ID):
        wise = Wise()
        balance = wise.get_balance()    
        if (balance):
            await message.answer(f'''Balance: {balance['data']} EUR''')
    else:
        await message.answer(f'''You need to setup bot. Your user id: {message.from_user.id}\nYou should add it to .env file''')

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_get, commands="get")