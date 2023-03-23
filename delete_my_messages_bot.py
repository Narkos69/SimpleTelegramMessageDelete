import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext





# Remplacez YOUR_API_KEY par l'API key de votre bot
API_KEY = "YOUR API KEY"
# Remplacez YOUR_USER_ID par votre identifiant d'utilisateur Telegram (UserID)
YOUR_USER_ID = YOUR USERID

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def delete_my_message(update: Update, context: CallbackContext):
    if update.message.chat.type in ["group", "supergroup"]:
        if update.message.from_user.id == YOUR_USER_ID:
            try:
                message_id = update.message.message_id
                context.bot.delete_message(chat_id=update.message.chat_id, message_id=message_id)
            except Exception as e:
                logging.error(f"Error while deleting message: {e}")

def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    # Ajoutez le gestionnaire de messages pour supprimer uniquement vos messages
    dp.add_handler(MessageHandler(Filters.all, delete_my_message))

    # Lance le bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
