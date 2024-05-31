from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
import jwt
from datetime import datetime
from .gpt35_service import GPT35Service

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import secrets
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .decorators import login_required
from django.contrib.auth import authenticate
from .models import User


# client = MongoClient('mongodb://localhost:27017/')
# db = client['investment_insights_db']
# collection = db['user']



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        # Generate a random 4-character hexadecimal user ID
        user_id = secrets.token_hex(2)

        # Create the user
        user = User(email=email, user_id=user_id)
        user.set_password(password)
        user.save()

        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)  # Use 'username' for email

        if user is not None:
            # Generate JWT token
            token = jwt.encode({'user_id': user.user_id}, settings.SECRET_KEY, algorithm='HS256')

            return JsonResponse({'token': token})
        else:
            # Check if the user exists with the provided email
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Incorrect password'}, status=400)
            else:
                return JsonResponse({'error': 'User does not exist'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@csrf_exempt
@login_required
def generate_insight(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        user_id = user_data.get('user_id', '')
        prompt = user_data.get('prompt', '')
        
        # Generate insight using GPT-3.5 API
        gpt35_service = GPT35Service()
        insight = gpt35_service.generate_insight(prompt, settings.OPENAI_API_KEY)
        
        # Save the generated insight in MongoDB
        if insight and user_id:
            # Get existing insights for the user
            existing_insights = settings.MONGO_DB.insights.find_one({'user_id': user_id})
            if existing_insights:
                # Append the new insight to existing insights if the 'insights' key is present
                insights_list = existing_insights.get('insights', [])
                insights_list.append({
                    'insight': insight,
                    'created_at': datetime.utcnow()
                })
                # Update the existing document with the appended insights
                settings.MONGO_DB.insights.update_one(
                    {'user_id': user_id},
                    {'$set': {'insights': insights_list}}
                )
                return JsonResponse({'insight': insight, 'message': 'Insight appended successfully'})
            else:
                # Create a new document for the user with the first insight
                result = settings.MONGO_DB.insights.insert_one({
                    'user_id': user_id,
                    'insights': [{
                        'insight': insight,
                        'created_at': datetime.utcnow()
                    }]
                })
                return JsonResponse({'insight': insight, 'message': 'Insight generated and saved successfully', 'id': str(result.inserted_id)})
        else:
            return JsonResponse({'error': 'Error generating or saving insight'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
@login_required
def save_user_preference(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        preferences = data.get('preferences')

        # Upsert user preference in MongoDB
        result = settings.MONGO_DB.user_preferences.update_one(
            {'user_id': user_id},
            {'$set': {'preferences': preferences}},
            upsert=True
        )

        if result.upserted_id:
            return JsonResponse({'message': 'Preferences saved successfully', 'id': str(result.upserted_id)})
        else:
            return JsonResponse({'message': 'Preferences updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def get_user_preference(request, user_id):
    preference = settings.MONGO_DB.user_preferences.find_one({'user_id': user_id})
    if preference:
        preference['_id'] = str(preference['_id'])  # Convert ObjectId to string for JSON serialization
        return JsonResponse(preference)
    else:
        return JsonResponse({'error': 'User preferences not found'}, status=404)

@csrf_exempt
@login_required
def save_insight(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        insight = data.get('insight')

        # Insert insight in MongoDB
        result = settings.MONGO_DB.insights.insert_one({
            'user_id': user_id,
            'insight': insight,
            'created_at': datetime.utcnow()
        })

        return JsonResponse({'message': 'Insight saved successfully', 'id': str(result.inserted_id)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def get_insights(request, user_id):
    insights = settings.MONGO_DB.insights.find({'user_id': user_id})
    insights_list = []
    for insight in insights:
        insight['_id'] = str(insight['_id'])  # Convert ObjectId to string for JSON serialization
        insights_list.append(insight)
    return JsonResponse({'insights': insights_list})

@csrf_exempt
@login_required
def update_preferences(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        user_id = user_data.get('user_id', '')
        preferences = user_data.get('preferences', {})
        
        # Update the user preferences in the database
        if user_id and preferences:
            settings.MONGO_DB.users.update_one(
                {'user_id': user_id},
                {'$set': {'preferences': preferences}}
            )
            return JsonResponse({'message': 'Preferences updated successfully'})
        else:
            return JsonResponse({'error': 'Invalid user ID or preferences'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
