# My Home Assistant Projects

A collection of my personal Home Assistant projects.



## Content

 1. Documentation ([Link](docs))
 2. Src files
    1. Components
       1. Cover - `Group` Platform ([Link](src/components/cover))
       2. Sensor - `Event_notify` Platform ([Link](src/components/sensor))
       3. Sensor - `Wind_dir` Platform ([Link](src/components/sensor))
    2. Custom UI ([Link](src/custom_ui))
       1. Cover
       2. Input Number



## Update Home Assistant on Hassbian

```bash
$ sudo systemctl stop home-assistant@homeassistant.service

$ sudo su -s /bin/bash homeassistant
$ source /srv/homeassistant/bin/activate
$ pip3 install --upgrade homeassistant
$ exit

$ sudo systemctl start home-assistant@homeassistant.service
```
