from django.db import models

class BlogPost(models.Model):
    name = models.CharField(max_length=20)
    blog_body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.blog_post.name} - {self.created_date}"
