from django.db import models
from typing import Any

class OpenIDStore(models.Model):
    server_url: Any = ...
    handle: Any = ...
    secret: Any = ...
    issued: Any = ...
    lifetime: Any = ...
    assoc_type: Any = ...

class OpenIDNonce(models.Model):
    server_url: Any = ...
    timestamp: Any = ...
    salt: Any = ...
    date_created: Any = ...
