import requests,pprint

pp = pprint.PrettyPrinter(indent=4)

def slack_message(data):
    url = 'secretURL.com'
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % data

    slack_resp = requests.post(url, headers=header, data=data)
    print(slack_resp)
    return slack_resp

def weather_status():
    do_url = ''
    do_resp = requests.get(do_url)
    do_status = do_resp.json()
# try:
#     do_status['current_weather']['weathercode'] == 80 :
#     temperature = do_status ['current_weather']['temperature']
#     time = do_status ['current_weather']['time']
#     # else:
#     #     temperature = do_status ['current_weather']['temperature']
#     #     time = do_status ['current_weather']['time']
# except:
#     print(temperature)
#     slack_message(data="Something went wrong")
    

    
#     return temperature,time

pp.pprint(weather_status)