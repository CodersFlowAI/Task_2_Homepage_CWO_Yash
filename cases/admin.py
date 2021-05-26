from django.contrib import admin
from cases.models import ReportAnonymously,Report

# Register your models here.
admin.site.register(ReportAnonymously)
admin.site.register(Report)