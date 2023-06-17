import asyncio
from aiogram import Bot, Dispatcher
from config import token
from handlers import main_handler, auth_handler, does_handler



async def main():
    bot=Bot(token=token, parse_mode="HTML")
    dp=Dispatcher()
    dp.include_routers(main_handler.router, auth_handler.router, does_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
    
if __name__=="__main__":
    asyncio.run(main())