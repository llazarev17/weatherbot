import os
from dotenv import load_dotenv

load_dotenv()  # загружает переменные окружеиня из .dotenv файла
token = os.getenv('BOT_TOKEN')  # токен бота
api_key = os.getenv('API_KEY')  # API key от Yandex weather API
