from django.utils import timezone
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Vendor, Performance, PurchaseOrder
from .serializer import VendorSerializer, PerformanceSerializer, PurchaseOrderSerializer
from datetime import datetime


class VendorViewset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def vendor_list(self, request):
        """listing all vendors"""
        try:
            res = self.get_serializer(self.queryset)
            return Response(res.data)
        except Exception as e:
            return Response(str(e))

    def vendor_details(self, request, pk):
        """details of a vendor"""
        try:
            ven = self.queryset.filter(Vendor_id=pk)
            res = self.get_serializer(ven).data
            return Response(res)
        except Exception as e:
            return Response(str(e))

    def update_details(self, request, pk):
        """update vendor details"""
        try:
            ven = self.queryset.filter(Vendor_id=pk)
            res = self.get_serializer(ven, data=request.data, partial=True)
            if res.is_valid():
                res.save()
            return Response(res.data)
        except Exception as e:
            return Response(str(e))

    def delete(self, request, pk):
        """delete the vendor"""
        try:
            res = self.queryset.filter(task_id=pk).first()
            res.delete()
            return Response({"message": "Deleted"})
        except Exception as e:
            return Response(str(e))

    @action(detail=True, methods=(["PATCH"]))
    def acknowledgment(self, request, pk):
        """acknowledging the order"""
        try:
            product = PurchaseOrder.objects.filter(po_id=pk).first()
            cur_date = timezone.now()
            diff = (cur_date - product.issue_date).seconds
            ven = self.queryset.filter(vendor_id=product.vendor.vendor_id).first()
            ven.response_time += diff // 60
            ven.save()
            product.acknowledgement_date = cur_date
            product.save()
            return Response({"message": "success"})
        except Exception as e:
            return Response(str(e))


class PurchaseOrderViewset(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def po_list(self, request):
        """list all orders"""
        try:
            res = self.get_serializer(self.queryset)
            return Response(res.data)
        except Exception as e:
            return Response(str(e))

    @action(detail=True, methods=(["GET"]))
    def po_details(self, request, pk):
        """details of a order"""
        try:
            ven = self.queryset.filter(po_id=pk).first()
            res = self.get_serializer(ven).data
            return Response(res)
        except Exception as e:
            return Response(str(e))

    @action(detail=True, methods=(["PATCH"]))
    def po_update(self, request, pk):
        """update a order"""
        try:
            product = self.queryset.filter(po_id=pk).first()
            ven = Vendor.objects.filter(vendor_id=product.vendor.vendor_id).first()
            if "status" in request.data and request.data["status"] == "completed":
                ven.order_comleted += 1
            if "quality_rating" in request.data:
                ven.total_rating += request.data["quality_rating"]
            if "delivery_date" in request.data:
                if datetime.strptime(
                    request.data["delivery_date"], "%Y-%M-%d"
                ) <= datetime.strptime(str(product.delivery_date), "%Y-%M-%d"):
                    ven.on_time_delivery += 1
                    ven.save()
            res = self.get_serializer(product, data=request.data, partial=True)
            if res.is_valid():
                res.save()
            return Response(res.data)
        except Exception as e:
            return Response(str(e))

    def delete(self, request, pk):
        """delete a order"""
        try:
            res = self.queryset.filter(task_id=pk).first()
            res.delete()
            return Response({"message": "Deleted"})
        except Exception as e:
            return Response(str(e))


class PerformanceViewset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer

    @action(detail=True, methods=(["GET"]))
    def performance(self, request, pk):
        """return performance matrices of vendors"""
        try:
            ven = self.queryset.filter(vendor_id=pk).first()
            p = Performance.objects.filter(vendor=ven.vendor_id).first()
            if ven.total_orders > 0:
                art = ven.response_time / ven.total_orders
                qar = ven.total_rating / ven.total_orders
                fr = ven.order_comleted / ven.total_orders
                otdr = ven.on_time_delivery / ven.total_orders
                p.date = timezone.now()
                p.on_time_delivery_rate = otdr
                p.quality_rating_avg = qar
                p.average_response_time = art
                p.fullfillment_rate = fr
                p.save()
            return Response(self.get_serializer(p).data)
        except Exception as e:
            return Response(str(e))
