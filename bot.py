from aiogram.dispatcher.filters import Command

import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from db import BotDB
BotDB = BotDB('bd.db')

"""Все что с logging - для получения разной информации в терминал"""
logging.basicConfig(level=logging.INFO)

"""Подключение бота"""
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

"""Создание клавиш"""
"""НАЧАЛО ВСЕХ КЛАВИШШШ"""
"""Простая клавиатура с существующими командами"""
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("/start")
button2 = KeyboardButton('/рецепты')
keyboard.add(button1).add(button2)


rev = InlineKeyboardMarkup(row_width=1)
item1 = KeyboardButton(text="Хочу оставить коментарий", callback_data="octav")
item2 = KeyboardButton(text="Хочу посмотреть отзывы", callback_data="posm")
item3 = KeyboardButton(text="нет, ничего не хочу", callback_data="net")

rev.add(item1).add(item2).add(item3)

kakou1 = InlineKeyboardMarkup(row_width=5)
octav1 = KeyboardButton(text="1⃣", callback_data="oct1")
octav2 = KeyboardButton(text="2⃣", callback_data="oct2")
octav3 = KeyboardButton(text="3⃣", callback_data="oct3")
octav4 = KeyboardButton(text="4⃣", callback_data="oct4")
octav5 = KeyboardButton(text="5⃣", callback_data="oct5")
kakou1.add(octav1, octav2, octav3, octav4, octav5)

kakou2 = InlineKeyboardMarkup(row_width=5)
prosm1 = KeyboardButton(text="1⃣", callback_data="pos1")
prosm2 = KeyboardButton(text="2⃣", callback_data="pos2")
prosm3 = KeyboardButton(text="3⃣", callback_data="pos3")
prosm4 = KeyboardButton(text="4⃣", callback_data="pos4")
prosm5 = KeyboardButton(text="5⃣", callback_data="pos5")
kakou2.add(prosm1, prosm2, prosm3, prosm4, prosm5)

rec = InlineKeyboardMarkup(row_width=1)
pel = InlineKeyboardButton(text="Пельмени", callback_data="pelmen")
mak = InlineKeyboardButton(text="Макароны", callback_data="makaron")
rec.add(pel).add(mak)

"""КОНЕЦ ВСЕХ КЛАВИШШШ"""


@dp.message_handler(Command("start"))
async def hello(message: types.Message):
    """Ответ на /start"""
    await message.answer(text="Привет, я Бот-повар\nЯ создан для того, чтобы помочь тебе найти простые рецепты, кроме доширака",
                         reply_markup=keyboard)

@dp.message_handler(Command("рецепты"))
async def show_recept(message: types.Message):
    """Ответ на /рецепты"""
    await message.answer(text="У нас представлены некоторые рецепты. \n"
                         "Выберете, что у вас есть в холодильнике", reply_markup=rec)

@dp.callback_query_handler(text="pelmen")
async def rec_pelm(call: CallbackQuery):
    """Обработка инлайновой кнопки у которой call_back=pelmen"""
    await call.answer(cache_time=60)
    calll = call.data
    logging.info(f"call = {calll}")

    records = BotDB.get_recipe(calll)

    records = BotDB.get_recipe(calll)

    """Вывод рецептов"""
    if (len(records) != 0):
        await call.message.answer("Мы нашли для вас вот такие рецепты:")
        for i in range(len(records)):
            x = records[i]
            print(records[i][3])
            print(x[3])
            await call.message.answer(records[i][3])
            i += 1
        await call.message.answer(text="Это наши 5 лучших рецептов\n" "хотите посмотреть отзывы или оставить свой "
                                       "какому-нибудь рецепту?", reply_markup=rev)
    else:
        await call.message.answer("У нас пока нет рецптов с пельменями. Дождитесь обновления. \n""Спасибо за понимание")

    @dp.callback_query_handler(text="net")
    async def rev_net(call: CallbackQuery):
        """Обработка ответа, если человек не хочет ни смотреть отзывы, ни писать свой"""
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer("Буду рад тебя еще встретить🥺😄")

    @dp.callback_query_handler(text="octav")
    async def rev_ost(call: CallbackQuery):
        """если человек хочет написать отзыв"""
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer(text="К какому рецепту вы хотите оставить коментарий?", reply_markup=kakou1)

        @dp.callback_query_handler(text="oct1")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к первому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[0][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


        @dp.callback_query_handler(text="oct2")
        async def rev_ost(call: CallbackQuery):
            """Отзыв ко второму рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[1][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


        @dp.callback_query_handler(text="oct3")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к третьему рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[2][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


        @dp.callback_query_handler(text="oct4")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к четвертому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[3][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")

        @dp.callback_query_handler(text="oct5")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к пятому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[4][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


    @dp.callback_query_handler(text="posm")
    async def rev_pos(call: CallbackQuery):
        """Недоделанный кусок для вывода отзывов для того или иного рецепты"""
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer("Извините, не допилил(( Ждите обновлений!")
        """await call.message.answer(text="К какому рецепту вы хотите посмотреть коментарии?", reply_markup=kakou2)

        @dp.callback_query_handler(text="pos1")
        async def rev_pos(call: CallbackQuery):
            await call.answer(cache_time=60)
            calll = call.data
            logging.info(f"call = {calll}")

            await call.message.answer("Извините, не допилил(( Ждите обновлений!")
            call.message.answer(text="К какому рецепту вы хотите посмотреть коментарии?", reply_markup=kakou2)"""


@dp.callback_query_handler(text="makaron")
async def rec_mak(call: CallbackQuery):
    """Обработка инлайновой кнопки у которой call_back=makaron"""
    await call.answer(cache_time=60)
    calll = call.data
    logging.info(f"call = {calll}")

    records = BotDB.get_recipe(calll)
    """Вывод рецептов"""
    if (len(records) != 0):
        await call.message.answer("Мы нашли для вас вот такие рецепты:")
        for i in range(len(records)):
            x = records[i]
            print(records[i][3])
            print(x[3])
            await call.message.answer(records[i][3])
            i += 1
        await call.message.answer(text="Это наши 5 лучших рецептов\n" "хотите посмотреть отзывы или оставить свой "
                                       "какому-нибудь рецепту?", reply_markup=rev)
    else:
        await call.message.answer("У нас пока нет рецптов с макаронами. Дождитесь обновления. \n""Спасибо за понимание")

    @dp.callback_query_handler(text="net")
    async def rev_net(call: CallbackQuery):
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer("Буду рад тебя еще встретить🥺😄")

    @dp.callback_query_handler(text="octav")
    async def rev_ost(call: CallbackQuery):
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer(text="К какому рецепту вы хотите оставить коментарий?", reply_markup=kakou1)

        @dp.callback_query_handler(text="oct1")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к первому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):

                x = message.text
                y = records[0][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


        @dp.callback_query_handler(text="oct2")
        async def rev_ost(call: CallbackQuery):
            """Отзыв ко второму рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[1][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")


        @dp.callback_query_handler(text="oct3")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к третьем рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[2][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")

        @dp.callback_query_handler(text="oct4")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к четвертому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[3][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")

        @dp.callback_query_handler(text="oct5")
        async def rev_ost(call: CallbackQuery):
            """Отзыв к пятому рецепту"""
            await call.answer(cache_time=60)
            callback = call.data
            logging.info(f"call = {callback}")

            await call.message.answer("Введите свой отзыв")

            @dp.message_handler()
            async def obrab(message: types.Message):
                x = message.text
                y = records[4][1]
                print(x, '   ', y)
                BotDB.add_record(y, x)
                await message.answer("Спасибо за отзыв")

    @dp.callback_query_handler(text="posm")
    async def rev_pos(call: CallbackQuery):
        """Недоделанный кусок для вывода отзывов для того или иного рецепты"""
        await call.answer(cache_time=60)
        calll = call.data
        logging.info(f"call = {calll}")

        await call.message.answer("Извините, не допилил(( Ждите обновлений!")
        """await call.message.answer(text="К какому рецепту вы хотите посмотреть коментарии?", reply_markup=kakou2)

        @dp.callback_query_handler(text="pos1")
        async def rev_pos(call: CallbackQuery):
            await call.answer(cache_time=60)
            calll = call.data
            logging.info(f"call = {calll}")

            await call.message.answer("Извините, не допилил(( Ждите обновлений!")
            call.message.answer(text="К какому рецепту вы хотите посмотреть коментарии?", reply_markup=kakou2)"""


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)