from loader import session
from config import api_key

# фу-ия для получения погодв
# принимает на вход параметры (долгота & широта)
# возвращает обьект погода
async def get_weather(lat: int, lon: int):
    params = {
        'lat': lat,
        'lon': lon,
        'lang': 'ru_RU',
        'extra': 'true'
    }
    headers = {'X-Yandex-API-Key': api_key}
    async with session.get(
            f'https://api.weather.yandex.ru/v2/forecast',
            params=params,
            headers=headers
    ) as response:
        return await response.json()
