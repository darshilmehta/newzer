from django.db import models
from django.contrib.postgres.fields import ArrayField

class News(models.Model):
    country_name = models.CharField(max_length=200, default="")
    newspaper_name = models.CharField(max_length=200, default="")
    title = models.TextField(default="")
    summary = models.TextField(default="")
    post_url = models.CharField(max_length=200, default="")
    image_url = models.CharField(max_length=200, default="")
    sentiment = models.FloatField(blank=False)
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    authors = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return self.title