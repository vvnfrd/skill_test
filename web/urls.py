from web.apps import WebConfig
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from web.views import ProductViewSet, SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, \
    SupplierUpdateAPIView, SupplierDestroyAPIView

app_name = WebConfig.name

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
                  path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier-create'),
                  path('supplier/', SupplierListAPIView.as_view(), name='supplier-list'),
                  path('supplier/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier-retrieve'),
                  path('supplier/update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier-update'),
                  path('supplier/destroy/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier-destroy'),
              ] + router.urls
