import requests
import calendars as cal
import sys
import datetime as dt
import convert
import json
#generate
today = str(dt.date.today())
target_date = convert.converter(today)
date_to_convert = cal.Calendar().to_french_revolutionary(target_date)

#print(date_to_convert)

url = 'https://hooks.slack.com/services/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'
payload = {"text":date_to_convert}
data = json.dumps(payload)
requests.post(url,data)
print('success')