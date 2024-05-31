from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Attempt to retrieve a user based on the provided email
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If the user does not exist, return None (authentication failed)
            return None

        # Check if the provided password matches the user's password
        if user.check_password(password):
            # If the passwords match, return the user (authentication successful)
            return user
        # If the passwords do not match, return None (authentication failed)
        return None
