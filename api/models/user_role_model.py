from django.db import models

class UserRoleModel(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'
