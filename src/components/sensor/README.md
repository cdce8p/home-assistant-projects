# Custom Sensor Components

## Event notify

### Description

Print a log message if an event has been fired by Home Assistant. If a slack channel name is given, it can also notify it. To activate the log messages, enable `debug` logging:

```yaml
logger:
  logs:
    custom_components.sensor.entity_notify: debug
```

### Example configuration

```yaml
sensor:
  - platform: event_notify
    slack_name: default_channel
    events:
      - homeassistant_start
      - homeassistant_stop
      - zwave.network_ready
```

### Config options

| parameter | required | type | default | description |
| --------- | -------- | ---- | ------- | ----------- |
| slack_name | no | string | | Name of slack notify platform. |
| events | yes | list[string] | | Events that should be tracked. |


## Wind direction

### Description

Convert the wind direction from degrees to the direction names.

### Example configuration

```yaml
sensor:
  - platform: yr
    monitored_conditions:
      - windDirection

  - platform: wind_dir
    name: YR Wind Direction:
    entity_id: sensor.yr_wind_direction
```

### Config options

| parameter | required | type | default | description |
| --------- | -------- | ---- | ------- | ----------- |
| name | no | string | Wind direction | Name of the entity. |
| entity_id | yes | string | | Sensor entity_id that provides the wind direction in degrees. |
