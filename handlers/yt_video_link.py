from aiogram import types, Router, F
from aiogram.exceptions import TelegramNetworkError
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile
from pytube.exceptions import RegexMatchError

from keyboards.inline_main import choice_file_type
from utils.misc import Youtube

router = Router()


@router.message(F.text.startswith(("https://www.youtube.com/", "https://m.youtube.com/", "https://youtube.com/")))
async def youtube_video(message: types.Message, state: FSMContext):
    await state.clear()
    try:
        url = message.text
        yt = Youtube(url=url)
    except RegexMatchError:
        await message.reply("<strong>❗Could not find video❗</strong>")
        return
    await message.answer_photo(photo=yt.get_video_preview, caption=yt.title, reply_markup=choice_file_type)
    await state.update_data(yt=yt)


@router.callback_query(F.data == "mp4")
async def download_video(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    yt: Youtube = (await state.get_data()).get("yt")
    msg = await call.message.answer("<strong>Started downloading video ✅</strong>")

    await call.message.delete()

    video = await yt.download_video()

    # TODO If the size exceeds 50 MB, upload to the cloud
    if video:
        try:
            await call.message.answer_video(BufferedInputFile(file=video, filename=yt.title), caption=yt.title)
            await msg.delete()
        except TelegramNetworkError:
            await msg.edit_text(
                text="File too large for uploading. Check telegram api limits <em>https://core.telegram.org/bots/api#senddocument</em>",
                disable_web_page_preview=True)
        finally:
            await state.clear()
    else:
        await msg.edit_text(text="<strong>An error has occurred. Please, try again.</strong>", parse_mode="html")


@router.callback_query(F.data == "mp3")
async def download_audio(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    yt: Youtube = (await state.get_data()).get("yt")
    msg = await call.message.answer("<strong>Started downloading audio ✅</strong>")

    await call.message.delete()

    audio = await yt.download_audio()

    # TODO If the size exceeds 50 MB, upload to the cloud
    if audio:
        try:
            await call.message.answer_audio(BufferedInputFile(file=audio, filename=yt.title), caption=yt.title)
            await msg.delete()
        except TelegramNetworkError:
            await msg.edit_text(
                text="File too large for uploading. Check telegram api limits <em>https://core.telegram.org/bots/api#senddocument</em>",
                disable_web_page_preview=True
            )
        finally:
            await state.clear()
    else:
        await msg.edit_text(text="<strong>An error has occurred. Please, try again.</strong>")
