"""Config flow for Lab Target, creates an entry without asking anything."""

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class LabTargetConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Lab Target."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Create the entry straight away."""
        return self.async_create_entry(title="Lab Target", data={})
