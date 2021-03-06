from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from beacon.models import Time, Beacon, Signal

class SignalInilne(admin.StackedInline):
    model = Signal

@admin.register(Time)
class TimeAdmin(ImportExportModelAdmin):
    model = Time
    inlines = [
        SignalInilne,
    ]
    readonly_fields = ('created_at',)
    fields = ('created_at', 'user', 'beacon_total_number')

@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    model = Beacon

@admin.register(Signal)
class SignalAdmin(ImportExportModelAdmin):
    model = Signal
