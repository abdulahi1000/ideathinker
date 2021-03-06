from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from requests import get
from django.db import transaction
import os


from .serializers import *

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse

# Create your views here.


@api_view(['GET'])
def requestList(request):
    data=[
        '/api/all_user/',
        '/api/login/',
        '/api/register/',
        '/api/uploadImage/',
        '/api/getWeather/',
        {'for dummy email sending':'/api/sendMail/'},

    ]
    return Response(data)

@api_view(['GET'])
def allUserProfile(request):
    users = UserProfile.objects.all()

    serializer = UserProfileSerializer(users, many=True)

    return Response(serializer.data)

class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        return serializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

@api_view(['POST'])
@transaction.atomic
def registerUser(request): 
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password =make_password(data['password'])
        ) 
        userprofile = UserProfile.objects.create(
            user=user,
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            phone_number = data['phone_number'],

        )
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)
    except: 
        massage ={'detail': 'user with this email already exists'}
        return Response(massage, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def imageUpload(request):
    user = request.user

    userprofile = UserProfile.objects.get(user=user)
    userprofile.profile_pic = request.FILES.get('image')
    userprofile.save()

    serializer = UserProfileSerializer(userprofile)
    return Response(serializer.data)

@api_view(['POST'])
def getWeather(request):
    data = request.data
    # appId = os.environ.get('WEATHER_API_ID')
    appId = ab1d18fb699a235516a19f175a46585d
    url = 'https://api.openweathermap.org/data/2.5/weather'
    response = get(url+f"?lat={data['lat']}&lon={data['lon']}&appid={appId}")

    if response.status_code != status.HTTP_200_OK:
        return Response({'details':'something went wrong with the api server, try again'})
    else:
        return Response(response.json())

@api_view(['POST'])
def sendMail(request):

    subject = 'Welcome to Idea Thinker'
    html_message = render_to_string('base/welcome_email.html', 
    {'fullName': 'qudus' +' '+ 'abdulahi', })
    plain_message = strip_tags(html_message) 
    from_email = 'abdulahiopeyemiq1@gmail.com'
    to= 'abdulahiopeyemiq1@gmail.com'

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    return Response('working')

