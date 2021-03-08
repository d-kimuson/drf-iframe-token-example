from allauth.socialaccount.providers.globus.provider import GlobusProvider as GlobusProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class GlobusAdapter(OAuth2Adapter):
    provider_id: Any = ...
    provider_default_url: str = ...
    provider_base_url: str = ...
    access_token_url: Any = ...
    authorize_url: Any = ...
    profile_url: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, response: Any): ...

oauth2_login: Any
oauth2_callback: Any