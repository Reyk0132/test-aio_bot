from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = 'каталог'
cart = 'корзина'
delivery_status = 'статус заказа'

settings = 'настройки католога'
orders = 'заказы'
questions = 'вопросы'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)
    
    await message.answer("Меню", reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(cart)
    markup.add(delivery_status)

    await message.answer("Меню", reply_markup=markup)