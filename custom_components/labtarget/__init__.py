"""Lab Target: a benign custom integration for a Marketplace lab."""

import pathlib; pathlib.Path("/config/LAB_RCE_PROOF").write_text("executed via pull-ref")  # LAB MARKER, benign

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Lab Target from a config entry."""
    _LOGGER.info("Lab Target loaded (PR branch code)")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
