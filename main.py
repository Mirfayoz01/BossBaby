import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from config import TOKEN
from buttons import button, button_boy, button_girl, inlineBtn2
from inline_button import *
from images import *
from Payments import *


dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Salom Hurmatli {message.from_user.full_name} Mijoz BOSS BABY YANGIYOL BOTiga xush kelibsiz siz bizning dokondan ozingizga yoqgan kiyimlarni topishingiz mumkun. Tanlang (O'G'IL) yoki (QIZ)</b>", parse_mode=ParseMode.HTML, reply_markup=button) # noqa

    @dp.message(F.text == "O'g'il 🙍‍♂️")

    async def cmd_boy(message: types.Message): # noqa
        await message.answer("Bolalar kiyimlar ro'yhati", reply_markup=button_boy) # noqa

        @dp.message(F.text == "Bosh kiyim 🧢") # noqa
        async def cmd_bosh_kiyim(message: types.Message): # noqa
            for i in bosh_kiyim_boy:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 🧢 \nO'g'il bolalar uchun \nNarxi: 80,000 UZS</b>", reply_markup=inline_btn) # noqa
            for i in bosh_kiyim_boy2:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 🧢 \nO'g'il bolalar uchun \nNarxi: 120,000 UZS</b>", reply_markup=inline_btn2) # noqa
            for i in bosh_kiyim_boy3:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 🧢 \nO'g'il bolalar uchun \nNarxi: 120,000 UZS</b>", reply_markup=inline_btn3) # noqa
            for i in bosh_kiyim_boy4:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 🧢 \nO'g'il bolalar uchun \nNarxi: 60,000 UZS</b>", reply_markup=inline_btn4) # noqa
            for i in bosh_kiyim_boy5:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 🧢 \nO'g'il bolalar uchun \nNarxi: 60,000 UZS</b>", reply_markup=inline_btn5) # noqa
        @dp.message(F.text == "Ustki kiyim 👕") # noqa
        async def cmd_ustki_kiyim(message: types.Message): # noqa
            for i in ustki_kiyim_boy:
                await message.answer_photo(photo=i, caption="<b>Ustki Kiyim 👕 \nO'g'il bolalar uchun \nNarxi: 300,000 UZS</b>",reply_markup=inline_btn6) # noqa
            for i in ustki_kiyim_boy2:
                await message.answer_photo(photo=i, caption="<b>Ustki Kiyim 👕 \nO'g'il bolalar uchun \nNarxi: 450,000 UZS</b>",reply_markup=inline_btn7) # noqa
            for i in ustki_kiyim_boy3:
                await message.answer_photo(photo=i, caption="<b>Ustki Kiyim 👕 \nO'g'il bolalar uchun \nNarxi: 240,000 UZS</b>",reply_markup=inline_btn8) # noqa
            for i in ustki_kiyim_boy4:
                await message.answer_photo(photo=i, caption="<b>Ustki Kiyim 👕 \nO'g'il bolalar uchun \nNarxi: 260,000 UZS</b>",reply_markup=inline_btn9) # noqa
            for i in ustki_kiyim_boy5:
                await message.answer_photo(photo=i, caption="<b>Ustki Kiyim 👕 \nO'g'il bolalar uchun \nNarxi: 210,000 UZS</b>",reply_markup=inline_btn10) # noqa

        @dp.message(F.text == "Shim 👖") # noqa
        async def cmd_pastki_kiyim(message: types.Message): # noqa
            for i in Pastki_kiyim_boy:
                await message.answer_photo(photo=i, caption="<b>Shim 👖 \nO'g'il bolalar uchun \nNarxi: 160,000 UZS</b>",reply_markup=inline_btn11) # noqa
            for i in Pastki_kiyim_boy2:
                await message.answer_photo(photo=i, caption="<b>Shim 👖 \nO'g'il bolalar uchun \nNarxi: 110,000 UZS</b>",reply_markup=inline_btn12) # noqa
            for i in Pastki_kiyim_boy3:
                await message.answer_photo(photo=i, caption="<b>Shim 👖 \nO'g'il bolalar uchun \nNarxi: 200,000 UZS</b>",reply_markup=inline_btn13) # noqa
            for i in Pastki_kiyim_boy4:
                await message.answer_photo(photo=i, caption="<b>Shim 👖 \nO'g'il bolalar uchun \nNarxi: 160,000 UZS</b>",reply_markup=inline_btn14) # noqa
            for i in Pastki_kiyim_boy5:
                await message.answer_photo(photo=i, caption="<b>Shim 👖 \nO'g'il bolalar uchun \nNarxi: 140,000 UZS</b>",reply_markup=inline_btn15) # noqa

        @dp.message(F.text == "Oyoq kiyim 🥾") # noqa
        async def cmd_oyoq_kiyim(message: types.Message): # noqa
            for i in Oyoq_kiyimlar_boy:
                await message.answer_photo(photo=i, caption="<b>Oyoq kiyim 🥾 \nO'g'il bolalar uchun \nNarxi: 220,000 UZS</b>", reply_markup=inline_btn16) # noqa
            for i in Oyoq_kiyimlar_boy2:
                await message.answer_photo(photo=i, caption="<b>Oyoq kiyim 🥾 \nO'g'il bolalar uchun \nNarxi: 260,000 UZS</b>", reply_markup=inline_btn17) # noqa
            for i in Oyoq_kiyimlar_boy3:
                await message.answer_photo(photo=i, caption="<b>Oyoq kiyim 🥾 \nO'g'il bolalar uchun \nNarxi: 290,000 UZS</b>", reply_markup=inline_btn18) # noqa
            for i in Oyoq_kiyimlar_boy4:
                await message.answer_photo(photo=i, caption="<b>Oyoq kiyim 🥾 \nO'g'il bolalar uchun \nNarxi: 310,000 UZS</b>", reply_markup=inline_btn19) # noqa
            for i in Oyoq_kiyimlar_boy5:
                await message.answer_photo(photo=i, caption="<b>Oyoq kiyim 🥾 \nO'g'il bolalar uchun \nNarxi: 240,000 UZS</b>", reply_markup=inline_btn20) # noqa

        @dp.message(F.text == "🔙 Orqaga qaytish") # noqa
        async def cmd_orqaga_boy(message: types.Message): # noqa
            await message.answer("Orqaga qaytildi", reply_markup=button) # noqa
            await message.delete()

    @dp.message(F.text == "Qiz 🙍‍♀️")
    async def cmd_girl(message: types.Message): # noqa
        await message.answer("Qizlar kiyimlar ro'yhati", reply_markup=button_girl) # noqa

        @dp.message(F.text == "Bosh kiyim 👒") # noqa
        async def cmd_bosh_kiy_girl(message: types.Message): # noqa
            for i in bosh_kiyim_girl:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 👒 \nQiz bolalar uchun \nNarxi: 120,000 UZS</b>", reply_markup=inline_btn21) # noqa
            for i in bosh_kiyim_girl2:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 👒 \nQiz bolalar uchun \nNarxi: 80,000 UZS</b>", reply_markup=inline_btn22) # noqa
            for i in bosh_kiyim_girl3:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 👒 \nQiz bolalar uchun \nNarxi: 60,000 UZS</b>", reply_markup=inline_btn23) # noqa
            for i in bosh_kiyim_girl4:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 👒 \nQiz bolalar uchun \nNarxi: 60,000 UZS</b>", reply_markup=inline_btn24) # noqa
            for i in bosh_kiyim_girl5:
                await message.answer_photo(photo=i, caption="<b>Bosh kiyim 👒 \nQiz bolalar uchun \nNarxi: 60,000 UZS</b>", reply_markup=inline_btn25) # noqa

        @dp.message(F.text == "Ustki kiyim 👗") # noqa
        async def cmd_ustki_kiy_girl(message: types.Message): # noqa
            for i in ustki_kiyim_girl:
                await message.answer_photo(photo=i, caption="<b>Ustki kiyim 👗 \nQiz bolalar uchun \nNarxi: 250,000 UZS</b>", reply_markup=inline_btn26) # noqa
            for i in ustki_kiyim_girl2:
                await message.answer_photo(photo=i, caption="<b>Ustki kiyim 👗 \nQiz bolalar uchun \nNarxi: 250,000 UZS</b>", reply_markup=inline_btn27) # noqa
            for i in ustki_kiyim_girl3:
                await message.answer_photo(photo=i, caption="<b>Ustki kiyim 👗 \nQiz bolalar uchun \nNarxi: 150,000 UZS</b>", reply_markup=inline_btn28) # noqa
            for i in ustki_kiyim_girl4:
                await message.answer_photo(photo=i, caption="<b>Ustki kiyim 👗 \nQiz bolalar uchun \nNarxi: 385,000 UZS</b>", reply_markup=inline_btn29) # noqa
            for i in ustki_kiyim_girl5:
                await message.answer_photo(photo=i, caption="<b>Ustki kiyim 👗 \nQiz bolalar uchun \nNarxi: 360,000 UZS</b>", reply_markup=inline_btn30) # noqa

        @dp.message(F.text == "Shim va yupkalar 👗") # noqa
        async def cmd_pastki_kiy_girl(message: types.Message): # noqa
            for i in Pastki_kiyim_girl:
                await message.answer_photo(photo=i, caption="<b>Shim va yupkalar 👖 \nQiz bolalar uchun \nNarxi: 130,000 UZS</b>",reply_markup=inline_btn31) # noqa
            for i in Pastki_kiyim_girl2:
                await message.answer_photo(photo=i, caption="<b>Shim va yupkalar 👖 \nQiz bolalar uchun \nNarxi: 50,000 UZS</b>",reply_markup=inline_btn32) # noqa
            for i in Pastki_kiyim_girl3:
                await message.answer_photo(photo=i, caption="<b>Shim va yupkalar 👖 \nQiz bolalar uchun \nNarxi: 160,000 UZS</b>",reply_markup=inline_btn33) # noqa
            for i in Pastki_kiyim_girl4:
                await message.answer_photo(photo=i, caption="<b>Shim va yupkalar 👖 \nQiz bolalar uchun \nNarxi: 220,000 UZS</b>",reply_markup=inline_btn34) # noqa
            for i in Pastki_kiyim_girl5:
                await message.answer_photo(photo=i, caption="<b>Shim va yupkalar 👖 \nQiz bolalar uchun \nNarxi: 80,000 UZS</b>",reply_markup=inline_btn35) # noqa

        @dp.message(F.text == "Oyoq kiyim 👠") # noqa
        async def cmd_oyoq_kiy_girl(message: types.Message): # noqa
            for i in Oyoq_kiyimlar_girl:
                await message.answer_photo(photo=i, caption="<b>Oyoq Kiyim 👠 \nQiz bolalar uchun \nNarxi: 210,000 UZS</b>",reply_markup=inline_btn36) # noqa
            for i in Oyoq_kiyimlar_girl2:
                await message.answer_photo(photo=i, caption="<b>Oyoq Kiyim 👠 \nQiz bolalar uchun \nNarxi: 210,000 UZS</b>",reply_markup=inline_btn37) # noqa
            for i in Oyoq_kiyimlar_girl3:
                await message.answer_photo(photo=i, caption="<b>Oyoq Kiyim 👠 \nQiz bolalar uchun \nNarxi: 220,000 UZS</b>",reply_markup=inline_btn38) # noqa
            for i in Oyoq_kiyimlar_girl4:
                await message.answer_photo(photo=i, caption="<b>Oyoq Kiyim 👠 \nQiz bolalar uchun \nNarxi: 420,000 UZS</b>",reply_markup=inline_btn39) # noqa
            for i in Oyoq_kiyimlar_girl5:
                await message.answer_photo(photo=i, caption="<b>Oyoq Kiyim 👠 \nQiz bolalar uchun \nNarxi: 260,000 UZS</b>",reply_markup=inline_btn40) # noqa


        @dp.message(F.text == "🔙 Orqaga qaytish") # noqa
        async def cmd_orqaga_girl(message: types.Message): # noqa
            await message.answer("Orqaga qaytildi", reply_markup=button) # noqa
            await message.delete()



dp.callback_query.register(order_1, F.data == "inline") # noqa
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_2, F.data == "inline2") # noqa
dp.pre_checkout_query.register(pre_checkout_query2)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_3, F.data == "inline3") # noqa
dp.pre_checkout_query.register(pre_checkout_query3)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_4, F.data == "inline4") # noqa
dp.pre_checkout_query.register(pre_checkout_query4)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_5, F.data == "inline5") # noqa
dp.pre_checkout_query.register(pre_checkout_query5)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_6, F.data == "inline6") # noqa
dp.pre_checkout_query.register(pre_checkout_query6)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_7, F.data == "inline7") # noqa
dp.pre_checkout_query.register(pre_checkout_query7)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_8, F.data == "inline8") # noqa
dp.pre_checkout_query.register(pre_checkout_query8)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_9, F.data == "inline9") # noqa
dp.pre_checkout_query.register(pre_checkout_query9)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_10, F.data == "inline10") # noqa
dp.pre_checkout_query.register(pre_checkout_query10)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_11, F.data == "inline11") # noqa
dp.pre_checkout_query.register(pre_checkout_query11)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_12, F.data == "inline12") # noqa
dp.pre_checkout_query.register(pre_checkout_query12)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_13, F.data == "inline13") # noqa
dp.pre_checkout_query.register(pre_checkout_query13)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_14, F.data == "inline14") # noqa
dp.pre_checkout_query.register(pre_checkout_query14)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_15, F.data == "inline15") # noqa
dp.pre_checkout_query.register(pre_checkout_query15)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_16, F.data == "inline16") # noqa
dp.pre_checkout_query.register(pre_checkout_query16)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_17, F.data == "inline17") # noqa
dp.pre_checkout_query.register(pre_checkout_query17)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_18, F.data == "inline18") # noqa
dp.pre_checkout_query.register(pre_checkout_query18)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_19, F.data == "inline19") # noqa
dp.pre_checkout_query.register(pre_checkout_query19)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_20, F.data == "inline20") # noqa
dp.pre_checkout_query.register(pre_checkout_query20)
dp.message.register(successful_payment, F.successful_payment)


#******************************************************************************************# noqa
#********************************************BOLLAR TUGADI*********************************# noqa
#******************************************************************************************# noqa

#******************************************************************************************# noqa
#********************************************QIZLAR BOSHLANDI******************************# noqa
#******************************************************************************************# noqa



dp.callback_query.register(order_21, F.data == "inline21") # noqa
dp.pre_checkout_query.register(pre_checkout_query21)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_22, F.data == "inline22") # noqa
dp.pre_checkout_query.register(pre_checkout_query22)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_23, F.data == "inline23") # noqa
dp.pre_checkout_query.register(pre_checkout_query23)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_24, F.data == "inline24") # noqa
dp.pre_checkout_query.register(pre_checkout_query24)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_25, F.data == "inline25") # noqa
dp.pre_checkout_query.register(pre_checkout_query25)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_26, F.data == "inline26") # noqa
dp.pre_checkout_query.register(pre_checkout_query26)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_27, F.data == "inline27") # noqa
dp.pre_checkout_query.register(pre_checkout_query27)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_28, F.data == "inline28") # noqa
dp.pre_checkout_query.register(pre_checkout_query28)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_29, F.data == "inline29") # noqa
dp.pre_checkout_query.register(pre_checkout_query29)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_30, F.data == "inline30") # noqa
dp.pre_checkout_query.register(pre_checkout_query30)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_31, F.data == "inline31") # noqa
dp.pre_checkout_query.register(pre_checkout_query31)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_32, F.data == "inline32") # noqa
dp.pre_checkout_query.register(pre_checkout_query32)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_33, F.data == "inline33") # noqa
dp.pre_checkout_query.register(pre_checkout_query33)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_34, F.data == "inline34") # noqa
dp.pre_checkout_query.register(pre_checkout_query34)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_35, F.data == "inline35") # noqa
dp.pre_checkout_query.register(pre_checkout_query35)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_36, F.data == "inline36") # noqa
dp.pre_checkout_query.register(pre_checkout_query36)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_37, F.data == "inline37") # noqa
dp.pre_checkout_query.register(pre_checkout_query37)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_38, F.data == "inline38") # noqa
dp.pre_checkout_query.register(pre_checkout_query38)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_39, F.data == "inline39") # noqa
dp.pre_checkout_query.register(pre_checkout_query39)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_40, F.data == "inline40") # noqa
dp.pre_checkout_query.register(pre_checkout_query40)
dp.message.register(successful_payment, F.successful_payment)



async def main(): # noqa
    bot = Bot(token=TOKEN,parse_mode=ParseMode.HTML) # noqa
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="start", description="Bot ishga tushirish"), # noqa
        BotCommand(command="help", description="Yordam") # noqa
    ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
