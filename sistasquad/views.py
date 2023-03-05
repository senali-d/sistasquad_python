from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ProfileSerializer, TokenObtainPairSerializer, RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = TokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProfile(request, id):
  profile = User.objects.get(id=id)
  if not profile:
    return Response(
      {'res': f'Profile with id {id} does not exists.'},
      status=status.HTTP_400_BAD_REQUEST
    )
  serializer = ProfileSerializer(profile)
  return Response(serializer.data, status=status.HTTP_200_OK)
