#!/bin/bash

set -e

opkg update

/etc/init.d/lora-network-server stop

opkg install python-pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install AWSIoTPythonSDK
pip install boto3
pip install paho-mqtt

/etc/init.d/lora-network-server start