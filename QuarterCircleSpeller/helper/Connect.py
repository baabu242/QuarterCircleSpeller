import requests


def egi_connect(val):
    if val == 0:
        x = requests.get("http://10.14.76.136:8080/start")
    elif val == 1:
        x = requests.get("http://10.14.76.136:8080/startrec")
    elif val == 2:
        x = requests.get('http://10.14.76.136:8080/stoprec')
    elif val == 3:
        x = requests.get('http://10.14.76.136:8080/stop')
    else:
        x = requests.get('http://10.14.76.136:8080/send?event_type=' + val)
    print(x.content)