from django.conf.urls import url

from ..api import views

urlpatterns = [
    url(r'^diseases/$', views.DiseaseListAPIView.as_view(), name='Diseases'),
    url(r'^medicine/$', views.MedicineListAPIView.as_view(), name='Medicines'),
    url(r'^general-plan/$', views.GeneralPlanList.as_view(), name='general_plans'),
]
