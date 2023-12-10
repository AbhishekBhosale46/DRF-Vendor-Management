from rest_framework import serializers
from core.models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'name', 'contact_details', 'address']
        read_only_fields = ['vendor_code']

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']
        read_only_fields = ['vendor_code', 'on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['po_number', 'issue_date', 'acknowledgment_date']