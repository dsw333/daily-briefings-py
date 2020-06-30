# app/daily_briefing.py

import os
from dotenv import load_dotenv
from datetime import date
#from print import pprint

from app import APP_ENV
from app.weather_service import get_hourly_forecasts
from app.sms_service import send_sms

load_dotenv()


#If weather is greater than 75% then send a text message that you need sunblock


if 'my_temperature_f' > 75:
    send_sms(print("Put on sunscreen"))




