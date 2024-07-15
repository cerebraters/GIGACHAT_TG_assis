from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


help_keyboard = [
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")
    #InlineKeyboardButton(text="Очистить диалог", callback_data="exit")
    ]
]

help_keyboard = InlineKeyboardMarkup(inline_keyboard=help_keyboard)
