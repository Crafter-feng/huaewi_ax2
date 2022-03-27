import unittest
import os
from HuaweiAX2client.huawei_ax2_client import HuaweiAX2Client

#import ...

#class HuaweiAX2ClientTest(unittest.TestCase):
password = os.environ.get('TEST_PASSWORD', '!secret')
host = os.environ.get('TEST_HOST', 'xx192.168.3.1')

client = HuaweiAX2Client(host, 'admin', password)
res = client.login()
if res:
    devices = client.get_devices_response()

    for device in devices:
        if device['Active']:
            name = device['HostName']
            name = name.replace('未知设备', 'Desconocido')
            print(name)
else:
    print("Error: {0}".format(client.statusmsg));
client.logout()
