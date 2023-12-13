from rest_framework.serializers import ModelSerializer
from .models import Vendor, Performance, PurchaseOrder
from django.utils import timezone


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

    def create(self, validated_data):
        ven = Vendor.objects.create(**validated_data)
        Per = Performance.objects.create(vendor=ven, date=timezone.now())
        return ven


class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    def create(self, validated_data):
        order = PurchaseOrder.objects.create(**validated_data)
        ven = Vendor.objects.filter(
            vendor_id=validated_data["vendor"].vendor_id
        ).first()
        ven.total_orders += 1
        ven.save()
        return order


class PerformanceSerializer(ModelSerializer):
    class Meta:
        model = Performance
        fields = "__all__"
