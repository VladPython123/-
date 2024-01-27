from aiogram import  Router, types, F , Bot
from aiogram.filters import Command
from aiogram.types import Message
from keyboard.admin_keyboard import buttons2 , buttons3
from database.db import connection
import json


router = Router()
chat_id = '-1001996686892'


def read_phone():
    with open('admin_handlers\end.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data

def update_phone(new_data):
    with open('admin_handlers\end.json', 'w',encoding='utf-8' ) as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)


def read_phone():
    with open('admin_handlers\phone.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data


def update_phone(new_data):
    with open('admin_handlers\phone.json', 'w',encoding='utf-8' ) as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)




@router.message(Command("Admin"))
async def start_admin_panel(msg: Message):
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
        await msg.answer('Управління ботом', reply_markup=keyboard1) 
        

@router.callback_query(F.data == 'Меню2')
async def meny_panel(call:  types.CallbackQuery):
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
        await call.message.edit_text('Управління ботом', reply_markup=keyboard1)        
           


@router.callback_query(F.data == 'Пітвердети')
async def proverca(call: types.CallbackQuery  , bot: Bot):
    button_data = read_phone()
    bat = [button_data['id_user']]
    nomer1 = bat[0]
    await bot.send_message(chat_id , f"Заказ підвердяний" )       
    await bot.send_message(chat_id=nomer1, text="Ваш заказ був пытвердяний")
 
 
     
@router.callback_query(F.data == 'Відмінити')
async def proverca(call: types.CallbackQuery  , bot: Bot):
    button_data = read_phone()
    bat = [button_data['id_user']]
    nomer1 = bat[0]
    await bot.send_message(chat_id , f"Заказ відміняний" )       
    await bot.send_message(chat_id=nomer1, text="Ваш заказ був на жаль відміняний")  
    
    
    
    
@router.callback_query(F.data == 'Аналітика')
async def Analitik(call: types.CallbackQuery):
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
              f"""SELECT id1 FROM users ORDER BY id1 DESC LIMIT 1;""" )
            users1 = cursor.fetchone()[0]
            cursor.execute(
              f"""SELECT  zakaz_bot FROM users ORDER BY zakaz_bot DESC LIMIT 1;""" )
            zakaz = cursor.fetchone()[0]
            keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons3,resize_keyboard=True,)
            await call.message.edit_text(f"""
                                 Аналітика \n\n Запуск бота за весь час: {users1}\n\nВсього кількість заказів: {zakaz}
                                 """ , reply_markup=keyboard2
                                 )
            
@ router.callback_query(F.data == 'Змінити_товари')
async def meny_panel(call:  types.CallbackQuery):
        phone_data = read_phone()
        brands = [phones['brand'] for phones in phone_data['phones']]
        nomer1 = brands[0]  
        nomer2 = brands[1]
        nomer3 = brands[2]
        nomer4 = brands[3]
        nomer5 = brands[4]
        buttons4 = [
           [types.InlineKeyboardButton(text=f"{nomer1}", callback_data="Телефон-1"),],
           [types.InlineKeyboardButton(text=f"{nomer2}", callback_data="Телефон-2"), ] ,
           [types.InlineKeyboardButton(text=f"{nomer3}", callback_data="Телефон-3"),],
           [types.InlineKeyboardButton(text=f"{nomer4}", callback_data="Телефон-4"),   ],
           [types.InlineKeyboardButton(text=f"{nomer5}", callback_data="Телефон-5"),    ],
           [types.InlineKeyboardButton(text="⬅️Меню", callback_data="Меню2"),    ],
           ]
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons4,resize_keyboard=True,)
        await call.message.edit_text('Зміна товару                ➕', reply_markup=keyboard1)        


