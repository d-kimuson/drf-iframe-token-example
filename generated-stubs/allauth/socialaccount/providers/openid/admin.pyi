from .models import OpenIDNonce as OpenIDNonce, OpenIDStore as OpenIDStore
from django.contrib import admin

class OpenIDStoreAdmin(admin.ModelAdmin): ...
class OpenIDNonceAdmin(admin.ModelAdmin): ...
