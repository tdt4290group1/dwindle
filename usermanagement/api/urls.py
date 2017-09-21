from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ..api import views

urlpatterns = [
    url(r'^patient/$', views.PatientList.as_view()),
    url(r'^employee/$', views.EmployeeList.as_view()),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
