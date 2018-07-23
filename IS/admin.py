from django.contrib import admin

from IS.models import *


class GougingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gouging._meta.fields]


admin.site.register(Gouging, GougingAdmin)


class SurfacingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Surfacing._meta.fields]


admin.site.register(Surfacing, SurfacingAdmin)


class HeatTreatmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HeatTreatment._meta.fields]


admin.site.register(HeatTreatment, HeatTreatmentAdmin)


class MachiningAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Machining._meta.fields]


admin.site.register(Machining, MachiningAdmin)


class PrimaryTableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PrimaryTable._meta.fields]


admin.site.register(PrimaryTable, PrimaryTableAdmin)
