from django.shortcuts import render

from rest_framework import generics, permissions
# Create your views here.
# views.py
from rest_framework import generics
from .models import blog_post
from .serializer import BlogSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = blog_post.objects.all()
    serializer_class = BlogSerializer

class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = blog_post.objects.all()
    serializer_class = BlogSerializer
