from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=400)
    email = models.TextField(null=True, blank=True)
    tell_me_more = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
