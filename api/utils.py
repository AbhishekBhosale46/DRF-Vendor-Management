from core import models 
from django.db.models import F, Avg

def calculate_on_time_delivery_rate(vendor_code):
    pos = models.PurchaseOrder.objects.filter(vendor=vendor_code)
    completed_pos = pos.filter(status='completed')
    on_time_completed_pos = completed_pos.filter(actual_delivery_date__lte=F('expected_delivery_date'))
    new_on_time_delivery_rate = on_time_completed_pos.count()/completed_pos.count()
    vendor = models.Vendor.objects.get(vendor_code=vendor_code)
    vendor.on_time_delivery_rate = new_on_time_delivery_rate
    vendor.save() 

def calculate_quality_rating_average(vendor_code):
    pos = models.PurchaseOrder.objects.filter(vendor=vendor_code)
    completed_pos = pos.filter(status='completed').exclude(quality_rating__isnull=True)
    new_quality_rating_average = completed_pos.aggregate(Avg('quality_rating'))
    vendor = models.Vendor.objects.get(vendor_code=vendor_code)
    vendor.quality_rating_average = new_quality_rating_average['quality_rating__avg']
    vendor.save()

def calculate_fulfilment_rate(vendor_code):
    pos = models.PurchaseOrder.objects.filter(vendor=vendor_code)
    completed_pos = pos.filter(status='completed')
    new_fulfilment_rate = completed_pos.count()/pos.count()
    vendor = models.Vendor.objects.get(vendor_code=vendor_code)
    vendor.fulfillment_rate = new_fulfilment_rate
    vendor.save()

def calculate_average_response_time(vendor_code):
    pos = models.PurchaseOrder.objects.filter(vendor=vendor_code)
    acknowledged_pos = pos.exclude(acknowledgment_date__isnull=True)
    time_diff_seconds = F('acknowledgment_date')-F('issue_date')
    new_avg_response_time = acknowledged_pos.aggregate(avg_response_time=Avg(time_diff_seconds))['avg_response_time']
    new_avg_response_time = new_avg_response_time.total_seconds()/ (60 * 60) if new_avg_response_time else 0
    vendor = models.Vendor.objects.get(vendor_code=vendor_code)
    vendor.average_response_time = new_avg_response_time
    vendor.save()