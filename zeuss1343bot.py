from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
import schedule
import time

bot_configuration = BotConfiguration(
    name='ZeUsSbot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='50ada4c8d5a7dfc4-5f7e895c55ff7ad2-72eb5a69893a34a8'
)

viber = Api(bot_configuration)

def send_message():
    message = TextMessage(text='Your message')
    viber.send_messages('receiver_user_id', [message])

# Schedule message to be sent at specific time
schedule.every().day.at("08:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
