import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class SimpliStreamerFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initiated by the user."""
        if user_input is None:
            return self._show_config_form()

        # Here is where you would process the user input, if necessary,
        # and create the configuration entry:
        return self.async_create_entry(title="SimpliSafe Streamer", data=user_input)

    @callback
    def _show_config_form(self, errors=None):
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("parameter_1"): str,
                vol.Required("parameter_2"): str,
            }),
            errors=errors or {},
        )
