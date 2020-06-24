from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=120)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return f'Lists categories of applications served {self.category}'
