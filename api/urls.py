from django.urls import path, include
from .views import VendorListCreate, VendorDetail, VendorPerformanceDetail, PurchaseOrderListCreate, PurchaseOrderDetail, acknowledgePurchaseOrder

urlpatterns = [
    path('vendors/', view=VendorListCreate.as_view()),
    path('vendors/<uuid:vendor_id>/', view=VendorDetail.as_view()),
    path('vendors/<uuid:vendor_id>/performance', view=VendorPerformanceDetail.as_view()),
    path('purchase_orders/', view=PurchaseOrderListCreate.as_view()),
    path('purchase_orders/<uuid:po_id>/', view=PurchaseOrderDetail.as_view()),
    path('purchase_orders<uuid:po_id>/acknowledge/', view=acknowledgePurchaseOrder),
]
