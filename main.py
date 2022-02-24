import logging
import os
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType
from cnop import greet_kb

button_hi = KeyboardButton('Сливы')
button_hi2 = KeyboardButton('Архивы') 
button_hi3 = KeyboardButton('Приватка') 
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_hi,button_hi2,button_hi3)

Arhivi = KeyboardButton('Школьницы')
Arhivi2 = KeyboardButton('Милфы')
menu = KeyboardButton('Главное меню') 
Arhivis = ReplyKeyboardMarkup(resize_keyboard=True)
Arhivis.add(Arhivi,Arhivi2,menu)

Privatka = KeyboardButton('Купить')
Otzivi = KeyboardButton('Отзывы')
menu = KeyboardButton('Главное меню')
press = ReplyKeyboardMarkup(resize_keyboard=True)
press.add(Privatka,Otzivi,menu)

Pokypka_arhiv = KeyboardButton('Купить Архив со Шк')
menu = KeyboardButton('Главное меню')
arif = ReplyKeyboardMarkup(resize_keyboard=True)
arif.add(Pokypka_arhiv,menu)

Pokypka_arhiv2 = KeyboardButton('Купить Архив со Милфами')
menu = KeyboardButton('Главное меню')
arif2 = ReplyKeyboardMarkup(resize_keyboard=True)
arif2.add(Pokypka_arhiv2,menu)

sub_inline_markup = InlineKeyboardMarkup(row_width=1)
ssilka_oplata = InlineKeyboardButton(text="Месяц приватки 250р", callback_data="submonth")
sub_inline_markup.insert(ssilka_oplata)

sub_inline_shkool_markup = InlineKeyboardMarkup(row_width=1)
ssilka_oplata_shkool = InlineKeyboardButton(text="Покупка архива школьниц", callback_data="shkool")
sub_inline_shkool_markup.insert(ssilka_oplata_shkool)

sub_inline_milfs_markup = InlineKeyboardMarkup(row_width=1)
ssilka_oplata_milfs = InlineKeyboardButton(text="Покупка архива милф", callback_data="milfs")
sub_inline_milfs_markup.insert(ssilka_oplata_milfs)


TOKEN_KASSA = "381764678:TEST:33651"
API_TOKEN = "5220046644:AAEHt4ki_jK3mH8S0ds8-2UNxfSqJ5xZCtw"
# Configure logging 
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN) 
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет, я бот приват Сливов @slivu97\n<◇>~•~ОБЬЯВЛЕНИЕ~•~<◇>\nБот в ранем доступе! прошу не покупать архивы\nПотратите деньги в пустую.\n<◇>~•~ОБЬЯВЛЕНИЕ~•~<◇>\nВыбери что тебя интересует",reply_markup=greet_kb)

@dp.message_handler(text=['Главное меню'])
async def glav_menu(message: types.Message):
    await message.answer("~~~~Вы_Перешли_В~~~~\n~~~главное меню~~~",reply_markup=greet_kb)

@dp.message_handler(text=['Сливы'])
async def nashi_slivu(message: types.Message):
    await message.answer("Наши сливы\n№1 - @slivu97\n№2 - @slivu96")

@dp.message_handler(text=['Архивы'])
async def arhifs_menu(message: types.Message):
    await message.answer("Есть архивы вот такие:\n№1-Школьницы\n№2-Милфы",reply_markup=Arhivis)

@dp.message_handler(text=['Приватка'])
async def privatochka(message: types.Message):
    await message.answer("Вход в приватку стоит 250р\nУспей пока цены не поднялись",reply_markup=press)

@dp.message_handler(text=['Школьницы'])
async def shk(message: types.Message):
    await message.answer("Архив со шк 1гб Цена 500р", reply_markup=arif)

@dp.message_handler(text=['Милфы'])
async def mifs(message: types.Message):
    await message.answer("Архив со Милфами 1гб Цена 250р",reply_markup=arif2)

@dp.message_handler(text=['Купить Архив со Шк'])
async def arhif_shk(message: types.Message):
    await message.answer("◇ВОТ ИНЛАЙН КНОПКА ДЛЯ ОПЛАТЫ◇", reply_markup=sub_inline_shkool_markup)

@dp.message_handler(text=['Купить Архив со Милфами'])
async def arhif_mifs(message: types.Message):
    await message.answer("◇ВОТ ИНЛАЙН КНОПКА ДЛЯ ОПЛАТЫ◇", reply_markup=sub_inline_milfs_markup)
   
@dp.message_handler(text=['Рефиральная Ссылка'])
async def ref_silka(message: types.Message):
    await message.answer("Ещё не создана")

@dp.message_handler(text=['Купить'])
async def process_h2_command(message: types.Message):
    await message.answer("◇ВОТ ИНЛАЙН КНОПКА ДЛЯ ОПЛАТЫ◇", reply_markup=sub_inline_markup)
   
@dp.message_handler(text=['Отзывы'])
async def procss_hi2_command(message: types.Message):
    await message.answer("Лови")
    await bot.send_photo(message.chat.id,photo=open('1.jpg', 'rb'))
    await bot.send_photo(message.chat.id,photo=open('2.jpg', 'rb'))
    await bot.send_photo(message.chat.id,photo=open('3.jpg', 'rb'))

@dp.message_handler(text=['Пополнить'])
async def esli_kupil_privat(message: types.Message):
    await message.answer("◇ВОТ ИНЛАЙН КНОПКА ДЛЯ ОПЛАТЫ◇", reply_markup=sub_inline_markup)
 
@dp.callback_query_handler(text=['shkool'])
async def submonth(callp: types.CallbackQuery):
    await bot.delete_message(callp.from_user.id, callp.message.message_id)
    await bot.send_invoice(chat_id=callp.from_user.id, title="Покупка архива школьниц", description="Покупка архива со школьницами", payload="month_shkool", provider_token=TOKEN_KASSA, currency="RUB", start_parameter="bot_shk",prices=[{"label": "Руб", "amount": 50000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay_shk(message: types.Message):
    if message.successful_payment.invoice_payload == "month_shkool":
        await message.answer(f"Держи ссылку\nhttps://mega.nz/folder/vaYHlYTJ#jlFyV7T2uq3-J4X1nenP1A")

@dp.callback_query_handler(text=['milfs'])
async def milfs_arhiv(calls: types.CallbackQuery):
    await bot.delete_message(calls.from_user.id, calls.message.message_id)
    await bot.send_invoice(chat_id=calls.from_user.id, title="Покупка архива милфами", description="Покупка архива с милфами", payload="month_filfs", provider_token=TOKEN_KASSA, currency="RUB", start_parameter="bot_milfs",prices=[{"label": "Руб", "amount": 25000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay_milf(message: types.Message):
    if message.successful_payment.invoice_payload == "month_filfs":
        await message.answer(f"Держи ссылку\nНа милф")

@dp.callback_query_handler(text=['submonth'])
async def submonth(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Покупка привата", description="Покупка доступа к приват каналу", payload="month_sub", provider_token=TOKEN_KASSA, currency="RUB", start_parameter="test_bots",prices=[{"label": "Руб", "amount": 25000}])
    
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == "month_sub":
        chat_id = -1001554743391
        expire_date = datetime.now() + timedelta(days=1)
        link = await bot.create_chat_invite_link(chat_id, expire_date.timestamp, 1)
        await message.answer(f"Держи ссылку\n{link.invite_link}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
