# huelights

ITEC 320 - Project 3

huelights is a Python application utilizing the Raspberry Pi 4 to control and automate the Philips Hue Smart Lights within a local area network.

## Technologies

* [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation in association with Broadcom.
* [Raspberry Pi OS](https://www.raspberrypi.com/software/) - Raspberry Pi OS is a Unix-like operating system based on the Debian Linux distribution for the Raspberry Pi family of compact single-board computers.
* [Python](https://www.python.org) - Python is a high-level, general-purpose programming language.
* [Nmap](https://nmap.org/) - Nmap is a network scanner used to discover hosts and services on a computer network by sending packets and analyzing the responses.
* [Phillips Hue API](https://developers.meethue.com/) - Philips Hue is a line of color-changing LED lamps and white bulbs which can be controlled wirelessly.

## Getting Started

1. Install the Raspberry Pi OS on your Raspberry Pi utilizing the Raspberry Pi Imager - [Raspbian OS](https://www.raspberrypi.com/software/)
2. Configure the Raspberry Pi's network settings and connect it to Wifi - [Raspberry Pi Networking Documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking)
3. Enable SSH - [Raspberry Pi SSH Documentation](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)

## Setup

1. First, we will update the system to ensure that everything will work properly:
```
sudo apt update
sudo apt upgrade
```

2. Next, we will install the Python package installer so we can install our Python dependencies later:
```
sudo apt install python3-pip
```

3. Then, we need to find the IP address of the Philips Hue Bridge. We can accomplish this by installing Nmap, which is a network scanner that allows us to find hosts and services on a computer network:
```
sudo apt install nmap
```

4. After installing Nmap, we will utilize the program to scan our local area network until we find the IP address of the Philips Hue Bridge:
```
nmap -sP 192.168.86.0/24
```
*Change the IP address to match your personal network configuration*

The IP address should be located here in the output. Save this IP address as it will be utilized later:

<img src="https://github.com/jimbucktoo/huelights/blob/main/s1.png" width="500">

5. Finally,  we will install the Phillips Hue Python library so that we can interact with the Philips Hue API:
```
sudo pip install phue
```

## Authentication

Before writing Python scripts to control and automate the lighting system, we can first test the Philips Hue API without code so we can understand how to communicate with it.

1. Philips Hue provides a request form to test their API. Navigate to this form at http://192.168.86.41/debug/clip.html
*Change the IP address to match your personal network configuration*

2. In order to access that API, first we must create a authenticated user. To create an authenticated user, we should fill the request form API field with:
```
/api
```

3. Next, in the message body, we must send the device type (device name of your choice) utilizing this format:
```
{"devicetype":"<Device_Name>"}
```

4. Next, press the link button on the center of your Philips Hue Bridge device.

5. Within the next few seconds, submit the form by pressing the POST button under the URL section. You should receive a command response including the authentication token:
```
[
	{
		"success": {
			"username": "<Authentication_Token>"
		}
	}
]
```
Save this token as it will be utilized in later requests:

<img src="https://github.com/jimbucktoo/huelights/blob/main/s2.png" width="500">

## Operation

Now that we are properly authenticated, we can begin utilizing the request form to manipulate our lights. Let's start by turning the light on.

1. In order to do so, we must first retrieve a list of all the lights. We can do this by clicking the GET button under the URL section to submit a GET request to the Philips Hue API by replacing the request URL with:
```
/api/<Authentication_Token>/lights
```
Each code block in the list, returned as JSON output, begins with the light number. This light number will be utilized to identify which light we wish to manipulate. In the following examples, we will use light number 6:

2. To turn a light on, replace the request URL with:
```
/api/<Authentication_Token>/lights/6/state
```

3. Then, replace the message body with:
```
{"on":true}
```

4. Finally, click the PUT button under the URL section to submit and update the Philips Hue light status. By now, you should notice that the light has been turned on.

5. To turn off the light, simply switch the value in the message body from "true" to "false":
```
{"on":false}
```

## Scripting

While we can access the Philips Hue API with the request form, we can also interact with it dynamically by writing scripts to utilize the API through the Philips Hue Python library as well.

To demonstrate this, we will create a Python script to swtich on and off the light:

1. Open your Command Prompt/Terminal and create a Python text file for the script:
```
nano lightswitch.py
```

2. Copy and paste the following code inside. Replace the first argument of the set_light method with the light number you wish to manipulate. In this example, we will be utilizing light number 6.
```
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
```
*Change the IP address to match your personal network configuration*

You may run into an error the first time you run this because the script needs to create an authorization token similar to what we did using the request form earlier. To fix this:
- Uncomment the bridge.connect() line and save the file
- Press the link button in the center of the Philips Hue Bridge device
- Run the script

*This only needs to be done the first time as the authentication will be cached for future utilization. For subsequent usage, the bridge.connect() line can be negated*

3. Save the file and run the script. The light should turn on, stay on for 5 seconds, and then turn off:
```
python3 lightswitch.py
```

## Authors

* **James Liang** - *Initial work* - [jimbucktoo](https://github.com/jimbucktoo/)
