import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def rego_track(update: Update, context):
    base_url = "https://indodax.com"
    coin_name = context.args[0]

    api_url = f"{base_url}/api/ticker/{coin_name}idr"

    response = requests.get(api_url)

    print(response.json().get("ticker").get("last"))

    price_data = response.json().get("ticker").get("last")

    update.message.reply_text(f'Regone Saiki {coin_name} yaiku {price_data} ')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1990212802:AAGBEfVl2qN6Ogr8CvkQDUV3Ya8tsZRDRqE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('rego', rego_track))

updater.start_polling()
updater.idle()