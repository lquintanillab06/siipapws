
from rest_framework.pagination import PageNumberPagination, CursorPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class  CursorSetPagination(CursorPagination):
    page_size = 2
    ordering = 'id'
