from django.urls import path, include
from . import views 

urlpatterns = [
    path('vendors/', view=views.VendorListCreate.as_view()),
    path('vendors/<str:vendor_code>/', view=views.VendorDetail.as_view()),
    path('vendors/<str:vendor_code>/performance', view=views.VendorPerformanceDetail.as_view()),
    path('vendors/<str:vendor_code>/recordperformance', view=views.recordVendorPerformance),
    path('vendors/<str:vendor_code>/historicalperformance', view=views.HistoricalPerformanceList.as_view()),
    path('purchase_orders/', view=views.PurchaseOrderListCreate.as_view()),
    path('purchase_orders/<str:po_number>/', view=views.PurchaseOrderDetail.as_view()),
    path('purchase_orders<str:po_number>/acknowledge/', view=views.acknowledgePurchaseOrder),
    path('user/create', view=views.CreateUserView.as_view()),
    path('user/token/', view=views.CreateTokenView.as_view()),
]
