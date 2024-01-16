from .models import blog_post
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):  # Fix the typo here
    class Meta:
        model = blog_post
        fields = "__all__"
