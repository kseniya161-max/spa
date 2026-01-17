
from celery import shared_task
import telegram
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = 6980147515

@shared_task
def send_habit_reminder(habit_name):
    bot = telegram.Bot(token=TOKEN)
    message = f"Напоминание: пора выполнить привычку '{habit_name}'!"
    bot.send_message(chat_id=CHAT_ID, text=message)
