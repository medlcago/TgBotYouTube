from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_file_type = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Скачать MP4", callback_data="mp4"),
        InlineKeyboardButton(text="Скачать MP3", callback_data="mp3")
    ]
])

choice_video = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="[1]", callback_data="1"),
        InlineKeyboardButton(text="[2]", callback_data="2"),
        InlineKeyboardButton(text="[3]", callback_data="3")
    ],
    [
        InlineKeyboardButton(text="❌ Закрыть", callback_data="close")
    ]
])
