from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
from typing import List, Any, Optional

from django.conf import settings


# ユーザーを作成した後に、トークンを自動生成する
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender: str, instance: Optional['User'] = None, created: bool = False, **kwargs: Any) -> None:
    if created and instance is not None:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str, is_staff: bool, is_superuser: bool) -> 'User':
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=timezone.now(),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str) -> 'User':
        return self._create_user(email, password, False, False)

    def create_superuser(self, email: str, password: str) -> 'User':
        return self._create_user(email, password, True, True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(
        _('password'),
        max_length=128,
        validators=[MinLengthValidator(5)]
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects = UserManager()

    def __repr__(self) -> str:
        return "User <{}>".format(self.email)

    __str__ = __repr__
