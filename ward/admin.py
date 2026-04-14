from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'illness', 'prescription', 'bill_balance', 'bill_status']
    list_filter = ['bill_balance']
    search_fields = ['name', 'illness']

    def bill_status(self, obj):
        if obj.bill_balance > 0:
            return 'Owes money'
        return "Cleared"
    bill_status.short_description = 'Bill Status'