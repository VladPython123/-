from aiogram import types 
import json

def read_phone():
    with open('admin_handlers\phone.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data

phone_data = read_phone()
brands = [phones['brand'] for phones in phone_data['phones']]
nomer1 = brands[0]  
nomer2 = brands[1]
nomer3 = brands[2]
nomer4 = brands[3]
nomer5 = brands[4]



buttons1 = [
           [types.InlineKeyboardButton(text="Товари", callback_data="Товари"),],
           [types.InlineKeyboardButton(text="Корзина", callback_data="Корзина"), ] ,
           ]



buttons2 = [
           [types.InlineKeyboardButton(text=f"{nomer1}", callback_data="Телефон-01"),],
           [types.InlineKeyboardButton(text=f"{nomer2}", callback_data="Телефон-02"), ] ,
           [types.InlineKeyboardButton(text=f"{nomer3}", callback_data="Телефон-03"),],
           [types.InlineKeyboardButton(text=f"{nomer4}", callback_data="Телефон-04"),   ],
           [types.InlineKeyboardButton(text=f"{nomer5}", callback_data="Телефон-05"),    ],
           [types.InlineKeyboardButton(text=f"⬅️Меню", callback_data="Меню"),    ],
           ]

buttons3 = [
           [types.InlineKeyboardButton(text="Обнулити заказ ", callback_data="Обнулити заказ"),],
           [types.InlineKeyboardButton(text="Заказати", callback_data="Заказати"),],
           [types.InlineKeyboardButton(text="⬅️Меню", callback_data="Меню"), ] ,
           ]




but1 = [
           [types.InlineKeyboardButton(text="Добавити до корзини ➕ ", callback_data="iPhone"),],
           [types.InlineKeyboardButton(text="⬅️Назад", callback_data="Назад"), ] ,
           ]
but2 = [
           [types.InlineKeyboardButton(text="Добавити до корзини ➕ ", callback_data="Galaxy"),],
           [types.InlineKeyboardButton(text="⬅️Назад", callback_data="Назад"), ] ,
           ]
but3 = [
           [types.InlineKeyboardButton(text="Добавити до корзини ➕ ", callback_data="Redmi"),],
           [types.InlineKeyboardButton(text="⬅️Назад", callback_data="Назад"), ] ,
           ]
but4 = [
           [types.InlineKeyboardButton(text="Добавити до корзини ➕ ", callback_data="POCO"),],
           [types.InlineKeyboardButton(text="⬅️Назад", callback_data="Назад"), ] ,
           ]
but5 = [
           [types.InlineKeyboardButton(text="Добавити до корзини ➕ ", callback_data="HUAWEI"),],
           [types.InlineKeyboardButton(text="⬅️Назад", callback_data="Назад"), ] ,
           ]



buttons4 = [
           [types.InlineKeyboardButton(text="Повторити", callback_data="Повторити"),],
           [types.InlineKeyboardButton(text="Заказати", callback_data="Заказати1"),],
           ]


