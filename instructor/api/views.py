from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView

from instructor.api.serializers import DiseaseSerializer, MedicineSerializer, PatientTreatmentPlanSerializer, PlanSerializer
from instructor.models import Disease, Medicine, PatientTreatmentPlan, Plan


class DiseaseListAPIView(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class MedicineListAPIView(ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PatientTreatmentPlanListAPIView(ListAPIView):
    queryset = PatientTreatmentPlan.objects.all()
    serializer_class = PatientTreatmentPlanSerializer


class PatientTreatmentPlanDetailedView(RetrieveAPIView, ):
    queryset = PatientTreatmentPlan.objects


class GeneralPlanList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
