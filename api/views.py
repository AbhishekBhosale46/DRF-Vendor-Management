from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import VendorSerializer, VendorPerformanceSerializer,PurchaseOrderSerializer
from core.models import Vendor, PurchaseOrder
from .utils import calculate_on_time_delivery_rate, calculate_quality_rating_average, calculate_fulfilment_rate, calculate_average_response_time

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'vendor_code'

class VendorPerformanceDetail(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'vendor_code'

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'

    def perform_update(self, serializer):

        instance = self.get_object()
        updated_instance = serializer.save()

        if 'status' in self.request.data :
            calculate_fulfilment_rate(instance.vendor.vendor_code)
        
        if 'status' in self.request.data and self.request.data['status'] == 'completed':
            calculate_on_time_delivery_rate(instance.vendor.vendor_code)
 
            if 'quality_rating' in self.request.data:
                calculate_quality_rating_average(instance.vendor.vendor_code)
        
        return updated_instance

@api_view(['POST'])
def acknowledgePurchaseOrder(request, po_number):
    po = PurchaseOrder.objects.get(po_number=po_number)
    po.acknowledgment_date = datetime.now()
    po.save()
    calculate_average_response_time(po.vendor.vendor_code)
    return Response(status=status.HTTP_200_OK)