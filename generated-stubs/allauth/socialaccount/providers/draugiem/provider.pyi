from allauth.socialaccount.providers.base import Provider as Provider, ProviderAccount as ProviderAccount
from typing import Any

class DraugiemAccount(ProviderAccount):
    def get_avatar_url(self): ...
    def to_str(self): ...

class DraugiemProvider(Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def get_login_url(self, request: Any, **kwargs: Any): ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...
    def extract_extra_data(self, data: Any): ...

provider_classes: Any
