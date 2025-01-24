from rest_framework.pagination import PageNumberPagination


class SupplierPaginator(PageNumberPagination):
    page_size = 10
