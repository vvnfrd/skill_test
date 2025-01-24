from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from users.permissions import IsActiveAuthenticated
from web.models import Product, Supplier
from web.paginators import SupplierPaginator
from web.serializers import ProductSerializer, SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet продукта """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveAuthenticated]


class SupplierCreateAPIView(generics.CreateAPIView):
    """ APIView создания поставщиков """

    serializer_class = SupplierSerializer
    permission_classes = [IsActiveAuthenticated]


class SupplierListAPIView(generics.ListAPIView):
    """ APIView вывода списка поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['city']
    permission_classes = [IsActiveAuthenticated]
    pagination_class = SupplierPaginator


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """ APIView подробной информации поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveAuthenticated]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """ APIView обновления поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveAuthenticated]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """ APIView удаления поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveAuthenticated]
