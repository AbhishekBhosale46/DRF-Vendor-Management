from django.db import models
import uuid

class Vendor(models.Model):
    vendor_code = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_average = models.FloatField(default=0) 
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vendor_code} {self.name}"

class PurchaseOrder(models.Model):
    po_number = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.po_number}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_average = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)