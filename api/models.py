from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)