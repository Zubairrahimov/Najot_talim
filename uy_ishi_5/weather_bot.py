import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TELEGRAM_BOT_TOKEN = '6054349441:AAFgiuGOxGJIKmPb4ZeX8bACM-nyIjWqRho'
#ogre13bot

OPENWEATHERMAP_API_KEY = 'bd5e378503939ddaee76f12ad7a97608'


WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'
FORECAST_API_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}! I am your weather bot. Send me any location, and I'll show you the weather.")


def get_weather_data(location, api_url):
    params = {
        'q': location,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric',  # You can change to 'imperial' for Fahrenheit
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    return None


def weather(update: Update, context: CallbackContext) -> None:
    location = ' '.join(context.args)
    if not location:
        update.message.reply_text("Please provide a location. Use /weather <location>.")
        return


    current_data = get_weather_data(location, WEATHER_API_URL)
    if current_data:
        weather_info = f"Weather in {current_data['name']}: {current_data['weather'][0]['description']}\n"
        temperature = f"Temperature: {current_data['main']['temp']}°C\n"
        humidity = f"Humidity: {current_data['main']['humidity']}%\n"
        wind_speed = f"Wind Speed: {current_data['wind']['speed']} m/s\n"
        update.message.reply_text(weather_info + temperature + humidity + wind_speed)
    else:
        update.message.reply_text("Sorry, I couldn't fetch the current weather data for that location. Please try again later.")


def daily_weather(update: Update, context: CallbackContext) -> None:
    location = ' '.join(context.args)
    if not location:
        update.message.reply_text("Please provide a location. Use /daily <location>.")
        return

    forecast_data = get_weather_data(location, FORECAST_API_URL)
    if forecast_data:
        daily_forecast = forecast_data.get('list', [])
        if daily_forecast:
            response = "Daily Weather Forecast:\n"
            for forecast in daily_forecast:
                date = forecast['dt_txt']
                temperature = f"Temperature: {forecast['main']['temp']}°C"
                weather_description = forecast['weather'][0]['description']
                response += f"\n{date}: {weather_description}, {temperature}"
            update.message.reply_text(response)
        else:
            update.message.reply_text("Sorry, I couldn't fetch the daily weather forecast for that location. Please try again later.")
    else:
        update.message.reply_text("Sorry, I couldn't fetch the weather data for that location. Please try again later.")

def weekly_weather(update: Update, context: CallbackContext) -> None:
    # topomadim
    pass

def ten_days_weather(update: Update, context: CallbackContext) -> None:
    pass

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I don't understand that command. Use /weather <location> to get the current weather or use /daily, /weekly, or /10days for different forecasts.")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("weather", weather))
    dispatcher.add_handler(CommandHandler("daily", daily_weather))
    dispatcher.add_handler(CommandHandler("weekly", weekly_weather))
    dispatcher.add_handler(CommandHandler("10days", ten_days_weather))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
