from aiogram import  Router, types ,F 
from aiogram.fsm.state import StatesGroup , State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboard.admin_keyboard import buttons3
import json

router = Router()

keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons3,resize_keyboard=True,)

class Form (StatesGroup):
    photo1 = State()
    phone1 =State()
    color1 = State()
    storage1 = State()
    prise1 = State()
    
    photo2 = State()
    phone2 =State()
    color2 = State()
    storage2 = State()
    prise2 = State()
    
    photo3 = State()
    phone3 =State()
    color3 = State()
    storage3 = State()
    prise3 = State()
    
    photo4 = State()
    phone4 =State()
    color4 = State()
    storage4 = State()
    prise4 = State()
    
    photo5 = State()
    phone5 =State()
    color5 = State()
    storage5 = State()
    prise5 = State()
    
    
def read_phone_data():
    with open('admin_handlers\phone.json', 'r' , encoding='utf-8') as file:
        data = json.load(file)
    return data

def update_phone_data(new_data):
    with open('admin_handlers\phone.json', 'w',encoding='utf-8' ) as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)
        
  
phone_data = read_phone_data()  
  
  
           
@router.callback_query(F.data == "Телефон-1" )
async def p1(call: CallbackQuery , state: FSMContext):
        await state.set_state(Form.photo1)
        await call.message.edit_text("Cкеньте фото телефону")             

@router.message(F.photo, Form.photo1)
async def photo(msg: types.Message, state: FSMContext): 
    image_id = msg.photo[-1].file_id
    phone_data["phones"][0]['photo'] = (image_id)
    update_phone_data(phone_data)
    await state.set_state(Form.phone1)
    await msg.answer("Введыть назву телефона ") 
    
    
@router.message(Form.phone1)
async def brand(msg: types.Message, state: FSMContext):
    phone_data['phones'][0]['brand'] = (msg.text)
    update_phone_data(phone_data)
    await state.set_state(Form.color1)
    await msg.answer("Введыть колір ")
 
@router.message(Form.color1)
async def color(msg: types.Message, state: FSMContext):
    phone_data['phones'][0]['color'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть пімять")
    await state.set_state(Form.storage1)
    
    
@router.message(Form.storage1)
async def storage(msg: types.Message, state: FSMContext):
    phone_data['phones'][0]['storage'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть ціну")
    await state.set_state(Form.prise1)
         
    
@router.message(Form.prise1)
async def prise(msg: types.Message, state: FSMContext):
    phone_data['phones'][0]['prise'] = (float(msg.text))
    update_phone_data(phone_data)
    await msg.answer("Товар був змінений",reply_markup=keyboard1)
    await state.clear() 
    
    
@router.callback_query(F.data == "Телефон-2" )
async def p2(call: CallbackQuery , state: FSMContext):
        await state.set_state(Form.photo2)
        await call.message.edit_text("Cкеньте фото телефону")    
    
@router.message(F.photo, Form.photo2)
async def photo(msg: types.Message, state: FSMContext): 
    image_id = msg.photo[-1].file_id
    phone_data["phones"][1]['photo'] = (image_id)
    update_phone_data(phone_data)
    await state.set_state(Form.phone2)
    await msg.answer("Введыть назву телефона ") 
    
    
@router.message(Form.phone2)
async def brand(msg: types.Message, state: FSMContext):
    phone_data['phones'][1]['brand'] = (msg.text)
    update_phone_data(phone_data)
    await state.set_state(Form.color2)
    await msg.answer("Введыть колір ")
 
@router.message(Form.color2)
async def color(msg: types.Message, state: FSMContext):
    phone_data['phones'][1]['color'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть пімять")
    await state.set_state(Form.storage2)
    
    
@router.message(Form.storage2)
async def storage(msg: types.Message, state: FSMContext):
    phone_data['phones'][1]['storage'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть ціну")
    await state.set_state(Form.prise2)
         
    
@router.message(Form.prise2)
async def prise(msg: types.Message, state: FSMContext):
    phone_data['phones'][1]['prise'] = (float(msg.text))
    update_phone_data(phone_data)
    await msg.answer("Товар був змінений",reply_markup=keyboard1)
    await state.clear()
    
    
@router.callback_query(F.data == "Телефон-3" )
async def p3(call: CallbackQuery , state: FSMContext):
        await state.set_state(Form.photo3)
        await call.message.edit_text("Cкеньте фото телефону")    
    
@router.message(F.photo, Form.photo3)
async def photo(msg: types.Message, state: FSMContext): 
    image_id = msg.photo[-1].file_id
    phone_data["phones"][2]['photo'] = (image_id)
    update_phone_data(phone_data)
    await state.set_state(Form.phone3)
    await msg.answer("Введыть назву телефона ") 
    
    
@router.message(Form.phone3)
async def brand(msg: types.Message, state: FSMContext):
    phone_data['phones'][2]['brand'] = (msg.text)
    update_phone_data(phone_data)
    await state.set_state(Form.color3)
    await msg.answer("Введыть колір ")
 
@router.message(Form.color3)
async def color(msg: types.Message, state: FSMContext):
    phone_data['phones'][2]['color'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть пімять")
    await state.set_state(Form.storage3)
    
    
@router.message(Form.storage3)
async def storage(msg: types.Message, state: FSMContext):
    phone_data['phones'][2]['storage'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть ціну")
    await state.set_state(Form.prise3)
         
    
@router.message(Form.prise3)
async def prise(msg: types.Message, state: FSMContext):
    phone_data['phones'][2]['prise'] = (float(msg.text))
    update_phone_data(phone_data)
    await msg.answer("Товар був змінений",reply_markup=keyboard1)
    await state.clear()
    
    
    
@router.callback_query(F.data == "Телефон-4" )
async def p4(call: CallbackQuery , state: FSMContext):
        await state.set_state(Form.photo4)
        await call.message.edit_text("Cкеньте фото телефону")    
    
@router.message(F.photo, Form.photo4)
async def photo(msg: types.Message, state: FSMContext): 
    image_id = msg.photo[-1].file_id
    phone_data["phones"][3]['photo'] = (image_id)
    update_phone_data(phone_data)
    await state.set_state(Form.phone4)
    await msg.answer("Введыть назву телефона ") 
    
    
@router.message(Form.phone4)
async def brand(msg: types.Message, state: FSMContext):
    phone_data['phones'][3]['brand'] = (msg.text)
    update_phone_data(phone_data)
    await state.set_state(Form.color4)
    await msg.answer("Введыть колір ")
 
@router.message(Form.color4)
async def color(msg: types.Message, state: FSMContext):
    phone_data['phones'][3]['color'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть пімять")
    await state.set_state(Form.storage4)
    
    
@router.message(Form.storage4)
async def storage(msg: types.Message, state: FSMContext):
    phone_data['phones'][3]['storage'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть ціну")
    await state.set_state(Form.prise4)
         
    
@router.message(Form.prise4)
async def prise(msg: types.Message, state: FSMContext):
    phone_data['phones'][3]['prise'] = (float(msg.text))
    update_phone_data(phone_data)
    await msg.answer("Товар був змінений",reply_markup=keyboard1)
    await state.clear()
    
@router.callback_query(F.data == "Телефон-5" )
async def p5(call: CallbackQuery , state: FSMContext):
        await state.set_state(Form.photo5)
        await call.message.edit_text("Cкеньте фото телефону")    
  
@router.message(F.photo, Form.photo5)
async def photo(msg: types.Message, state: FSMContext): 
    image_id = msg.photo[-1].file_id
    phone_data["phones"][4]['photo'] = (image_id)
    update_phone_data(phone_data)
    await state.set_state(Form.phone5)
    await msg.answer("Введыть назву телефона ") 
    
    
@router.message(Form.phone5)
async def brand(msg: types.Message, state: FSMContext):
    phone_data['phones'][4]['brand'] = (msg.text)
    update_phone_data(phone_data)
    await state.set_state(Form.color5)
    await msg.answer("Введыть колір ")
 
@router.message(Form.color5)
async def color(msg: types.Message, state: FSMContext):
    phone_data['phones'][4]['color'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть пімять")
    await state.set_state(Form.storage5)
    
    
@router.message(Form.storage5)
async def storage(msg: types.Message, state: FSMContext):
    phone_data['phones'][4]['storage'] = (msg.text)
    update_phone_data(phone_data)
    await msg.answer("Введіть ціну")
    await state.set_state(Form.prise5)
         
    
@router.message(Form.prise5)
async def prise(msg: types.Message, state: FSMContext):
    phone_data['phones'][4]['prise'] = (float(msg.text))
    update_phone_data(phone_data)
    await msg.answer("Товар був змінений",reply_markup=keyboard1)
    await state.clear()        
        
    
    
    
    
    
    
    
            
