import asyncio
import logging


async def main():
    from aiogram import Bot, Dispatcher
    from data.config import config

    from handlers import yt_video_link_router
    from handlers import yt_video_name_router

    bot = Bot(token=config.tg_bot.get_token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(yt_video_link_router)
    dp.include_router(yt_video_name_router)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S')

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(f"[!!! Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
