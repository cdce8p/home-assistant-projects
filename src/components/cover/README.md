# Custom Cover Components

## Group

### Description

Group several cover entities into one.

### Example configuration

```yaml
cover:
  - platform: group
    name: My Group Cover
    entities:
      - cover.kitchen_window
      - cover.hall_window
      - cover.living_room_window
```

### Config options

| parameter | required | type | default | description |
| --------- | -------- | ---- | ------- | ----------- |
| name | no | string | Group Cover | Name of the entity. |
| entities | yes | list[string] | | List of cover entities to control.
