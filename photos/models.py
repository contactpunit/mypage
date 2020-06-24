from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from utils.utilities import generate_slug
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from catagories.models import Categories


class Photos(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='photos_photo')
    categoryid = models.ForeignKey(Categories, on_delete=models.CASCADE,
                                   related_name='category_photo')
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
    comments = GenericRelation(Comment)

    def get_absolute_url(self):
        return reverse('photos:detail_photo',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'Photos uploaded by user {self.owner} with title {self.title}'
