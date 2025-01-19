from django.contrib import admin
from visits.models import VisitPage
# Register your models here.


@admin.register(VisitPage)
class VisitPageAdmin(admin.ModelAdmin):
    list_display = ["path", "timestamp"]
