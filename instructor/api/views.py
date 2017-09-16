from rest_framework.generics import ListAPIView,RetrieveAPIView

from instructor.models import Disease, Medicine,PatientTreatmentPlan
from instructor.api.serializers import DiseaseSerializer,MedicineSerializer,PatientTreatmentPlanSerializer


class DiseaseListAPIView(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class MedicineListAPIView(ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class PatientTreatmentPlanListAPIView(ListAPIView):
    queryset = PatientTreatmentPlan.objects.all()
    serializer_class = PatientTreatmentPlanSerializer

class PatientTreatmentPlanDetailedView(RetrieveAPIView,):
    queryset = PatientTreatmentPlan.objects