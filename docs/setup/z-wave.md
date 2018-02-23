# Z-Wave

https://home-assistant.io/docs/z-wave/

### Aeotec Z-Stick

```bash
# Find USB Port
$ sudo ls /dev/tty
$ sudo dmesg | grep USB
```

```yaml
zwave:
  usb_path: /dev/ttyACM0  ## or /ttyACM1
```

```bash
# Disable disco lights
$ echo -e -n "\x01\x08\x00\xF2\x51\x01\x00\x05\x01\x51" > /dev/serial/by-id/usb-0658_0200-if00
```

### Razberry Board

```bash
# Install Z-Way
$ wget -q -O - razberry.z-wave.me/install | sudo bash

# Deactivate Z-Way Service
$ sudo update-rc.d z-way-server disable

$ sudo nano /boot/config.txt
```

```conf
# Add this to file
dtoverlay=pi3-disable-bt
```

```yaml
zwave:
  usb_path: /dev/ttyAMA0
```
