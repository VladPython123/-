from aiogram.fsm.state import StatesGroup , State
from aiogram.fsm.context import FSMContext
from aiogram import F, types, Router , Bot
from aiogram.types import CallbackQuery
from keyboard.users_keyboard import buttons4 , buttons1
from users_handlers.handlers_basket import user_baskets 
from keyboard.admin_keyboard import  buttons01
from database.db import connection
import json

router = Router() 

name  = ''
nomer = ''
region = ''


chat_id = "-1001996686892"

class Form (StatesGroup):
    name1 = State()
    nomer2 = State()
    region3 = State()
    
    
def read_phone_data():
    with open(f'admin_handlers\end.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data    
    
def update_phone_data(new_data):
    with open('admin_handlers\end.json', 'w',encoding='utf-8' ) as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)   
    
   
@router.callback_query(F.data == "Заказати" )
async def zakaz(call: CallbackQuery , state: FSMContext):
    user_id = call.from_user.id
    if user_baskets[user_id]['total'] == 0:
        await call.message.answer("Вас порожня корзина") 
    else:
        names = call.from_user.first_name
        kb = [[types.KeyboardButton(text=f"{names}")],]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,one_time_keyboard=True)
        await state.set_state(Form.name1)
        await call.message.answer("Введіть своє імя:", reply_markup=keyboard) 
    
@router.message(Form.name1)
async def name1(msg: types.Message, state: FSMContext):
    global name
    name = msg.text.strip()
    await state.set_state(Form.nomer2)
    await msg.answer("Введіть свій номер телефону ")
   
    
@router.message(Form.nomer2)
async def nomer1(msg: types.Message, state: FSMContext):
    global nomer
    if msg.text.isdigit:
        nomer = msg.text.strip()
        await msg.answer("Введіть де ви проживаєте ")
        await state.set_state(Form.region3)
    else:
        await msg.answer("Вветь числами !!!")
           
    
@router.message(Form.region3)
async def region1(msg: types.Message, state: FSMContext):
    global region
    region = msg.text.strip()
    keyboard4 = types.InlineKeyboardMarkup(inline_keyboard=buttons4,resize_keyboard=True,)
    await msg.answer(f"Ім'я: {name} \n Номер: {nomer} \n Регіон: {region} ",reply_markup=keyboard4)
    await state.clear() 
    
    
@router.callback_query(F.data == "Повторити" )
async def zakaz2(call: CallbackQuery , state: FSMContext):
        names = call.from_user.first_name
        kb = [[types.KeyboardButton(text=f"{names}")],]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,one_time_keyboard=True)
        await state.set_state(Form.name1)
        await call.message.answer("Введіть своє імя:", reply_markup=keyboard)
 
    
@router.callback_query(F.data == "Заказати1")
async def zakaz(call: CallbackQuery , bot: Bot):
    phone_data = read_phone_data() 
    user_id = call.from_user.id
    phone_data['id_user'] = user_id
    update_phone_data(phone_data)
    with connection.cursor() as cursor:
            cursor.execute(
              f"""UPDATE users SET zakaz_bot  = zakaz_bot + 1   """ 
            )
    await call.answer(text="Вітаю ваший заказ був відісланий🎉",show_alert=True)
    keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1,resize_keyboard=True,)
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons01,resize_keyboard=True,)
    await call.message.edit_text("Вітаю ваз заказ був відісланий !!!!", reply_markup=keyboard1)
    #basket_content = "\n".join([f"{item}: {count}" for item, count in user_baskets[user_id].items()])
    await bot.send_message(chat_id , f"""Ім'я: {name} \n Номер: {nomer} \n Регіон: {region} \n\n Айфон    : {user_baskets[user_id]['Телефон1']}\nСамсунг : {user_baskets[user_id]['Телефон2']}\nРедмі     : {user_baskets[user_id]['Телефон3']}\nПоко      : {user_baskets[user_id]['Телефон4']}\nХаувей   : {user_baskets[user_id]['Телефон5']}
                                     \n\nВаш рахунок: {user_baskets[user_id]['total']}$ """,reply_markup=keyboard2)
    user_baskets[user_id]["total"] = 0
    user_baskets[user_id]["Телефон1"] = 0
    user_baskets[user_id]["Телефон2"] = 0
    user_baskets[user_id]["Телефон3"] = 0
    user_baskets[user_id]["Телефон4"] = 0
    user_baskets[user_id]["Телефон5"] = 0
    
