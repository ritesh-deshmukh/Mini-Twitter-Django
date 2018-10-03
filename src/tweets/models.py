from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_content
class Tweet(models.Model):
    # for a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    timestamp = models.TimeField(auto_now=True)
    updated = models.TimeField(auto_now_add=True)


    def __str__(self):
        return str(self.content)
        # return str(self.id)

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)

