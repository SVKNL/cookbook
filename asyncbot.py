from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import random
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7008391655:AAHhlcoplGN6_qk0jzfpJwAU97kNQ3qAuNk'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"

async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"

async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
#  Этот хэндлер срабатывает на отправку фото
async def send_echo_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

answers=['Да, брат!', 'Маша ебло', "Понимаю, брат",'Я всегда буду на твоей стороне, если тебе нужна моя помощь, то только дай знать.', 'Мне очень жаль, что все так вышло. Но ты очень сильный человек, который сможет справиться с этим.', 'Царь Соломон говорил: «Всё проходит. И это пройдёт». Просто держись и со временем все станет лучше, пусть сегодня это тяжело.', 'Как же тебе тяжело. Но пройдут дни и месяцы, как улыбка снова будет на твоем лице.','Ты обязательно справишься и пройдешь через все это. Тебе очень тяжело, но крепись. Я даже не представляю, как тебе плохо сейчас.',' Пожалуйся прими мою поддержку и руку помощи. Через месяцы и годы горечь уйдет, а ты будешь счастливым, а все наладится.']


async def send_echo(message: Message):
    a=random.randint(0,8)
    answer=answers[a]
    await message.reply(text=f' {answer}')
    
    
async def send_echo_ultimative(message: Message):
    await message.send_copy(chat_id=message.chat.id)    
    

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)
dp.message.register(send_echo_ultimative)
dp.message.register(send_echo_photo, F.photo)




if __name__ == '__main__':
    dp.run_polling(bot)