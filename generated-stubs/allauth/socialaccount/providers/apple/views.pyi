from .apple_session import add_apple_session as add_apple_session, persist_apple_session as persist_apple_session
from .client import AppleOAuth2Client as AppleOAuth2Client
from .provider import AppleProvider as AppleProvider
from allauth.socialaccount.adapter import get_adapter as get_adapter
from allauth.socialaccount.models import SocialToken as SocialToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Error as OAuth2Error
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from allauth.utils import build_absolute_uri as build_absolute_uri, get_request_param as get_request_param
from typing import Any

class AppleOAuth2Adapter(OAuth2Adapter):
    client_class: Any = ...
    provider_id: Any = ...
    access_token_url: str = ...
    authorize_url: str = ...
    public_key_url: str = ...
    def get_public_key(self, id_token: Any): ...
    def get_client_id(self, provider: Any): ...
    def get_verified_identity_data(self, id_token: Any): ...
    def parse_token(self, data: Any): ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...
    def get_user_scope_data(self, request: Any): ...
    def get_access_token_data(self, request: Any, app: Any, client: Any): ...

def apple_post_callback(request: Any, finish_endpoint_name: str = ...): ...

oauth2_login: Any
oauth2_callback = apple_post_callback
oauth2_finish_login: Any
