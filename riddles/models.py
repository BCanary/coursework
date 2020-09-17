from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=25, default="No name")
	author = models.CharField(max_length=15, default="Anonymus")
	image_id = models.CharField(max_length=10, default="0")
	image_format = models.CharField(max_length=6, default="jpg")