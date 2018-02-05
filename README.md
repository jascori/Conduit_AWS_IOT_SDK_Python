# Installing AWS IOT SDK for python on Multitech Conduit

Using Kinesis stream API on Conduit can be used to create a scalable LoRaWAN sensor Application network.
Kinesis streams can be scaled up for any number of producers and consumers.

## Architecture

![Architecture Image](https://github.com/jascori/Conduit_AWS_IOT_SDK_Python/raw/master/AWS-Kinesis-Conduit.png)

## Overview

1. Install application dependencies on Conduit
	1. Update mLinux packages
	2. Install pip v1.3.1 and dependencies from mLinux packages
	3. Upgrade to pip v9.0.1
	4. Install AWS SDK and boto3 libraries for python
	5. Copy MQTT to AWS Kinesis producer application
2. Install application dependencies on Server
	1. Install to pip v9.0.1
	2. Install AWS SDK, AWS CLI and boto3 for python
	3. Copy MQTT to AWS Kinesis consumer application
3. Configure Kinesis stream on AWS
	1. Create Kinesis stream
	2. Create IAM credentials 
	3. Copy AWS IAM Credentials	to Conduit and Server
4. Start consumer and producer applications
5. Connect LoRaWAN sensor and send packets to Conduit

## References

[Connect to your AWS back-end](https://us-west-2.console.aws.amazon.com/console/home)
[Kenesis](https://us-west-2.console.aws.amazon.com/kinesis/home)
[Kenesis Getting Started](https://aws.amazon.com/kinesis/getting-started/)
[Stream Setup](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)
[Setup IAM role for Conduit access to kinesis stream](https://console.aws.amazon.com/iam/)
[Boto library](https://github.com/boto/boto)
[Boto Reference](http://boto3.readthedocs.io/en/latest/reference/services/iot.html)
[Installing with get-pip.py](https://pip.pypa.io/en/stable/installing/)
[AWS IoT Python SDK](https://github.com/aws/aws-iot-device-sdk-python)
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html)


## 1. Install application dependencies on Conduit

### i. Update mLinux packages

#### Update the package list to install pip and dependencies
`admin@mtcdt# opkg update`

If an error occurs update the mlinux feeds urls to 
`admin@mtcdt# vi /etc/opkg/mlinux-feed.conf`

See http://multitech.net/mlinux/feeds/ for a list of available versions
3.3.15 is currently the latest

```
   mlinux-feed.conf example
   ———————————————————————————————————————
   src/gz mlinux-all http://multitech.net/mlinux/feeds/3.3.15/all
   src/gz mlinux-arm926ejste http://multitech.net/mlinux/feeds/3.3.15/arm926ejste
   src/gz mlinux-mtcdt http://multitech.net/mlinux/feeds/3.3.15/mtcdt
   ———————————————————————————————————————
```

### ii. Install mLinux python-pip package
```
admin@mtcdt# opkg update
admin@mtcdt# opkg install python-pip
```


### iii. Upgrade to newer pip version
[Installing with get-pip.py](https://pip.pypa.io/en/stable/installing/)

```
admin@mtcdt# wget https://bootstrap.pypa.io/get-pip.py
admin@mtcdt# python get-pip.py`
```

#### SSL Warning
Successfully installed pip-9.0.1 setuptools-38.4.1 wheel-0.30.0
/tmp/tmpS5_Rwe/pip.zip/pip/_vendor/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.

mLinux 3.x does not support python with SSL
mLinux 4.x is needed for python with SSL

### iv. Install AWS IoT SDK and boto3 libraries
[AWS IoT Python SDK](https://github.com/aws/aws-iot-device-sdk-python)

```
admin@mtcdt# pip install AWSIoTPythonSDK
admin@mtcdt# pip install boto3
```


### v. Copy Producer Application to Conduit

The provided application can be run on the Conduit. It subcribes via MQTT for LoRaWAN uplinks and forwards them to the LoRaWAN Kenisis stream.

Install boto_producer.py by copying the file to the Conduit file system
```
linux$ scp boto_producer.py admin@192.168.2.1:
```


Run with
```
admin@mtcdt# python boto_producer.py
```


## 2. Install application dependencies on Server


### i. Install pip v9.0.1
[Installing with get-pip.py](https://pip.pypa.io/en/stable/installing/)

```
linux$ wget https://bootstrap.pypa.io/get-pip.py
linux$ python get-pip.py`
```


### ii. Install AWS IoT SDK/CLI and boto3 libraries
[AWS IoT Python SDK](https://github.com/aws/aws-iot-device-sdk-python)
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html)


```
linux$ pip install AWSIoTPythonSDK
linux$ sudo pip install awscli
linux$ pip install boto3
```

### iii. Copy Consumer Application to Server

The provided consumer application will poll the kenisis stream for packets forwarded from the Conduit gateways.

Run with
`linux$ python boto_consumer.py`


## 3. Create Kinesis Stream and IAM Credentials on AWS

### i. Create Kinesis Stream
[Stream Setup](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)

Create a Kinesis stream named "LoRaWAN" for the producer application on Conduit to forward received packets and the consumer application to poll for packets.

### ii. Create IAM credentials 
[Setup IAM role for Conduit access to kinesis stream](https://console.aws.amazon.com/iam/)

Credentials allow authenticate remote access from authorized producers and consumers.
As secure transfer such as SSL must also used for a fully secure deployment.
mLinux 4.x has support for SSL in python, it should be available in early 2018

### iii. Copy Stream IAM Credentials to the Conduit and Server

/home/root/.aws/credentials file can be created to authenticate the Conduit sensor posts

## 4. Start consumer and producer applications

### i. Run consumer 
```
linux$ python boto_consumer.py
```

### Run producer 
```
admin@mtcdt# python boto_producer.py
```


## 5. Connect LoRaWAN sensor and send packets to Conduit


Provided by [Jascori Consulting](https://www.jascori.com)