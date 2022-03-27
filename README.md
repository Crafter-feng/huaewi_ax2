# Huawei Router AX2/AX2Pro  Integration in Home Assistant
Component to integrate the Huawei AX2 and AX2Pro (tested on model Huawei AX2 and AX2Pro).

base on https://github.com/juacas/honor_x3

## Example usage

```
# Setup the platform huaewi_ax2
huaewi_ax2:
  host: 192.168.0.1
  username: admin
  password: !secret router_password

# Enable and customize the tracker's parameters
device_tracker:
- platform: huaewi_ax2
  interval_seconds: 60
  consider_home: 180
  new_device_defaults:
    track_new_devices: false
```
