from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video_id = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=250, null=False)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    
    
class Reply(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=250, null=False)