"""Sensor platform. Convert wind direction form degree to direction."""
import asyncio
import logging

import voluptuous as vol

from homeassistant.core import callback
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_ENTITY_ID, CONF_NAME, STATE_UNKNOWN
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_state_change

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="Wind direction"): cv.string,
    vol.Required(CONF_ENTITY_ID): cv.entity_id,
})


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):

    async_add_devices(
        [WindDirSensor(hass, config.get(CONF_NAME),
                       config.get(CONF_ENTITY_ID))])
    return True


def degree_to_direction(degree):
    if degree >= 0 and degree < 22.5:
        return 'N'
    if degree >= 22.5 and degree < 67.5:
        return 'NE'
    if degree >= 67.5 and degree < 112.5:
        return 'E'
    if degree >= 112.5 and degree < 157.5:
        return 'SE'
    if degree >= 157.5 and degree < 202.5:
        return 'S'
    if degree >= 202.5 and degree < 247.5:
        return 'SW'
    if degree >= 247.5 and degree < 292.5:
        return 'W'
    if degree >= 292.5 and degree < 337.5:
        return 'NW'
    if degree >= 337.5 and degree <= 360:
        return 'N'


class WindDirSensor(Entity):

    def __init__(self, hass, name, entity_id):
        self._hass = hass
        self._name = name
        self._entity_id = entity_id

    @asyncio.coroutine
    def async_added_to_hass(self):

        @callback
        def state_change_listener(*args):
            self.async_schedule_update_ha_state(True)

        async_track_state_change(self._hass, self._entity_id,
                                 state_change_listener)

    @property
    def name(self):
        return self._name

    @property
    def should_poll(self):
        return False

    @property
    def state(self):
        state = self._hass.states.get(self._entity_id)
        if state is None:
            return STATE_UNKNOWN

        try:
            return degree_to_direction(float(state.state))
        except ValueError:
            return STATE_UNKNOWN
