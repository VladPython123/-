from aiogram import  Router, types, F 
from keyboard.users_keyboard import buttons1,buttons2
from keyboard.users_keyboard import but1 , but2 , but3 , but4 , but5
import json

msg1 = None
msg2 = None

router = Router()

def read_phone():
    with open('admin_handlers\phone.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data


@router.callback_query(F.data == "Товари")
@router.callback_query(F.data == "Назад")
async def menu(call: types.CallbackQuery ):
    global msg2 , msg1
    try:
        keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
        msg1 = await call.message.edit_text("Всі телефони які в нас є в наявності.", reply_markup=keyboard2)
    except:
        await msg2.delete() 
        keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
        msg1 = await call.message.answer("Всі телефони які в нас є в наявності.", reply_markup=keyboard2)

@router.callback_query(F.data == "Меню")
async def menu1(call: types.CallbackQuery ):
    keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1)
    await call.message.edit_text("Меню:                   ➕ ", reply_markup=keyboard1)
    


#Айфон
@router.callback_query(F.data == 'Телефон-01')
async def Phone1(call: types.CallbackQuery ) -> msg1:
        global msg2 
        await msg1.delete()
        phone_data = read_phone()
        photo = [phones['photo'] for phones in phone_data['phones']]
        brands = [phones['brand'] for phones in phone_data['phones']]
        color = [phones['color'] for phones in phone_data['phones']]
        storage = [phones['storage'] for phones in phone_data['phones']]
        price = [phones['prise'] for phones in phone_data['phones']]
        nomer1 = brands[0]  
        color1 = color[0]
        storage1 = storage[0]
        price1 = price[0]  
        photo1 = photo[0]
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but1 ,resize_keyboard=True,)
        msg2 = await call.message.answer_photo(
                                    photo1, caption=
                                    f" {nomer1} \n  \n Память: {storage1} \n Колір: {color1} \n Гарантія: 12 місяців\n Ціна: {price1}$ "
                                    , reply_markup=keyboard3)    
         
        
#Самсунг
@router.callback_query(F.data == "Телефон-02")
async def Phone2(call: types.CallbackQuery ):
        global msg1 ,msg2
        await msg1.delete()
        phone_data = read_phone()
        photo = [phones['photo'] for phones in phone_data['phones']]
        brands = [phones['brand'] for phones in phone_data['phones']]
        color = [phones['color'] for phones in phone_data['phones']]
        storage = [phones['storage'] for phones in phone_data['phones']]
        price = [phones['prise'] for phones in phone_data['phones']]
        nomer1 = brands[1]  
        color1 = color[1]
        storage1 = storage[1]
        price1 = price[1]  
        photo1 = photo[1]
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but2 ,resize_keyboard=True,)
        msg2 = await call.message.answer_photo(
                                    photo1, caption=
                                    f" {nomer1} \n  \n Память: {storage1} \n Колір: {color1} \n Гарантія: 12 місяців\n Ціна: {price1}$ "
                                    , reply_markup=keyboard3)


#Редмы
@router.callback_query(F.data == "Телефон-03")
async def Phone3(call: types.CallbackQuery ):
        global msg1 ,  msg2 
        await msg1.delete()
        phone_data = read_phone()
        photo = [phones['photo'] for phones in phone_data['phones']]
        brands = [phones['brand'] for phones in phone_data['phones']]
        color = [phones['color'] for phones in phone_data['phones']]
        storage = [phones['storage'] for phones in phone_data['phones']]
        price = [phones['prise'] for phones in phone_data['phones']]
        nomer1 = brands[2]  
        color1 = color[2]
        storage1 = storage[2]
        price1 = price[2]  
        photo1 = photo[2]
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but3 ,resize_keyboard=True,)
        msg2 = await call.message.answer_photo(
                                    photo1, caption=
                                    f" {nomer1} \n  \n Память: {storage1} \n Колір: {color1} \n Гарантія: 12 місяців\n Ціна: {price1}$ "
                                    , reply_markup=keyboard3)
               
#Поко
@router.callback_query(F.data == "Телефон-04")
async def Phone4(call: types.CallbackQuery ):
        global  msg1 , msg2 
        await msg1.delete()
        phone_data = read_phone()
        photo = [phones['photo'] for phones in phone_data['phones']]
        brands = [phones['brand'] for phones in phone_data['phones']]
        color = [phones['color'] for phones in phone_data['phones']]
        storage = [phones['storage'] for phones in phone_data['phones']]
        price = [phones['prise'] for phones in phone_data['phones']]
        nomer1 = brands[3]  
        color1 = color[3]
        storage1 = storage[3]
        price1 = price[3]  
        photo1 = photo[3]
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but4 ,resize_keyboard=True,)
        msg2 = await call.message.answer_photo(
                                    photo1, caption=
                                    f" {nomer1} \n  \n Память: {storage1} \n Колір: {color1} \n Гарантія: 12 місяців\n Ціна: {price1}$ "
                                    , reply_markup=keyboard3)
    
#Хаувей    
@router.callback_query(F.data == "Телефон-05")
async def Phone5(call: types.CallbackQuery ):
        global  msg1 , msg2 
        await msg1.delete()
        phone_data = read_phone()
        photo = [phones['photo'] for phones in phone_data['phones']]
        brands = [phones['brand'] for phones in phone_data['phones']]
        color = [phones['color'] for phones in phone_data['phones']]
        storage = [phones['storage'] for phones in phone_data['phones']]
        price = [phones['prise'] for phones in phone_data['phones']]
        nomer1 = brands[4]  
        color1 = color[4]
        storage1 = storage[4]
        price1 = price[4]  
        photo1 = photo[4]
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but5 ,resize_keyboard=True,)
        msg2 = await call.message.answer_photo(
                                    photo1, caption=
                                    f" {nomer1} \n  \n Память: {storage1} \n Колір: {color1} \n Гарантія: 12 місяців\n Ціна: {price1}$ "
                                    , reply_markup=keyboard3)
