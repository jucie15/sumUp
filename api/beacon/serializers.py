from rest_framework import serializers
from beacon.models import Time, Beacon, Signal

class BeaconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beacon
        fields = ('uuid', )

class SignalSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(write_only=True)

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
            uuid = signal.pop('uuid')
            beacon = Beacon.objects.get(uuid=uuid)
            Signal.objects.create(time=time, beacon=beacon, **signal)
        return time
