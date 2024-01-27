import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import users_handlers.handlers_start as handlers_start 
import admin_handlers.admin_panely as admin_panely
import admin_handlers.meny_phone as meny_phone
import admin_handlers.edition_phone as edition_phone
import users_handlers.handlers_phone as meny_phone
import users_handlers.handlers_basket as handlers_basket 
import users_handlers.state as state

BOT_TOKEN = '6862881309:AAGb2D4bXWM7rKbnU_zzUbDp6BqneJqrDRI'

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(meny_phone.router, 
                       handlers_basket.router, handlers_start.router, state.router
                       , admin_panely.router, meny_phone.router
                       , edition_phone.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
