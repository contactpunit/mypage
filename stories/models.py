from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from utils.utilities import generate_slug


class Story(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories_story')
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True, default=generate_slug())
    body = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = GenericRelation(Comment)

    def get_absolute_url(self):
        return reverse('stories:detail_story',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title} by {self.author}'
