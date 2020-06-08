from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from  django.core.validators import validate_email

class UserManager(BaseUserManager):

    def create_user(self, email, **extra_fields):
        validate_email(email)

        user = self.model(email=self.normalize_email(email),
                   **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255,
                              validators=[validate_email])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'