from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

##Edits
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Provider(models.Model):
    category = models.ForeignKey(Category)
    provider_name = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zipcode = models.CharField(max_length=128, blank=True)
    contact = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    hours = models.CharField(max_length=128, blank=True)
    
    def __str__(self):
        return self.provider_name