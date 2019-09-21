import requests
import json
base_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
params = {'city':'471010'}  #default = 那覇
def tenki(message):
    a = message
    response = requests.get(base_url,params)
    json_data = json.loads(response.content)
    json_city = json_data['location']['city']
    json_date     = json_data['forecasts'][0]['image']['title']

    for forecast in json_data['forecasts']:
        date = forecast['date']
        dateLabel = forecast['dateLabel'].encode('utf-8')
        print('{0} ({1})'.format(date, dateLabel))
        telop = forecast['telop'].encode('utf-8')
        t_max = forecast['temperature'].get('max')
        t_min = forecast['temperature'].get('min')
        if t_max is not None and t_min is not None:
            t_max = '{0}℃'.format(t_max['celsius'])
            t_min = '{0}℃'.format(t_min['celsius'])

    if t_max == None and t_min == None:
        return_data = (f'state:{json_date} location:{json_city}')
    elif t_max == None:
        return_data = (f'state:{json_date} location:{json_city} min_temp:{t_min}')
    elif t_min == None:
        return_data = (f'state:{json_date} location:{json_city} max_temp:{t_max}')
    else:
        return_data = (f'state{json_date} location:{json_city} max_temp:{t_max} min_temp:{t_min}')
    return return_data