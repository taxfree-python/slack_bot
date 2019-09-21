from slackbot.bot import respond_to
import sys
sys.path.append('/Users/taxfree/python/slackbot/bot_function')
import today
import kawaii
import fizzbuzz
import weather

@respond_to('today')
def when_today(message):
    message.reply(today.when_today(today))

@respond_to('ok')
def status(message):
    message.reply("OK")

@respond_to('thank you')
def thank_you(message):
    message.reply('thank you, too!')

@respond_to('kawaii')
def kawaii_reply(message):
    message.reply(kawaii.kawaii(message))

@respond_to('fizzbuzz')
def fizzbuzz_reply(message):
    text = message.body['text']
    message.reply(fizzbuzz.fizzbuzz(text))

@respond_to('weather')
def weather_reply(message):
    message.reply(weather.tenki(message))