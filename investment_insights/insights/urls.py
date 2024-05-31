from django.urls import path
from .views import generate_insight
from .views import save_user_preference, get_user_preference, save_insight, get_insights,update_preferences,signup,login

urlpatterns = [
    path('generate-insight/', generate_insight, name='generate_insight'),
]

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('generate-insight/', generate_insight, name='generate_insight'),
    path('save-preference/', save_user_preference, name='save_preference'),
    path('get-preference/<str:user_id>/', get_user_preference, name='get_preference'),
    path('save-insight/', save_insight, name='save_insight'),
    path('get-insights/<str:user_id>/', get_insights, name='get_insights'),
    path('api/update-preferences/', update_preferences, name='update_preferences'),

]