from rest_framework import serializers
from .models import Waste

# class ControlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Control
#         fields = '__all__'

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ['name','battery_percent','occupied_percent','ref']

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.occupied_percent = validated_data.get('occupied_percent', instance.occupied_percent)
        instance.battery_percent = validated_data.get('battery_percent', instance.battery_percent)
        instance.save()
        return instance