from django.db import models

class blog_post(models.Model):
    Name=models.CharField(max_length=20)
    Blog_body=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Name








# Create your models here.
