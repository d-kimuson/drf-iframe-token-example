from django.apps import AppConfig
from typing import Any

class AccountConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...