# My Home Assistant Documentation

This is my private documentation to Home Assistant. It is meant as an extension to the official one ([Link](https://home-assistant.io/)).



## Content

 1. Upgrade Home Assistant on Hassbian ([Link](#1-update-home-assistant-on-hassbian))
 2. Notes Configuration File ([Link](#2-notes-configuration-file))
 2. Setup
    1. Setup Home Assistant on Hassbian ([Link](setup/README.md))
    2. Setup Home Assistant on Raspbian ([Link](setup/raspbian.md))
    3. Setup Z-Wave ([Link](setup/z-wave.md))
    4. Software ([Link](setup/software.md))



## 1. Update Home Assistant on Hassbian

```bash
$ sudo systemctl stop home-assistant@homeassistant.service

$ sudo su -s /bin/bash homeassistant
$ source /srv/homeassistant/bin/activate
$ pip3 install --upgrade homeassistant
$ exit

$ sudo systemctl start home-assistant@homeassistant.service
```



## 2. Notes Configuration File

#### YAML Notes

```yaml
# Secrets
latitude: !secret latitude

# Include
customize: !include customize.yaml
group: !include_dir_merge_named group/
sensor: !include_dir_merge_list sensor/
```

#### Templating

 - **Templating** ([Link](https://home-assistant.io/docs/configuration/templating/))
 - **Sensor Template** ([Link](https://home-assistant.io/components/sensor.template/))
 - **Automation Templating** ([Link](https://home-assistant.io/docs/automation/templating/))
