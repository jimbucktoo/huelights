# huelights

huelights is a Python application that uses Raspberry Pi 4 to control and automate Philips Hue Smart Lights on a local network.

## Technologies

* [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation in association with Broadcom.
* [Raspberry Pi OS](https://www.raspberrypi.com/software/) - Raspberry Pi OS is a Unix-like operating system based on the Debian Linux distribution for the Raspberry Pi family of compact single-board computers.
* [Python](https://www.python.org) - Python is a high-level, general-purpose programming language.
* [Nmap](https://nmap.org/) - Nmap is a network scanner used to discover hosts and services on a computer network by sending packets and analyzing the responses.
* [Phillips Hue API](https://developers.meethue.com/) - Philips Hue is a line of color-changing LED lamps and white bulbs which can be controlled wirelessly.

## Getting Started

#### To get started:

1. Install Raspberry Pi OS onto your Raspberry Pi with Raspberry Pi Imager - [Raspbian OS](https://www.raspberrypi.com/software/)
2. Configure network settings and connect to Wi-Fi - [Raspberry Pi Networking Documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking)
3. Enable SSH - [Raspberry Pi SSH Documentation](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)

## Setup

#### To setup:

1. Update and upgrade the system:
```
sudo apt update
sudo apt upgrade
```
2. Install Python package installer:
```
sudo apt install python3-pip
```
3. Install Nmap to find the IP address of Philips Hue Bridge:
```
sudo apt install nmap
```
4. Scan the local network to find the IP address of Philips Hue Bridge:
```
nmap -sP 192.168.86.0/24
```
*Change the IP address to match your personal network configuration*

The IP address should be located here in the output. Save this IP address as it will be utilized later:

<img src="https://github.com/jimbucktoo/huelights/blob/main/s1.png" width="500">

5. Install Phillips Hue Python library:
```
sudo pip install phue
```

## Authentication

Before using the Phillips Hue API, we need to retrieve an authentication token in order to access it.

#### To retrieve an authentication token:

1. Access the Philips Hue API using their request form at http://192.168.86.41/debug/clip.html

*Change the IP address to match your personal network configuration*

2. Create an authenticated user by filling the API field with "/api" and sending device type in the message body using this format: 
```
{"devicetype": "<Device_Name>"}
```
4. Press the link button on the center of the Philips Hue Bridge device.

5. Submit the form after waiting a few seconds. Receive and save the authentication token from the command response.
```
[
    {
        "success": {
            "username": "<Authentication_Token>"
        }
    }
]
```

<img src="https://github.com/jimbucktoo/huelights/blob/main/s2.png" width="500">

## Usage

Before writing Python scripts to control and automate the lighting system, test the Philips Hue API without code by using the request form to understand how to communicate with it.

#### To use the API:

Once authenticated, start manipulating the lights using the request form by turning the light on.

1. Retrieve the list of all lights by submitting a GET request to the Philips Hue API with the request URL:
```
/api/<Authentication_Token>/lights
```

<img src="https://github.com/jimbucktoo/huelights/blob/main/s3.png" width="500">

2. Select a light to manipulate by noting its code block number and using it to identify the light. For example, to turn on light number 6, use the request URL: 
```
/api/<Authentication_Token>/lights/6/state
```
3. Turn the light on, replace the message body with: {"on": true} and click the PUT button to update the status.
```
{"on": true}
```
4. Turn the light off, replace the message body with:
```
{"on": false}
```

## Scripting

To control and automate the Philips Hue Lighting System, you can utilize the Philips Hue API and Python library to interact with it dynamically through scripts.

#### To Turn On and Off the Light

To switch the light on and off, follow these steps:

1. Create a Python file for the script:
```
nano lightswitch.py
```
2. Copy and paste the following code inside, replacing the IP address and the light number with your own configuration:
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

If you encounter an error when running the script for the first time, you can fix it by following these steps:
- Uncomment the bridge.connect() line in the script and save it
- Press the link button on the Philips Hue Bridge device
- Run the script again

Note that this step only needs to be done once as the authentication will be cached for future use. After the first use, you can comment out the bridge.connect() line in the script.

3. Uncomment the bridge.connect() line, save the file, and run the script:
```
python3 lightswitch.py
```

## Output:

The light should turn on, stay lit for 5 seconds, and then turn off.

https://github.com/jimbucktoo/huelights/assets/25806014/af4d4c46-6fd6-436d-911b-c2b8aee3edcd

## Authors

* **James Liang** - *Initial work* - [jimbucktoo](https://github.com/jimbucktoo/)
