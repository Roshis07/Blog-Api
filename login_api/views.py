from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from login_api.serializer import UserSerializer
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        