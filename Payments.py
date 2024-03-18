from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from root import PAY_TOKEN


async def order_1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 🧢", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/rs0rnT3w/IMG-20240210-111331.jpg", # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=80_000_00), # noqa
                               LabeledPrice(label="QQS", amount=10_000_00), # noqa
                               LabeledPrice(label="Skidka", amount=-20_200_00) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 🧢', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def order_2(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 🧢", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/6Tx0JckR",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=120_000_00), # noqa
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 🧢',# noqa
                           request_timeout=15
                           )


async def pre_checkout_query2(pre_checkout_query2: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query2.id, ok=True)


async def order_3(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 🧢", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/Fdy0HtMS",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=120_000_00), # noqa
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 🧢', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query3(pre_checkout_query3: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query3.id, ok=True)


async def order_4(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 🧢", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/VJv9BVty",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=60_000_00), # noqa
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-14_999_99) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 🧢', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query4(pre_checkout_query4: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query4.id, ok=True)


async def order_5(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 🧢", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/1gNpbVMJ",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=60_000_00), # noqa
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-14_999_99) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 🧢', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query5(pre_checkout_query5: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query5.id, ok=True)


#*************************************************************************************************************# noqa


async def order_6(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Ustki Kiyim 👕", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/QH0k73Hk",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=300_000_00), # noqa
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-29_999_99) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki Kiyim 👕', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query6(pre_checkout_query6: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query6.id, ok=True)


async def order_7(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Ustki Kiyim 👕", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/Fkh3fWvB",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=450_000_00), # noqa
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki Kiyim 👕', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query7(pre_checkout_query7: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query7.id, ok=True)



async def order_8(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki Kiyim 👕", # noqa
                           description="O'g'il bolalar uchun ", # noqa
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/S2FW4Qvq",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=240_000_00), # noqa
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00) # noqa
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki Kiyim 👕', # noqa
                           request_timeout=15
                           )


async def pre_checkout_query8(pre_checkout_query8: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query8.id, ok=True)



async def order_9(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki Kiyim 👕",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/0b80rQ2y",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=260_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki Kiyim 👕',
                           request_timeout=15
                           )


async def pre_checkout_query9(pre_checkout_query9: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query9.id, ok=True)



async def order_10(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki Kiyim 👕",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/bdPQFJn9",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=210_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki Kiyim 👕',
                           request_timeout=15
                           )


async def pre_checkout_query10(pre_checkout_query10: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query10.id, ok=True)


async def order_11(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim 👖",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/87xvdPDW",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim 👖',
                           request_timeout=15
                           )


async def pre_checkout_query11(pre_checkout_query11: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query11.id, ok=True)


async def order_12(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim 👖",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/QH41tJyf",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=110_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim 👖',
                           request_timeout=15
                           )


async def pre_checkout_query12(pre_checkout_query12: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query12.id, ok=True)



async def order_13(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Shim 👖",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/xNjNjXyr",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=200_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim 👖',
                           request_timeout=15
                           )


async def pre_checkout_query13(pre_checkout_query13: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query13.id, ok=True)



async def order_14(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Shim 👖",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/mP1zrfMr",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim 👖',
                           request_timeout=15
                           )


async def pre_checkout_query14(pre_checkout_query14: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query14.id, ok=True)


async def order_15(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim 👖",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/jL5nGJSP",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=140_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim 👖',
                           request_timeout=15
                           )


async def pre_checkout_query15(pre_checkout_query15: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query15.id, ok=True)



async def order_16(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 🥾",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/cgS8j9vL",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=220_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 🥾',
                           request_timeout=15
                           )


async def pre_checkout_query16(pre_checkout_query16: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query16.id, ok=True)


async def order_17(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 🥾",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/5YSFMBzq",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=260_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 🥾',
                           request_timeout=15
                           )


async def pre_checkout_query17(pre_checkout_query17: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query17.id, ok=True)



async def order_18(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 🥾",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/HVh8HsrK",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=290_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 🥾',
                           request_timeout=15
                           )


async def pre_checkout_query18(pre_checkout_query18: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query18.id, ok=True)



async def order_19(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 🥾",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/CZyZBPHs",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=310_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 🥾',
                           request_timeout=15
                           )


async def pre_checkout_query19(pre_checkout_query19: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query19.id, ok=True)


async def order_20(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 🥾",
                           description="O'g'il bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://postimg.cc/z3pRtk8q",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=240_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 🥾',
                           request_timeout=15
                           )


async def pre_checkout_query20(pre_checkout_query20: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query20.id, ok=True)


#***************************************************************************************************************************# noqa
#**********************************************************BOLLAR TUGADI****************************************************# noqa
#***************************************************************************************************************************# noqa


#***************************************************************************************************************************# noqa
#**********************************************************QIZLARNIKI BOSHLANDI*********************************************# noqa
#***************************************************************************************************************************# noqa


async def order_21(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 👒",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/TPPYJ6KL/photo-2-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=120_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_200_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 👒',
                           request_timeout=15
                           )


async def pre_checkout_query21(pre_checkout_query21: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query21.id, ok=True)


async def order_22(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 👒",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/j2ysSqF9/photo-3-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=80_000_00),
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 👒',
                           request_timeout=15
                           )


async def pre_checkout_query22(pre_checkout_query22: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query22.id, ok=True)


async def order_23(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 👒",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/kgJn7mF1/photo-4-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=60_000_00),
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 👒',
                           request_timeout=15
                           )


async def pre_checkout_query23(pre_checkout_query23: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query23.id, ok=True)


async def order_24(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 👒",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/pLctxndr/photo-5-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=60_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-14_999_99)
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 👒',
                           request_timeout=15
                           )


async def pre_checkout_query24(pre_checkout_query24: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query24.id, ok=True)


async def order_25(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Bosh kiyim 👒",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/tRdQJcgL/photo-6-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=60_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-14_999_99)
                           ],
                           start_parameter='time-machine-example',
                           payload='Bosh kiyim 👒',
                           request_timeout=15
                           )


async def pre_checkout_query25(pre_checkout_query25: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query25.id, ok=True)


#*************************************************************************************************************# noqa


async def order_26(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Ustki kiyim 👗",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/zB1KfvtZ/IMG-20240210-103302.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=250_000_00),
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-29_999_99)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki kiyim 👗',
                           request_timeout=15
                           )


async def pre_checkout_query26(pre_checkout_query26: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query26.id, ok=True)


async def order_27(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Ustki kiyim 👗",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/7ZwLb7DN/photo-1-2024-02-11-12-56-43.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=250_000_00),
                               LabeledPrice(label="QQS", amount=20_000_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki kiyim 👗',
                           request_timeout=15
                           )


async def pre_checkout_query27(pre_checkout_query27: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query27.id, ok=True)



async def order_28(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki kiyim 👗",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/brsJyR9C/IMG-20240210-103741.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=150_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki kiyim 👗',
                           request_timeout=15
                           )


async def pre_checkout_query28(pre_checkout_query28: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query28.id, ok=True)



async def order_29(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki kiyim 👗",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/m2T4yjH0/IMG-20240210-103924.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=385_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki kiyim 👗',
                           request_timeout=15
                           )


async def pre_checkout_query29(pre_checkout_query29: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query29.id, ok=True)



async def order_30(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Ustki kiyim 👗",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/bNYXtJXP/IMG-20240210-104334.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=360_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ustki kiyim 👗',
                           request_timeout=15
                           )


async def pre_checkout_query30(pre_checkout_query30: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query30.id, ok=True)


async def order_31(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim va yupkalar 👖",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/rmGbd6Qz/IMG-20240210-105514.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=130_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim va yupkalar 👖',
                           request_timeout=15
                           )


async def pre_checkout_query31(pre_checkout_query31: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query31.id, ok=True)


async def order_32(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim va yupkalar 👖",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/3NncBXMT/IMG-20240210-105718.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=50_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim va yupkalar 👖',
                           request_timeout=15
                           )


async def pre_checkout_query32(pre_checkout_query32: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query32.id, ok=True)



async def order_33(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Shim va yupkalar 👖",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/ryJ3MkDP/IMG-20240210-110024.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim va yupkalar 👖',
                           request_timeout=15
                           )


async def pre_checkout_query33(pre_checkout_query33: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query33.id, ok=True)



async def order_34(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Shim va yupkalar 👖",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/RF0yM29w/photo-2024-02-11-16-27-17.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=220_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim va yupkalar 👖',
                           request_timeout=15
                           )


async def pre_checkout_query34(pre_checkout_query34: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query34.id, ok=True)


async def order_35(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Shim va yupkalar 👖",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/JhZYgVwK/IMG-20240210-110344.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=80_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Shim va yupkalar 👖',
                           request_timeout=15
                           )


async def pre_checkout_query35(pre_checkout_query35: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query35.id, ok=True)



async def order_36(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 👠",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/QN04vJPL/IMG-20240210-110635.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=210_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 👠',
                           request_timeout=15
                           )


async def pre_checkout_query36(pre_checkout_query36: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query36.id, ok=True)


async def order_37(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 👠",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/mgMSZYdg/IMG-20240210-110705.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=210_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 👠',
                           request_timeout=15
                           )


async def pre_checkout_query37(pre_checkout_query37: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query37.id, ok=True)



async def order_38(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 👠",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/vmtLfQwR/IMG-20240210-110751.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=220_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 👠',
                           request_timeout=15
                           )


async def pre_checkout_query38(pre_checkout_query38: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query38.id, ok=True)



async def order_39(call: types.CallbackQuery, bot: Bot): # noqa
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 👠",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/nzVK16nX/IMG-20240210-110907.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=420_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 👠',
                           request_timeout=15
                           )


async def pre_checkout_query39(pre_checkout_query39: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query39.id, ok=True)


async def order_40(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Oyoq kiyim 👠",
                           description="Qiz bolalar uchun ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://i.postimg.cc/265vWhxv/IMG-20240210-111103.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=260_000_00),
                               LabeledPrice(label="QQS", amount=10_000_00),
                               LabeledPrice(label="Skidka", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Oyoq kiyim 👠',
                           request_timeout=15
                           )


async def pre_checkout_query40(pre_checkout_query40: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query40.id, ok=True)



async def successful_payment(message: types.Message, bot: Bot): # noqa
    msg = f"""
    Payment Done ✅ 
    Product name : {message.successful_payment.invoice_payload}
    Price: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg) # noqa