from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# we define blog model here

# models.Model: Django モデルであることを示す
class Post(models.Model): # Object
    # definition of property
    
    # models.ForeignKey: link to other models
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title : text which has limit
    title = models.CharField(max_length=200)
    # text: lots of text
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    # method: to publish the blog
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    # related_name: models.ForeignKey allows us to have access to comments from within Post model
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    text = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text