from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from login_api.serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens
            tokens = get_tokens_for_user(user)

            # Include the tokens in the response
            response_data = {
                'refresh_token': tokens['refresh'],
                'access_token': tokens['access'],
                'user': serializer.data
            }

            return Response(response_data)
        return Response(serializer.errors, status=400)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def custom_logout(request):
    try:
        request.auth.delete()  # Invalidate the token
    except AttributeError:
        pass  # If the token is not present, do nothing
    return Response({'detail': 'Successfully logged out.'})