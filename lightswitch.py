#!/usr/bin/python
from phue import Bridge
from time import sleep
import logging

logging.basicConfig()
b = Bridge('192.168.86.41')

#b.connect()

b.set_light(6, 'on', True)
sleep(5)
b.set_light(6, 'on', False)
