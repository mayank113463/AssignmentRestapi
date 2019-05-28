from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination

class MyPagination(PageNumberPagination):
    page_size = 10
    # page_query_param = 'page'
    page_size_query_param = 'limit'
