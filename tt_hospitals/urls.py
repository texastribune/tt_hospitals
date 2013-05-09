from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'v1/hospital/nearby/', views.NearbyHospitalApiView.as_view()),
)
