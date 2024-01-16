from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView, ReviewCreateView

urlpatterns = [
    path('blog-posts/', BlogPostListCreateView.as_view(), name='blog-post-list-create'),
    path('blog-posts/<int:pk>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='blog-post-retrieve-update-destroy'),
    path('blog-posts/<int:blog_post_id>/reviews/', ReviewCreateView.as_view(), name='review-create'),
]
