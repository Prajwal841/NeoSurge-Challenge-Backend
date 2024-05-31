import jwt
from django.conf import settings
from django.http import JsonResponse
from .models import User

def jwt_middleware(get_response):
    # Define a middleware function that checks JWT token for authentication
    def middleware(request):
        # Retrieve the JWT token from the Authorization header of the request
        token = request.headers.get('Authorization', None)
        if token:
            try:
                # Check if the token starts with 'Bearer ' and extract the token
                if token.startswith('Bearer '):
                    token = token.split(' ')[1]
                else:
                    # If the token doesn't start with 'Bearer ', return an error response
                    return JsonResponse({'error': 'Invalid token header format'}, status=403)
                
                # Decode the JWT token using the secret key from Django settings
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                # Extract the user ID from the decoded token
                user_id = decoded_token.get('user_id')
                if user_id:
                    # Retrieve the user object based on the user ID from the token
                    user = User.objects.get(user_id=user_id)
                    # Assign the user object to the request for further processing
                    request.user = user
                else:
                    # If user ID is not present in the token payload, return an error response
                    return JsonResponse({'error': 'Invalid token payload'}, status=403)
            except jwt.ExpiredSignatureError:
                # If the token has expired, return an error response
                return JsonResponse({'error': 'Token has expired'}, status=403)
            except jwt.DecodeError:
                # If there's an error decoding the token, return an error response
                return JsonResponse({'error': 'Error decoding token'}, status=403)
            except User.DoesNotExist:
                # If the user corresponding to the token is not found, return an error response
                return JsonResponse({'error': 'User not found'}, status=403)
        else:
            # If no token is provided, set request.user to None
            request.user = None
        
        # Call the next middleware or view function in the chain
        return get_response(request)

    # Return the middleware function
    return middleware
