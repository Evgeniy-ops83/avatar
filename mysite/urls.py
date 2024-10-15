from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),  # Подключаем маршруты приложения
    path('auth/', include('authapp.urls')), 
]
