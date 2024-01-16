from rest_framework import serializers
from .models import BlogPost, Review  # Fix the import and use CamelCase for the model name

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Add this line

    class Meta:
        model = BlogPost
        fields = "__all__"
