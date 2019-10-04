from slackbot.bot import respond_to
import sys
sys.path.append('/Users/taxfree/python/slackbot/Python_Calendar_Converter')
#print(sys.path)
#from memory_profiler import profile #メモリの使用枠を確認するライブラリ
import generater

#profile #メモリの使用枠を確認
@respond_to('revolutionary')
def calendar(message):
    message.reply(generater.calendar(message))