from allauth.account.models import EmailAddress as EmailAddress
from allauth.socialaccount.providers.base import Provider as Provider, ProviderAccount as ProviderAccount
from typing import Any

class PersonaAccount(ProviderAccount):
    def to_str(self): ...

class PersonaProvider(Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def media_js(self, request: Any): ...
    def get_login_url(self, request: Any, **kwargs: Any): ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...
    def extract_email_addresses(self, data: Any): ...

provider_classes: Any
