from .forms import FacebookConnectForm as FacebookConnectForm
from .provider import FacebookProvider as FacebookProvider, GRAPH_API_URL as GRAPH_API_URL, GRAPH_API_VERSION as GRAPH_API_VERSION
from allauth.socialaccount import app_settings as app_settings, providers as providers
from allauth.socialaccount.helpers import complete_social_login as complete_social_login, render_authentication_error as render_authentication_error
from allauth.socialaccount.models import SocialLogin as SocialLogin, SocialToken as SocialToken
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

logger: Any

def compute_appsecret_proof(app: Any, token: Any): ...
def fb_complete_login(request: Any, app: Any, token: Any): ...

class FacebookOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    provider_default_auth_url: Any = ...
    settings: Any = ...
    scope_delimiter: str = ...
    authorize_url: Any = ...
    access_token_url: Any = ...
    expires_in_key: str = ...
    def complete_login(self, request: Any, app: Any, access_token: Any, **kwargs: Any): ...

oauth2_login: Any
oauth2_callback: Any

def login_by_token(request: Any): ...
