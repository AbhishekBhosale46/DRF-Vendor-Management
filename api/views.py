from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime
from .serializers import VendorSerializer, VendorPerformanceSerializer,PurchaseOrderSerializer, HistoricalPerformanceSerializer, UserSerializer, AuthTokenserializer
from core.models import Vendor, PurchaseOrder, HistoricalPerformance
from .utils import calculate_on_time_delivery_rate, calculate_quality_rating_average, calculate_fulfilment_rate, calculate_average_response_time

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'vendor_code'

class VendorPerformanceDetail(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'vendor_code'

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def acknowledgePurchaseOrder(request, po_number):
    po = PurchaseOrder.objects.get(po_number=po_number)
    po.acknowledgment_date = datetime.now()
    po.save()
    calculate_average_response_time(po.vendor.vendor_code)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def recordVendorPerformance(request, vendor_code):
    vendor = Vendor.objects.get(vendor_code=vendor_code)
    historicalRecord = HistoricalPerformance.objects.create(
        vendor = vendor,
        date = datetime.now(),
        on_time_delivery_rate = vendor.on_time_delivery_rate,
        quality_rating_average = vendor.quality_rating_average,
        average_response_time = vendor.average_response_time,
        fulfillment_rate = vendor.fulfillment_rate
    )
    historicalRecord.save()
    return Response(status=status.HTTP_201_CREATED)

class HistoricalPerformanceList(generics.ListAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        vendor_code = self.kwargs['vendor_code']
        vendor = get_object_or_404(Vendor.objects.all(), vendor_code=vendor_code)
        return HistoricalPerformance.objects.filter(vendor=vendor)

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer  

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenserializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES