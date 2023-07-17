from rest_framework.pagination import PageNumberPagination

class PaginatedView(PageNumberPagination):

    page_size = 10  # Number of instances to display per page
    page_size_query_param = 'page_size'
    max_page_size = 100