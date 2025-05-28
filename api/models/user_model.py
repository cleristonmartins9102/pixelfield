from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_role_model import UserRoleModel

class UserModel(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoleModel.choices,
        default=UserRoleModel.USER
    )
    def __str__(self) -> str:
        return self.first_name # type: ignore