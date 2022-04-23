from django.db import models

class LocalNews(models.Model):
    name = models.CharField(max_length=50, default="")
    country_name = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=250, default="")
    content = models.TextField(default="")
    image_url = models.CharField(max_length=200, default="")
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.title