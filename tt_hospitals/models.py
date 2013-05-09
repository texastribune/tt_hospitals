from django.contrib.gis.db import models


class Hospital(models.Model):
    file_nbr = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.PositiveIntegerField()
    latitude = models.PointField()
    longitude = models.PointField()
    phone = models.CharField(max_length=250)
    status = models.CharField(max_length=20)  # TODO: Investigate, boolean?
    original_date = models.DateField()

    # TODO: denormalize these fields
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=2, default='TX')
    county = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.city)
