from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.TextField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Explanation(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    explanation = models.TextField()

class DebugRequest(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    debug_info = models.TextField()

class Collaboration(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User)
