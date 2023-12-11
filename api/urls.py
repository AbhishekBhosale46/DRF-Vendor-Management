from django.urls import path, include
from .views import VendorListCreate, VendorDetail, VendorPerformanceDetail, PurchaseOrderListCreate, PurchaseOrderDetail, acknowledgePurchaseOrder

urlpatterns = [
    path('vendors/', view=VendorListCreate.as_view()),
    path('vendors/<str:vendor_code>/', view=VendorDetail.as_view()),
    path('vendors/<str:vendor_code>/performance', view=VendorPerformanceDetail.as_view()),
    path('purchase_orders/', view=PurchaseOrderListCreate.as_view()),
    path('purchase_orders/<str:po_number>/', view=PurchaseOrderDetail.as_view()),
    path('purchase_orders<str:po_number>/acknowledge/', view=acknowledgePurchaseOrder),
]
