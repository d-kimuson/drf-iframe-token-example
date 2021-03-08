from allauth.account.models import EmailAddress as EmailAddress
from allauth.socialaccount.providers.amazon_cognito.utils import convert_to_python_bool_if_value_is_json_string_bool as convert_to_python_bool_if_value_is_json_string_bool
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class AmazonCognitoAccount(ProviderAccount):
    def to_str(self): ...
    def get_avatar_url(self): ...
    def get_profile_url(self): ...

class AmazonCognitoProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...
    def get_default_scope(self): ...
    def extract_email_addresses(self, data: Any): ...
    def extract_extra_data(self, data: Any): ...
    @classmethod
    def get_slug(cls): ...

provider_classes: Any
