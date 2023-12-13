from django.contrib import admin
from .models import Vendor, Performance, PurchaseOrder


class VendorAdmin(admin.ModelAdmin):
    readonly_fields = [
        "on_time_delivery_rate",
        "quality_rating_avg",
        "avg_response_time",
        "fullfilment_rate",
        "total_orders",
        "on_time_delivery",
        "fulfiled_rate",
        "order_comleted",
        "total_rating",
        "response_time",
    ]


class PurchaseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ["acknowledgement_date", "order_date"]


class PerformanceAdmin(admin.ModelAdmin):
    readonly_fields = [
        "vendor",
        "date",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fullfillment_rate",
    ]


admin.site.register(Vendor, VendorAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
# Register your models here.
