from django.db import models


# Create your models here.
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    avg_response_time = models.FloatField(default=0)
    fullfilment_rate = models.FloatField(default=0)
    total_orders = models.IntegerField(default=0)
    on_time_delivery = models.IntegerField(default=0)
    fulfiled_rate = models.IntegerField(default=0)
    order_comleted = models.IntegerField(default=0)
    total_rating = models.FloatField(default=0.0)
    response_time = models.IntegerField(default=0)


class PurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, db_column="vendor_id"
    )
    order_date = models.DateField(auto_now=True)
    delivery_date = models.DateField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=15,
        choices=[
            ("pending", "pending"),
            ("completed", "completed"),
            ("canceled", "canceled"),
        ],
    )
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now=True)
    acknowledgement_date = models.DateTimeField(null=True)


class Performance(models.Model):
    vendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, db_column="vendor_id"
    )
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fullfillment_rate = models.FloatField(default=0.0)
