"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""

from datetime import date
import logging

import ephem
from telegram import Update
from telegram.ext import (
    filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
    )

from secret_tokens import SECRET_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='8_ephem_bot.log',
    level=logging.INFO
)

secret_token = SECRET_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_chat.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello, {user_name}. I'm a bot, please talk to me!",
        )


async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
        )


async def planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    planets = {
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus,
        'Mars': ephem.Mars,
        'Jupiter': ephem.Jupiter,
        'Saturn': ephem.Saturn,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
        'Pluto': ephem.Pluto,
    }
    if update.message.text.split()[-1] in planets:
        planet_name = planets.get(update.message.text.split()[-1])
        planet = planet_name(date.today())
        constellation = ephem.constellation(planet)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=constellation
            )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Невозможно определить текущее созвездие для этой планеты'
            )


def main():
    application = ApplicationBuilder().token(secret_token).build()

    start_handler = CommandHandler('start', start)
    talk_to_me_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND), talk_to_me
        )
    planet_handler = CommandHandler('planet', planet)

    application.add_handler(start_handler)
    application.add_handler(talk_to_me_handler)
    application.add_handler(planet_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
