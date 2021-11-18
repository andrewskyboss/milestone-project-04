from django.db import models

# Create your models here.


class Role(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Employee(models.Model):
    role = models.ForeignKey(
        'Role', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    start_date = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    qualifications = models.TextField(max_length=1024, null=True, blank=True)
    interests = models.TextField(max_length=1024, null=True, blank=True)
    more = models.TextField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
