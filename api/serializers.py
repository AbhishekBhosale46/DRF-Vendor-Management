from rest_framework import serializers
from core.models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'name', 'contact_details', 'address']

    def update(self, instance, validated_data):
        if 'vendor_code' in validated_data:
            if not instance.vendor_code == validated_data['vendor_code']:
                raise serializers.ValidationError({'vendor_code': 'You cannot change this field'})
        return super().update(instance, validated_data) 

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']
        read_only_fields = ['on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['issue_date', 'acknowledgment_date']
    
    def update(self, instance, validated_data):
        if 'po_number' in validated_data:
            if not instance.po_number == validated_data['po_number']:
                raise serializers.ValidationError({'po_number': 'You cannot change this field'})
        return super().update(instance, validated_data) 

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'