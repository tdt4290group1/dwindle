from rest_framework.serializers import ModelSerializer
from ..models import Medicine, Disease, PlanDosage,PatientTreatmentPlan

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['title']

class DiseaseSerializer(ModelSerializer):
    class Meta:
        models = Disease
        fields = ['title','medicines']

class PlanDosageSerializer(ModelSerializer):
    class Meta:
        models = PlanDosage
        fields = ['plan','offset','amount']

class PatientTreatmentPlanSerializer(ModelSerializer):
    class Meta:
        models = PatientTreatmentPlan
        fields = ['patient','author','start','comment','medicine','disease']

