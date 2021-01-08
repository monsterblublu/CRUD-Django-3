from django.db import models
from django.urls import reverse

# Create your models here.
class Mahasiswa(models.Model):
    name = models.CharField(max_length=40)
    nisn = models.PositiveIntegerField()
    nis = models.PositiveIntegerField()
    address = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='profile')
    quote_me = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mahasiswa_detail',kwargs={'pk':self.pk})


