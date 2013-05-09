import csv
import os

from django.core.management.base import NoArgsCommand
from django.contrib.gis.geos import Point

from ... import models


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **kwargs):
        with open(os.environ['DATA_FILE']) as f:
            reader = csv.reader(f)
            legend = reader.next()
            for row_values in reader:
                row = dict(zip(legend, row_values))
                month, day, year = row['Orig Date'].split('/')
                models.Hospital.objects.get_or_create(
                    file_nbr=row['File Nbr'],
                    license_number=row['LIC#'],
                    name=row['Name'],
                    address=row['Selected Address'],
                    city=row['City'],
                    state=row['St'],
                    zipcode=int(row['Zip']),
                    coordinates=Point(float(row['Lat']), float(row['Lng'])),
                    county=row['County'],
                    phone=row['Phone'],
                    status=row['Status'],
                    original_date='%s-%s-%s' % (year, month, day)
                )
