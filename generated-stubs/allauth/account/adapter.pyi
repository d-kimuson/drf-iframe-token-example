from . import app_settings as app_settings
from ..utils import build_absolute_uri as build_absolute_uri, email_address_exists as email_address_exists, generate_unique_username as generate_unique_username, get_user_model as get_user_model, import_attribute as import_attribute
from typing import Any, Optional

class DefaultAccountAdapter:
    error_messages: Any = ...
    request: Any = ...
    def __init__(self, request: Optional[Any] = ...) -> None: ...
    def stash_verified_email(self, request: Any, email: Any) -> None: ...
    def unstash_verified_email(self, request: Any): ...
    def stash_user(self, request: Any, user: Any) -> None: ...
    def unstash_user(self, request: Any): ...
    def is_email_verified(self, request: Any, email: Any): ...
    def format_email_subject(self, subject: Any): ...
    def get_from_email(self): ...
    def render_mail(self, template_prefix: Any, email: Any, context: Any): ...
    def send_mail(self, template_prefix: Any, email: Any, context: Any) -> None: ...
    def get_signup_redirect_url(self, request: Any): ...
    def get_login_redirect_url(self, request: Any): ...
    def get_logout_redirect_url(self, request: Any): ...
    def get_email_confirmation_redirect_url(self, request: Any): ...
    def is_open_for_signup(self, request: Any): ...
    def new_user(self, request: Any): ...
    def populate_username(self, request: Any, user: Any) -> None: ...
    def generate_unique_username(self, txts: Any, regex: Optional[Any] = ...): ...
    def save_user(self, request: Any, user: Any, form: Any, commit: bool = ...): ...
    def clean_username(self, username: Any, shallow: bool = ...): ...
    def clean_email(self, email: Any): ...
    def clean_password(self, password: Any, user: Optional[Any] = ...): ...
    def validate_unique_email(self, email: Any): ...
    def add_message(self, request: Any, level: Any, message_template: Any, message_context: Optional[Any] = ..., extra_tags: str = ...) -> None: ...
    def ajax_response(self, request: Any, response: Any, redirect_to: Optional[Any] = ..., form: Optional[Any] = ..., data: Optional[Any] = ...): ...
    def ajax_response_form(self, form: Any): ...
    def login(self, request: Any, user: Any) -> None: ...
    def logout(self, request: Any) -> None: ...
    def confirm_email(self, request: Any, email_address: Any) -> None: ...
    def set_password(self, user: Any, password: Any) -> None: ...
    def get_user_search_fields(self): ...
    def is_safe_url(self, url: Any): ...
    def get_email_confirmation_url(self, request: Any, emailconfirmation: Any): ...
    def send_confirmation_mail(self, request: Any, emailconfirmation: Any, signup: Any) -> None: ...
    def respond_user_inactive(self, request: Any, user: Any): ...
    def respond_email_verification_sent(self, request: Any, user: Any): ...
    def pre_authenticate(self, request: Any, **credentials: Any) -> None: ...
    def authenticate(self, request: Any, **credentials: Any): ...
    def authentication_failed(self, request: Any, **credentials: Any) -> None: ...
    def is_ajax(self, request: Any): ...

def get_adapter(request: Optional[Any] = ...): ...