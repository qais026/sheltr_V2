from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
from django.contrib.gis.geos import GEOSGeometry
from .helpers import *

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
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Provider(models.Model):
    #Django automatically creates a primary key for a model
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
    notes = models.CharField(max_length=256, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    #location = models.PointField()
    location = models.PointField(null=False, blank=False, verbose_name="Location")
    objects = models.Manager()
    gis = models.GeoManager()


    def __str__(self):
        return self.provider_name

    ## Geocode using full address
    def _get_full_address(self):
        return u'%s %s %s %s %s %s' % (self.address_1, self.address_2, self.city, self.state, self.country, self.zipcode)
    full_address = property(_get_full_address)

    def save(self, *args, **kwargs):
        location = '+'.join(filter(None, (self.address1, self.address2, self.city, self.state, "USA")))
        lng = get_lng(location)
        lat = get_lat(location)
        print(get_lng_lat(location))
        inputloc = 'POINT('
        inputloc += lng
        inputloc += ' '
        inputloc += lat
        inputloc += ')'
        self.location = GEOSGeometry(inputloc, srid=3857)

        if not self.latlng:
            self.latlng = get_lat_lng(location)

        super(Provider, self).save(*args, **kwargs)