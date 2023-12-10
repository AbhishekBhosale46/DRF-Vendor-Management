from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .serializers import VendorSerializer, VendorPerformanceSerializer,PurchaseOrderSerializer
from core.models import Vendor, PurchaseOrder

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceDetail(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

@api_view(['POST'])
def acknowledgePurchaseOrder(request, po_id):
    po = PurchaseOrder.objects.get(po_number=po_id)
    po.acknowledgment_date = datetime.now()
    po.save()