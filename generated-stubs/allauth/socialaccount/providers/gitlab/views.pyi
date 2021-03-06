from allauth.socialaccount import app_settings as app_settings
from allauth.socialaccount.providers.gitlab.provider import GitLabProvider as GitLabProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class GitLabOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    provider_default_url: str = ...
    provider_api_version: str = ...
    settings: Any = ...
    provider_base_url: Any = ...
    access_token_url: Any = ...
    authorize_url: Any = ...
    profile_url: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, response: Any): ...

oauth2_login: Any
oauth2_callback: Any
