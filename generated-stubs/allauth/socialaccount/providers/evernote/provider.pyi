from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider as OAuthProvider
from typing import Any

class EvernoteAccount(ProviderAccount):
    def get_profile_url(self) -> None: ...
    def get_avatar_url(self) -> None: ...

class EvernoteProvider(OAuthProvider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...

provider_classes: Any
