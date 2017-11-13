from django.shortcuts import get_object_or_404
from django.db import transaction
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
        fields = ('created_at', 'user', 'beacon_total_number', 'signals', )
        extra_kwargs = {'created_at': {'read_only': True}}

    def create(self, validated_data):
        signals_data = validated_data.pop('signals')
        with transaction.atomic():
            # transaction all or nothing
            time = Time.objects.create(**validated_data)
            for signal in signals_data:
                uuid = signal['uuid']
                beacon, created = Beacon.objects.get_or_create(uuid=uuid)
                Signal.objects.create(time=time, beacon=beacon, **signal)
            return time
