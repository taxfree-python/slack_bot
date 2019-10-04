from slackbot.bot import respond_to
import sys
sys.path.append('/slackbot/Python_Calendar_Converter')
sys.path.append('/slackbot/bot_function')
import generater

@respond_to('revolutionary')
def calendar(message):
    message.reply(generater.calendar(message))