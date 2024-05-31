import secrets
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure that an email address is provided
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)  # Normalize the email address
        user_id = secrets.token_hex(2)  # Generate a random 4-character hexadecimal string
        extra_fields.setdefault('user_id', user_id)  # Set the user_id
        # Create a new user instance
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Set the user's password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Ensure that the user is a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Create a new superuser
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)  # Email field with unique constraint
    user_id = models.CharField(max_length=5, unique=True)  # Unique user ID field

    objects = UserManager()  # Custom user manager

    USERNAME_FIELD = 'email'  # Field to use for authentication
    REQUIRED_FIELDS = []  # Additional required fields for user creation

    def __str__(self):
        return self.email  # String representation of the user object
