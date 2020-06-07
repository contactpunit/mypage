from django.db import models
from stories.models import Story


class Comment(models.Model):
    story = models.ForeignKey(Story,
                              on_delete=models.CASCADE,
                              related_name='storycomments'
                              )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment from {self.email} on {self.created}'
