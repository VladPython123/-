
from aiogram import  Router, types
from aiogram.types import Message
from aiogram.filters import Command
from keyboard.users_keyboard import buttons1
from database.db import connection
from datetime import datetime

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    user_id=msg.from_user.id
    name = msg.from_user.first_name
    data = datetime.now()
    with connection.cursor() as cursor:
      cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
      existing_user = cursor.fetchall()
      if not existing_user:
           sql_query1 = "INSERT INTO users (name_id, user_id, press_id) VALUES (%s, %s, %s)"
           cursor.execute(sql_query1, (name, user_id, data))
      else:
          pass


    keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1,resize_keyboard=True,)
    await msg.answer(f"ID{user_id}\n\nДоброго дня {name} ми продаємо телефони відомих брендів \n\n орентуйтися по меню щоб заказати телефон. ", reply_markup=keyboard1)

