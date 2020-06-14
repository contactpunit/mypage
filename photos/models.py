from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import random
import string


def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Photos(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='photos_photo')
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            unique=True,
                            default=generate_slug())
    caption = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              blank=False)

    def get_absolute_url(self):
        return reverse('photos:detail_photo',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return f'Photos uploaded by user {self.owner} with title {self.title}'
