"""Get notified if event is called."""
import asyncio
import logging
from datetime import datetime

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

CONF_SLACK_NAME = 'slack_name'
CONF_EVENTS = 'events'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_SLACK_NAME, default=''): cv.string,
    vol.Required(CONF_EVENTS): cv.ensure_list,
})


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):

    event_notify = EventNotify(hass, config.get(CONF_SLACK_NAME))
    for event in config.get(CONF_EVENTS):
        hass.bus.async_listen(event, event_notify.event_fired)
    return True


class EventNotify():

    def __init__(self, hass, slack_name):
        self._hass = hass
        self._slack_name = slack_name.lower()

    def event_fired(self, event):
        data = event.data if event.data != {} else ''
        _LOGGER.debug("%s %s", event.event_type, data)

        if self._slack_name is not None and \
                self._hass.services.has_service('notify', self._slack_name):
            time = datetime.now().strftime(DATETIME_FORMAT)
            msg = "{} {} {}".format(time, event.event_type, data)
            self._hass.services.call('notify', self._slack_name,
                                     {'message': msg})
