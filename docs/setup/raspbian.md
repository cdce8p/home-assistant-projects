# Home Assistant on Rapbian



## Content

1. Common Tasks ([Link](#1-common-tasks))
2. Home Assistant Setup ([Link](#2-homeassistant-setup))



## 1. Common Tasks

#### Virtual environment

```bash
$ cd ~/home-assistant
$ source bin/activate

$ deactivate
```

#### Start Home Assistant

```bash
# **Activate environment**
$ hass
```

#### Update Home Assistant

```bash
$ cd ~/home-assistant
$ git fetch upstream dev
$ git rebase upstream/dev
```

#### List of useful directories

| Name | Directory |
| ---- | --------- |
| Config dir | `/home/pi/.homeassistant/` |
| Virtual Environment | `~/home-assistant/` |
| Src files | `~/home-assistant/homeassistant/` |



## 2. Home Assistant Setup

### First steps

 1. Download Hassbian Image [**Link**](https://github.com/home-assistant/pi-gen/releases/)
 2. Format SD Card [**SDFormatter**](https://www.sdcard.org/downloads/formatter_4/)
 3. Write image to SD Card [**Win32DiskImager**](https://sourceforge.net/projects/win32diskimager/)
 4. Copy [`wpa_supplicant.conf`](wpa_supplicant.conf) to `boot`
 5. Copy [`ssh`](ssh) to `boot`

### First Boot

 1. Login via SSH (user: pi, psk: raspberry)
 2. Update `raspi-config`
    
    ```bash
    $ sudo raspi-config

    # Change Local
    # Change Timezone
    # Change Wifi Country
    ```

 3. Install updates

    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get autoclean
    ```

 4. Install dependencies
    
    ```bash
    $ sudo apt-get install python3-pip python3-dev python3-venv
    $ sudo apt-get install libssl-dev libxml2-dev libxslt1-dev libjpeg-dev libffi-dev libudev-dev
    ```

 5. Setup local repository and virtual environment
    
    ```bash
    $ git clone https://github.com/YOUR_GIT_USERNAME/home-assistant.git
    
    $ cd home-assistant
    $ git remote add upstream https://github.com/home-assistant/home-assistant.git

    $ python3 -m venv .
    $ source bin/activate
    ```

 6. Install additional software
    
    ```bash
    ## Fritz-Compontents ##
    ## (This might take a while) ##
    ###############################
    $ sudo apt-get install libxslt-dev libxml2-dev python3-lxml
    # **Activate environment**
    $ pip3 install lxml
    $ pip3 install fritzconnection
    ```

 7. Copy config files to `home/pi/.homeassistant`

 8. Setup and run
    
    ```bash
    $ cd ~/home-assistant
    $ script/setup
    
    $ source bin/activate
    $ hass
    ```
