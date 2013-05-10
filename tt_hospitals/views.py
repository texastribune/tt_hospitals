from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


from tx_schools.api import ApiView, JSON
from . import models


class NearbyHospitalApiView(ApiView):
    def get_json(self, data):
        response = super(NearbyHospitalApiView, self).get_json(data)
        if 'callback' in self.request.GET:
            response.content = '%s(%s)' % (self.request.GET['callback'],
                    response.content)
        return response

    def get_content_data(self):
        point = Point(float(self.request.GET['lat']),
                float(self.request.GET['lng']))
        distance = self.request.GET.get('distance', 5)
        nearby = models.Hospital.objects.distance(point).filter(
                coordinates__distance_lte=(point, D(mi=distance)))

        data = []
        for hospital in nearby:
            data.append({
                'name': unicode(hospital.name),
                'distance': round(hospital.distance.mi, 2),
                'geojson': JSON(hospital.coordinates.geojson),
            })
        return data
