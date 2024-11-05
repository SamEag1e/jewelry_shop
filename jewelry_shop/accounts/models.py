from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")

        # Set username equal to phone_number
        extra_fields["username"] = phone_number

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields["is_super_admin"] = True
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True

        # Set username equal to phone_number for superuser
        extra_fields["username"] = phone_number

        return self.create_user(
            phone_number=phone_number, password=password, **extra_fields
        )


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_product_admin = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)
    is_fellow_business = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
