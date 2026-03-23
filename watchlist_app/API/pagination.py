from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination 

class WatchListPaginaation(PageNumberPagination):
    
    page_size = 5
    page_query_param ='p'
    page_size_query_param='size'
    max_page_size=7
    last_page_strings="end" 
    
class WatchListLOPaginaation(LimitOffsetPagination):
    default_limit=5
    max_limit=10
    limit_query_param='limit'
    offset_query_param='start'
    
# class WatchListCPaginaation(CursorPagination):
#     page_size=5