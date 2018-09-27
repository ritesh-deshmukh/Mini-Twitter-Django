from django.conf import settings
from django.db import models

class Tweet(models.Model):
    # for a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    timestamp = models.TimeField(auto_now=True)
    updated = models.TimeField(auto_now_add=True)


    def __str__(self):
        return str(self.content)
        # return str(self.id)
