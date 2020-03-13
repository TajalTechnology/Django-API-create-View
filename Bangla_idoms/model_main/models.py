from django.db import models


# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        self.name

    class Meta:
        abstract = True


class Division(Common):

    pass


class District(Common):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    lat = models.CharField(max_length=200, default=None, null=True)
    lon = models.CharField(max_length=200, default=None, null=True)
    pass


class Category(Common):
    pass


class ChandaKatha(Common):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
