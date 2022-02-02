from django.urls import path
from . import views


urlpatterns = [
    path('all_user', views.allUserProfile, name='user_list'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login_with_token' ),
    path('register/', views.registerUser, name='register'),
    path('uploadImage/', views.imageUpload, name='image-upload'),
    path('getWeather/', views.getWeather, name='get_weather'),
    path('sendMail/', views.sendMail, name='sendMail'),


]