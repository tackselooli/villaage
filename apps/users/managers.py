from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_field
    ):
        if not username:
            raise ValueError(_("Users must submit a username"))

        if not first_name:
            raise ValueError(_("Users must submit a first name"))

        if not last_name:
            raise ValueError(_("Users must submit a last name"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Pls enter valid email address"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_field
        )

        user.set_password(password)
        extra_field.setdefault("is_staff", False)
        extra_field.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **extra_field
    ):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)
        extra_field.setdefault("is_active", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff = true"))

        if extra_field.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser = true"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Pls enter valid email address"))

        user = self.create_user(
            username, first_name, last_name, email, password, **extra_field
        )
        user.save(using=self._db)
        return user
