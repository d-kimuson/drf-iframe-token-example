from . import app_settings as app_settings, helpers as helpers
from ..account.views import AjaxCapableProcessFormViewMixin as AjaxCapableProcessFormViewMixin, CloseableSignupMixin as CloseableSignupMixin, RedirectAuthenticatedUserMixin as RedirectAuthenticatedUserMixin
from ..utils import get_form_class as get_form_class
from .adapter import get_adapter as get_adapter
from .forms import DisconnectForm as DisconnectForm, SignupForm as SignupForm
from .models import SocialAccount as SocialAccount, SocialLogin as SocialLogin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from typing import Any

class SignupView(RedirectAuthenticatedUserMixin, CloseableSignupMixin, AjaxCapableProcessFormViewMixin, FormView):
    form_class: Any = ...
    template_name: Any = ...
    def get_form_class(self): ...
    sociallogin: Any = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def is_open(self): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...
    def get_context_data(self, **kwargs: Any): ...
    def get_authenticated_redirect_url(self): ...

signup: Any

class LoginCancelledView(TemplateView):
    template_name: Any = ...

login_cancelled: Any

class LoginErrorView(TemplateView):
    template_name: Any = ...

login_error: Any

class ConnectionsView(AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...
    def get_ajax_data(self): ...

connections: Any