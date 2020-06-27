from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model. """

    def create_user(self,email, name,password=None):
        """Creates a new user profile object. """

        if not email:
            raise ValueError("User Must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_user_fullname(self):
        """Used to get a users full name """
        return self.name

    def get_user_shortname(self):
        """Used to get a users full name """

        return self.name

    def __str__(self):
        """Used to get a string representation of a string """

        return self.email
