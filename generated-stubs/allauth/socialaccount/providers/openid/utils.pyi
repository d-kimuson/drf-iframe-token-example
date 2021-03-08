from .models import OpenIDNonce as OpenIDNonce, OpenIDStore as OpenIDStore
from allauth.utils import valid_email_or_none as valid_email_or_none
from collections import UserDict
from openid.store.interface import OpenIDStore as OIDStore
from typing import Any, Optional

class JSONSafeSession(UserDict):
    data: Any = ...
    def __init__(self, session: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any): ...
    def __getitem__(self, key: Any): ...

class OldAXAttribute:
    PERSON_NAME: str = ...
    PERSON_FIRST_NAME: str = ...
    PERSON_LAST_NAME: str = ...

class AXAttribute:
    CONTACT_EMAIL: str = ...
    PERSON_NAME: str = ...
    PERSON_FIRST_NAME: str = ...
    PERSON_LAST_NAME: str = ...

AXAttributes: Any

class SRegField:
    EMAIL: str = ...
    NAME: str = ...

SRegFields: Any

class DBOpenIDStore(OIDStore):
    max_nonce_age: Any = ...
    def storeAssociation(self, server_url: Any, assoc: Optional[Any] = ...) -> None: ...
    def getAssociation(self, server_url: Any, handle: Optional[Any] = ...): ...
    def removeAssociation(self, server_url: Any, handle: Any) -> None: ...
    def useNonce(self, server_url: Any, timestamp: Any, salt: Any): ...

def get_email_from_response(response: Any): ...
def get_value_from_response(response: Any, sreg_names: Optional[Any] = ..., ax_names: Optional[Any] = ...): ...