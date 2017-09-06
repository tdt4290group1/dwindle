from django.contrib import admin

from .models import Medicine, PatientTreatmentPlan, Disease, Medium, Plan, PlanDosage, UserDose


class PlanDosageInline(admin.TabularInline):
    model = PlanDosage


class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanDosageInline, ]


admin.site.register(Medicine)
admin.site.register(PatientTreatmentPlan)
admin.site.register(Disease)
admin.site.register(Medium)
admin.site.register(Plan, PlanAdmin)

admin.site.register(UserDose)
