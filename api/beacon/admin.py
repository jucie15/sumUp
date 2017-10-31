from django.contrib import admin
from beacon.models import Time, Beacon, Signal

class SignalInilne(admin.StackedInline):
    model = Signal

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    model = Time
    inlines = [
        SignalInilne,
    ]
    fields = ('created_at', 'user', 'beacon_total_number')

@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    model = Beacon

@admin.register(Signal)
class SignalAdmin(admin.ModelAdmin):
    model = Signal
