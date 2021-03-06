from allauth.socialaccount.adapter import get_adapter as get_adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client as OAuth2Client, OAuth2Error as OAuth2Error
from typing import Any

class Scope:
    EMAIL: str = ...
    NAME: str = ...

class AppleOAuth2Client(OAuth2Client):
    def generate_client_secret(self): ...
    def get_client_id(self): ...
    def get_access_token(self, code: Any): ...
    def get_redirect_url(self, authorization_url: Any, extra_params: Any): ...
