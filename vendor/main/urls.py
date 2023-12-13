from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewset, PerformanceViewset, PurchaseOrderViewset

router1 = DefaultRouter()
router2 = DefaultRouter()

router1.register("vendors", VendorViewset, basename="vendor")
router2.register("purchase_orders", PurchaseOrderViewset, basename="vendor")

urlpatterns = [
    path(
        "purchase_orders/<int:pk>/",
        PurchaseOrderViewset.as_view({"patch": "po_update"}),
        name="purchase-orders-update",
    ),
    path(
        "purchase_orders/details/<int:pk>/",
        PurchaseOrderViewset.as_view({"get": "po_details"}),
        name="purchase-orders-get",
    ),
    path(
        "purchase_orders/<int:pk>/acknowledge",
        VendorViewset.as_view({"patch": "acknowledgment"}),
        name="acknowledgment",
    ),
    path(
        "purchase_orders/<int:pk>/performance/",
        PerformanceViewset.as_view({"get": "performance"}),
        name="performance",
    ),
    path("", include(router1.urls)),
    path("", include(router2.urls)),
]
