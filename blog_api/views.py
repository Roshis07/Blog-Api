from rest_framework import generics, permissions
from .models import BlogPost, Review
from .serializer import BlogSerializer, ReviewSerializer

class AdminCanCreatePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and request.user.is_staff

class BlogPostListCreateView(generics.ListCreateAPIView):
    permission_classes = [AdminCanCreatePostPermission, permissions.IsAuthenticatedOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedUser]  

    def perform_create(self, serializer):
        blog_post_id = self.kwargs.get('blog_post_id')
        blog_post = generics.get_object_or_404(BlogPost, pk=blog_post_id)
        serializer.save(user=self.request.user, blog_post=blog_post)

    def post(self, request, *args, **kwargs):
        blog_post_id = kwargs.get('blog_post_id')
        return self.create(request, *args, **kwargs)
