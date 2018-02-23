# Custom UI

### Installation

Copy files to `.homeassistant/www/custom_ui`.  
Add the following to your configuration file:

```yaml
homeassistant:
  # ...
  customize:
    cover.living_room:
      custom_ui_state_card: state-card-my-cover

frontend:
  javascript_version: latest
  extra_html_url:
    - /local/custom_ui/state-card-my-cover.html
```


## Custom `cover` state card

Copy all files from the [cover](cover) folder to your `custom_ui` folder.  
Display the current position of the cover below the cover name.

| | Name |
| --- | --- |
| extra_html_url | 'state-card-my-cover.html' |
| custom_ui_state_card | 'state-card-my-cover' |


## Custom `input_number` state card

Copy all files from the [input_number](input_number) folder to your `custom_ui` folder.  
Hide the current state and unit_of_measurement from the state card.

| | Name |
| --- | --- |
| extra_html_url | 'state-card-my-input_number.html' |
| custom_ui_state_card | 'state-card-my-input_number' |
