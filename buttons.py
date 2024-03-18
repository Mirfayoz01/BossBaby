from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


btn = [
    [types.KeyboardButton(text="O'g'il 🙍‍♂️"), types.KeyboardButton(text="Qiz 🙍‍♀️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True, input_field_placeholder="Tanlang:") # noqa

btn_boy1 = [
    [types.KeyboardButton(text="Bosh kiyim 🧢"), types.KeyboardButton(text="Ustki kiyim 👕")], # noqa
    [types.KeyboardButton(text="Shim 👖"), types.KeyboardButton(text="Oyoq kiyim 🥾")], # noqa
    [types.KeyboardButton(text="🔙 Orqaga qaytish")]  # noqa
]
button_boy = types.ReplyKeyboardMarkup(keyboard=btn_boy1, resize_keyboard=True, input_field_placeholder="Tanlang:") # noqa

btn_girl1 = [
    [types.KeyboardButton(text="Bosh kiyim 👒"), types.KeyboardButton(text="Ustki kiyim 👗")], # noqa
    [types.KeyboardButton(text="Shim va yupkalar 👗"), types.KeyboardButton(text="Oyoq kiyim 👠")], # noqa
    [types.KeyboardButton(text="🔙 Orqaga qaytish")] # noqa
]
button_girl = types.ReplyKeyboardMarkup(keyboard=btn_girl1, resize_keyboard=True, input_field_placeholder="Tanlang:") # noqa



inlineBtn2 = InlineKeyboardMarkup(inline_keyboard=[ # noqa
    [InlineKeyboardButton(text="Buy",callback_data="pay_1")] # noqa
])