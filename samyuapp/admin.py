from django.contrib import admin
from .models import Praveen

from samyuapp.models import Praveen


class PraveenAdmin(admin.ModelAdmin):
    pass


admin.site.register(Praveen, PraveenAdmin)
