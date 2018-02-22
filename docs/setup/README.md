# Home Assistant on a Raspberry Pi

## Content

1. Common Tasks ([Link](#1-common-tasks))
2. Home Assistant Setup ([Link](#2-home-assistant-setup))
3. Setup Z-Wave ([Link](#3-setup-z-wave))
4. Software ([Link](#4-software))




## 1. Common Tasks

#### Virtual environment

```bash
$ sudo su -s /bin/bash homeassistant
$ source /srv/homeassistant/bin/activate

$ deactivate
$ su pi
```

#### Start/Stop/Restart Home Assistant

```bash
$ sudo systemctl [start|stop|restart|status] home-assistant@homeassistant.service
```

```bash
## Manual start ##
##################
# **Activate environment**
$ hass
```

#### List of useful directories

| Name | Directory |
| ---- | --------- |
| Config dir | `/home/homeassistant/.homeassistant/` |
| Virtual Environment | `/srv/homeassistant/` |
| Src files | `/srv/homeassistant/lib/python[X.X]/site-packages/homeassistant/` |

#### Common Linux tasks

| Task | Command |
| ---- | ------- |
| Find files | `find / -type [f | d] -iname '*name*'` |
| Find content in files | `grep -rnwl './' -e 'pattern'` |



## 2. Home Assistant Setup

How I setup `Home Assistant` on my Raspberry Pi using `Hassbian 1.3`.

### First steps

 1. Download Hassbian Image [**Link**](https://github.com/home-assistant/pi-gen/releases/)
 2. Format SD Card [**SDFormatter**](https://www.sdcard.org/downloads/formatter_4/)
 3. Write image to SD Card [**Win32DiskImager**](https://sourceforge.net/projects/win32diskimager/)
 4. Copy [`wpa_supplicant.conf`](wpa_supplicant.conf) to `boot`

### First Boot

 1. Login via SSH (user: pi, psk: raspberry)
 2. Wait until frontend is loaded `[ip]:8123`
 3. Update `raspi-config`
    
    ```bash
    $ sudo raspi-config

    # Change Local
    # Change Timezone
    # Change Wifi Country
    ```

 4. Install updates

    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get autoclean
    ```

 5. Install Hassbian `Addons`
    
    ```bash
    $ sudo hassbian-config show
    ```

 6. Install additional software

    ```bash
    ## Colorlog ##
    ##############
    # **Activate environment**
    $ hass --script check_config
    # pip3 install colorlog
    ```

    ```bash
    ## Fritz-Compontents ##
    ## (This might take a while) ##
    ###############################
    $ sudo apt-get install libxslt-dev libxml2-dev python3-lxml
    # **Activate environment**
    $ pip3 install lxml
    $ pip3 install fritzconnection
    ```

 7. Copy config files to `home/homeassistant/.homeassistant`



## 3. Setup Z-Wave

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



## 4. Software

 - SSH Client: Putty ([Link](http://www.putty.org/))
 - SSH File Client: WinSCP ([Link](https://winscp.net/eng/download.php))
   - File Protocol: `SCP`
   - Advanced Options - Shell: `sudo su -`
