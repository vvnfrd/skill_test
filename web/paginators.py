from rest_framework.pagination import PageNumberPagination


class SupplierPaginator(PageNumberPagination):
    """ Пагинация поставщиков """

    page_size = 10
