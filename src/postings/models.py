from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse 

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
        
    def get_api_url(self, request=None):
        return reverse("api-postings:post-rud", kwargs={'pk': self.id}, request=request)