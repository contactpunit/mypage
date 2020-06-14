from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Photos(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='photos_photo')
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    caption = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return f'Photos uploaded by user {self.owner}'
