from youtubesearchpython.__future__ import VideosSearch
from aiogram import Router, F, types
from aiogram.exceptions import TelegramNetworkError
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile


from keyboards.inline_main import choice_video
from utils.misc.youtube import Youtube

router = Router()


@router.message(F.content_type == "text")
async def get_video_name(message: types.Message, state: FSMContext):
    await state.clear()
    answer = ""
    title = message.text
    results = VideosSearch(title, limit=3)

    result = (await results.next())["result"]
    for i, x in enumerate(result, start=1):
        answer += f"[{i}] {x.get('title')} ({x.get('duration')})\n"
        await state.update_data(data={str(i): x.get("link")})
    await message.answer(answer, reply_markup=choice_video)


@router.callback_query(F.data.in_({"1", "2", "3"}))
async def get_video_number(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    msg = await call.message.answer("<strong>Started downloading audio ✅</strong>")
    number = call.data
    url = (await state.get_data()).get(number)

    yt = Youtube(url=url)
    audio = await yt.download_audio()

    if audio:
        try:
            await msg.delete()
            await call.message.answer_audio(BufferedInputFile(file=audio, filename=yt.title), title=yt.title)
        except TelegramNetworkError:
            await msg.edit_text(
                text="File too large for uploading. Check telegram api limits <em>https://core.telegram.org/bots/api#senddocument</em>",
                disable_web_page_preview=True
            )
    else:
        await msg.edit_text(text="<strong>An error has occurred. Please, try again.</strong>", parse_mode="html")


@router.callback_query(F.data == "close")
async def close(call: types.CallbackQuery):
    await call.answer("Closed!")
    await call.message.delete()
