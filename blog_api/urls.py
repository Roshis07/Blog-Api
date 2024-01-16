# urls.py
from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView

urlpatterns = [
    path('blog-posts/', BlogPostListCreateView.as_view(), name='blog-post-list-create'),
    path('blog-posts/<int:pk>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='blog-post-detail'),
]
