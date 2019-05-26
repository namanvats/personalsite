from django.db import models

# Create your models here.


class Quotes(models.Model):
    content = models.TextField(max_length=1001)
