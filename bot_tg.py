from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import *
import asyncio

TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher()

def diff_date(input_date):
    try:
        temp = input_date.split(' ')
        today = datetime.today()
        input_date = datetime(int(temp[0]), int(temp[1]), int(temp[2]))
        if input_date.strftime('%Y-%m-%d') == today.strftime('%Y-%m-%d'):
            src = '0 дней'
        else:
            delta = input_date - today
            delta = str(delta)
            delta = delta.split(' ')[0]
            delta = int(delta)
            if delta < 0:
                delta *= -1
                src =  str(delta+1) + ' days left'
            else:
                src =  str(delta+1) + ' days passed'
    except:
        src = 'Введите корректный формат'
    return src

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
   await message.reply("Введите дату в формате ГГГГ ММ ДД (через пробел)")

@dp.message()
async def echo(message: types.Message): 
   await message.answer(diff_date(message.text))

async def main():
    bot = Bot(TOKEN)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
