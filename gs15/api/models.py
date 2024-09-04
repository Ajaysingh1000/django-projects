from django.db import models
from django.utils.translation import gettext_lazy as _  # Import for the translation

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    passby = models.CharField(max_length=100)
    file_upload = models.FileField(_("PDF"), upload_to='uploads/', max_length=100 , blank=True)

    def __str__(self):
        return self.name
