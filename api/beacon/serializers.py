from django.shortcuts import get_object_or_404
from rest_framework import serializers
from beacon.models import Time, Beacon, Signal

class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = ('uuid', 'rssi', )

class TimeSerializer(serializers.ModelSerializer):
    signals = SignalSerializer(many=True)

    class Meta:
        model = Time
        fields = ('user', 'beacon_total_number', 'signals', )

    def create(self, validated_data):
        signals_data = validated_data.pop('signals')
        time = Time.objects.create(**validated_data)
        for signal in signals_data:
            uuid = signal['uuid']
            beacon = get_object_or_404(Beacon, uuid=uuid)
            Signal.objects.create(time=time, beacon=beacon, **signal)
        return time
