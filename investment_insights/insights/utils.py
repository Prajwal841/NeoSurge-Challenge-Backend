import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user):
    # Create a payload containing the user ID and expiration time
    payload = {
        'user_id': user.id,  # User ID to identify the user
        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time (1 day from now)
    }
    # Encode the payload into a JWT token using the secret key from Django settings
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

def verify_jwt_token(token):
    try:
        # Decode the JWT token using the secret key from Django settings
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload  # Return the decoded payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Token is invalid
