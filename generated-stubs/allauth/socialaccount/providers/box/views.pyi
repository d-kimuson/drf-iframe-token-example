from .provider import BoxOAuth2Provider as BoxOAuth2Provider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class BoxOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    access_token_url: str = ...
    authorize_url: str = ...
    profile_url: str = ...
    redirect_uri_protocol: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...

oauth_login: Any
oauth_callback: Any