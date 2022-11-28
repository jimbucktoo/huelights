#!/usr/bin/python
from phue import Bridge
from time import sleep
import logging

logging.basicConfig()
bridge = Bridge('192.168.86.41')

#bridge.connect()

bridge.set_light(6, 'on', True)
sleep(5)
bridge.set_light(6, 'on', False)
