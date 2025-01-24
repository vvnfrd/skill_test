from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from web.models import Product, Supplier
from web.serializers import ProductSerializer, SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['city']


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()