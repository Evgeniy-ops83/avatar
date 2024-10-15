from django.urls import path
from .views import register_user, login_user, check_session, logout_user

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login'),
    path('check-session/', check_session, name='check_session'),
    path('logout/', logout_user, name='logout'),
]
