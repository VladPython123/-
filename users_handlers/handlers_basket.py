from aiogram import  Router, types, F
from keyboard.users_keyboard import buttons3 , buttons1
import json

router = Router()
user_baskets = {}

def read_phone():
    with open('admin_handlers\phone.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data


@router.callback_query(F.data == "iPhone")    
async def iPhone (call: types.CallbackQuery ) ->  user_baskets:
        user_id = call.from_user.id
        phone_data = read_phone()
        if user_id not in user_baskets:
                user_baskets[user_id] = {"Телефон1": 0, "Телефон2": 0, "Телефон3": 0, "Телефон4": 0, "Телефон5": 0,"total": 0}    
        price = [phones['prise'] for phones in phone_data['phones']]
        price1 = price[0]                      
        user_baskets[user_id]["Телефон1"] += 1
        user_baskets[user_id]["total"] += price1
        await call.answer('Ви успішно додали товар до кошика')
             
             
             
             
@router.callback_query(F.data == "Galaxy")    
async def Galaxy (call: types.CallbackQuery ) -> user_baskets:    
        user_id = call.from_user.id
        phone_data = read_phone()
        if user_id not in user_baskets:
                user_baskets[user_id] = {"Телефон1": 0, "Телефон2": 0, "Телефон3": 0, "Телефон4": 0, "Телефон5": 0,"total": 0}    
        price = [phones['prise'] for phones in phone_data['phones']]
        price2 = price[1]                      
        user_baskets[user_id]["Телефон2"] += 1
        user_baskets[user_id]["total"] += price2
        await call.answer('Ви успішно додали товар до кошика')
           
           
           
           
@router.callback_query(F.data == "Redmi")    
async def Redmi (call: types.CallbackQuery ) -> user_baskets:    
        user_id = call.from_user.id
        phone_data = read_phone()
        if user_id not in user_baskets:
                user_baskets[user_id] = {"Телефон1": 0, "Телефон2": 0, "Телефон3": 0, "Телефон4": 0, "Телефон5": 0,"total": 0}    
        price = [phones['prise'] for phones in phone_data['phones']]
        price3 = price[2]                      
        user_baskets[user_id]["Телефон3"] += 1
        user_baskets[user_id]["total"] += price3
        await call.answer('Ви успішно додали товар до кошика')
                 
                 
@router.callback_query(F.data == "POCO")    
async def POCO (call: types.CallbackQuery ) -> user_baskets:   
        user_id = call.from_user.id
        phone_data = read_phone()
        if user_id not in user_baskets:
                user_baskets[user_id] = {"Телефон1": 0, "Телефон2": 0, "Телефон3": 0, "Телефон4": 0, "Телефон5": 0,"total": 0}    
        price = [phones['prise'] for phones in phone_data['phones']]
        price4 = price[3]                      
        user_baskets[user_id]["Телефон4"] += 1
        user_baskets[user_id]["total"] += price4
        await call.answer('Ви успішно додали товар до кошика')
               
               
               
               
@router.callback_query(F.data == "HUAWEI")    
async def HUAWEI (call: types.CallbackQuery ) -> user_baskets:    
        user_id = call.from_user.id
        phone_data = read_phone()
        if user_id not in user_baskets:
                user_baskets[user_id] = {"Телефон1": 0, "Телефон2": 0, "Телефон3": 0, "Телефон4": 0, "Телефон5": 0,"total": 0}    
        price = [phones['prise'] for phones in phone_data['phones']]
        price5 = price[4]                      
        user_baskets[user_id]["Телефон5"] += 1
        user_baskets[user_id]["total"] += price5
        await call.answer('Ви успішно додали товар до кошика')
         
         
         
          
@router.callback_query(F.data == "Корзина")
async def basket(call: types.CallbackQuery ) -> user_baskets:
        user_id = call.from_user.id
        if user_id not in user_baskets:
                await call.answer("Кошик порожній!")
                return
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=buttons3,resize_keyboard=True,)
        await call.message.edit_text(f"""Кошик:\n\n Айфон    : {user_baskets[user_id]['Телефон1']}\nСамсунг : {user_baskets[user_id]['Телефон2']}\nРедмі     : {user_baskets[user_id]['Телефон3']}\nПоко      : {user_baskets[user_id]['Телефон4']}\nХаувей   : {user_baskets[user_id]['Телефон5']}
                                     \n\nВаш рахунок: {user_baskets[user_id]['total']}$""", reply_markup=keyboard3)
  
           
@router.callback_query(F.data == "Обнулити заказ")
async def basket_0(call: types.CallbackQuery ):
    global user_baskets , user_id 
    user_id=call.from_user.id
    user_baskets[user_id]["total"] = 0
    user_baskets[user_id]["Телефон1"] = 0
    user_baskets[user_id]["Телефон2"] = 0
    user_baskets[user_id]["Телефон3"] = 0
    user_baskets[user_id]["Телефон4"] = 0
    user_baskets[user_id]["Телефон5"] = 0
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons1,resize_keyboard=True,)
    await call.message.edit_text(f"Кошик порожній", reply_markup=keyboard2) 
