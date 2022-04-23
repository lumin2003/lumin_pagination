import django_tables2 as tables
from .models import PatientInfo
import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse


class PatientInfoTable(tables.Table):

    class Meta:
        model = PatientInfo
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "classify","age","phenotype","numbers","size","location","migration")
