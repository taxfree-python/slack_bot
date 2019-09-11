import requests
import calendars as cal
import sys
import datetime as dt
import convert
import json
#generate
def calendar(message):
    today = str(dt.date.today())
    target_date = convert.converter(today)
    date_to_convert = cal.Calendar().to_french_revolutionary(target_date)
    return date_to_convert