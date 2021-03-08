from .provider import VimeoProvider as VimeoProvider
from allauth.socialaccount.providers.oauth.client import OAuth as OAuth
from allauth.socialaccount.providers.oauth.views import OAuthAdapter as OAuthAdapter, OAuthCallbackView as OAuthCallbackView, OAuthLoginView as OAuthLoginView
from typing import Any

class VimeoAPI(OAuth):
    url: str = ...
    def get_user_info(self): ...

class VimeoOAuthAdapter(OAuthAdapter):
    provider_id: Any = ...
    request_token_url: str = ...
    access_token_url: str = ...
    authorize_url: str = ...
    def complete_login(self, request: Any, app: Any, token: Any, response: Any): ...

oauth_login: Any
oauth_callback: Any