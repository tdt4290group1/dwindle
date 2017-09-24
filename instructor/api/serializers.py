from rest_framework import serializers

from ..models import Medicine, Disease, PlanDosage, PatientTreatmentPlan, Plan


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['title']


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['title', 'medicines']


class PatientTreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTreatmentPlan
        fields = ['patient', 'author', 'start', 'comment', 'medicine', 'disease']


class DosePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDosage
        fields = ('offset', 'amount')


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    dosages = DosePlanSerializer(many=True)
    view_name = 'instructor:share-root'

    class Meta:
        model = Plan
        fields = ('title', 'comment', 'dosages',)

    def create(self, validated_data):
        # Pop external model "dosages" data
        dosages = validated_data.pop('dosages')

        # Create a plan with current data
        plan = Plan.objects.create(**validated_data)

        # For each dosage (1 for each day): Create it with a FK to the newly created plan
        for dose_data in dosages:
            PlanDosage.objects.create(plan=plan, **dose_data)
        return plan
