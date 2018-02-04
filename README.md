# Installing AWS IOT SDK for python on Multitech Conduit

Using Kinesis stream API on Conduit can be used to create a scalable LoRaWAN sensor Application network.
Kinesis streams can be scaled up for any number of producers and consumers.

## Update the package list to install pip and dependencies
`# opkg update`

If an error occurs update the mlinux feeds urls to 
`# vi /etc/opkg/mlinux-feed.conf`

See http://multitech.net/mlinux/feeds/ for a list of available versions
3.3.15 is currently the latest

mlinux-feed.conf example
———————————————————————————————————————
src/gz mlinux-all http://multitech.net/mlinux/feeds/3.3.15/all
src/gz mlinux-arm926ejste http://multitech.net/mlinux/feeds/3.3.15/arm926ejste
src/gz mlinux-mtcdt http://multitech.net/mlinux/feeds/3.3.15/mtcdt
———————————————————————————————————————

## Install mLinux python-pip package
`# opkg update
# opkg install python-pip`


## Upgrade to newer pip version
[Installing with get-pip.py](https://pip.pypa.io/en/stable/installing/)

`# wget https://bootstrap.pypa.io/get-pip.py
# python get-pip.py`


### SSL Warning
Successfully installed pip-9.0.1 setuptools-38.4.1 wheel-0.30.0
/tmp/tmpS5_Rwe/pip.zip/pip/_vendor/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.

mLinux 3.x does not support python with SSL
mLinux 4.x is needed for python with SSL

## Install AWS IoT SDK
[AWS IoT Python SDK](https://github.com/aws/aws-iot-device-sdk-python)

`# pip install AWSIoTPythonSDK
# sudo pip install awscli
# pip install boto3`

[Connect to your AWS back-end](https://us-west-2.console.aws.amazon.com/console/home)
[Kenesis](https://us-west-2.console.aws.amazon.com/kinesis/home)
[Kenesis Getting Started](https://aws.amazon.com/kinesis/getting-started/)
[Stream Setup](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)
[Setup IAM role for Conduit access to kinesis stream](https://console.aws.amazon.com/iam/)
[Boto library](https://github.com/boto/boto)
[Boto Reference](http://boto3.readthedocs.io/en/latest/reference/services/iot.html)


## Create Kinesis Stream

Stream name LoRaWAN will need to be defined for the producer application on Conduit to forward received packets

## Copy Stream IAM Credentials to the Conduit

/home/root/.aws/credentials file can be created to authenticate the Conduit sensor posts

## Producer Application

The provided application can be run on the Conduit. It subcribes via MQTT for LoRaWAN uplinks and forwards them to the LoRaWAN Kenisis stream.

Install boto_producer.py by copying the file to the Conduit file system
`scp boto_producer.py admin@192.168.2.1:`


Run 
`python boto_producer.py`


## Consumer Application

The provided consumer application will poll the kenisis stream for packets forwarded from the Conduit gateways.

Run 
`python boto_consumer.py`



## Installation of AWS CLI on Linux

[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html)

