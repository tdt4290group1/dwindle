from django.conf.urls import url
from django.contrib import admin

from .views import DiseaseListAPIView,MedicineListAPIView

urlpatterns=[
    url(r'^diseases', DiseaseListAPIView.as_view(),name = 'Diseases'),
    url(r'^medicine', MedicineListAPIView.as_view(),name = 'Medicines'),
    url(r'^', MedicineListAPIView.as_view(),name = 'Medicines'),
]