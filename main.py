import random
import telebot
from smm import Api

# Replace with your actual keys
SMM_API_KEY = 'YOUR_API_SMM_KEY'
TG_API_TOKEN = 'YOUR_TOKEN_FROM_BOTFATHER_FOR_A_TELEGRAM_BOT'

# List of allowed user_ids
allowed_user_ids = [4637428634, 234234221]  # Replace with your user_ids
# *** You can find your userid via bots like @getmyid etc...


bot = telebot.TeleBot(TG_API_TOKEN)
smm_api = Api(SMM_API_KEY)
links = []

def is_allowed(user_id):
    return user_id in allowed_user_ids

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if not is_allowed(message.from_user.id):
        bot.reply_to(message, "You do not have access to this bot")
        return
    bot.reply_to(message, "Hi. Send me a link to the promoted site or social network, I can suggest promotion methods for you.\n\nThis bot is available in the Github repository - https://github.com/fpoweredd/tg-smm-api\nContact: @westfresh")

@bot.message_handler(func=lambda message: 'http' in message.text)
def process_link(message):
    if not is_allowed(message.from_user.id):
        bot.reply_to(message, "You do not have access to this bot")
        return
    links.append(message.text.strip())
    options = [
        "1) Instagram - 1000000 views + 7000 likes :: 20.05 $",
        "2) Instagram - 500 followers :: ~0.5 $",
        "3) Web - 3000 views :: ~1.3 $",
        "4) TikTok - 1000000 views + likes :: ~100.00 $",
        "5) Facebook - 100 friends :: ~123.45 $",
    ]
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for option in options:
        keyboard.add(telebot.types.KeyboardButton(option))
    bot.reply_to(message, "Choose your promotion kit", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in [
        "1) Instagram - 1000000 views + 7000 likes :: 20.05 $",
        "2) Instagram - 500 followers :: ~0.5 $",
        "3) Web - 3000 views :: ~1.3 $",
        "4) TikTok - 1000000 views + likes :: ~100.00 $",
        "5) Facebook - 100 friends :: ~123.45 $",
])
def process_option(message):
    if not is_allowed(message.from_user.id):
        bot.reply_to(message, "You do not have access to this bot")
        return
    if not links:
        bot.reply_to(message, "Firstable, send a link")
        return

    link = links.pop(0)
    option = message.text
    
    # EXAMPLES, SWITCH TO YOUR SERVICESID AND ANYTHING

    if "1) " in option:
        smm_api.order({'service': 1234, 'link': link, 'quantity': 1000000})
        smm_api.order({'service': 1235, 'link': link, 'quantity': 7000})
    elif "2) " in option:
        smm_api.order({'service': 4321, 'link': link, 'quantity': 500})
    elif "3) " in option:
        smm_api.order({'service': 5555, 'link': link, 'quantity': 3000})
    elif "4) " in option:
        smm_api.order({'service': 3333, 'link': link, 'quantity': 1000000}) # views
        smm_api.order({'service': 1111, 'link': link, 'quantity': random.randint(3000, 30000)}) #random likes
    elif "5) " in option:
        smm_api.order({'service': 125, 'link': link, 'quantity': 100})
        
    # ---------------------------------------------------

    bot.reply_to(message, f'{option} ordered.\n\nYour Balance: {smm_api.balance()}')

bot.polling()