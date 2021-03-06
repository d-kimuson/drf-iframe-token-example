from allauth.socialaccount import app_settings as app_settings
from allauth.socialaccount.providers.auth0.provider import Auth0Provider as Auth0Provider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class Auth0OAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    supports_state: bool = ...
    settings: Any = ...
    provider_base_url: Any = ...
    access_token_url: Any = ...
    authorize_url: Any = ...
    profile_url: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, response: Any): ...

oauth2_login: Any
oauth2_callback: Any
