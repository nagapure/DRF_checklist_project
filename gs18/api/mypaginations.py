from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# Below code is for pagenumber pagination
# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'p'
#     page_size_query_param = 'records'
#     max_page_size = 7


# Below code is for limit off set pagination
# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param= 'myoffset'
#     max_limit = 6


# Below code is for cursor pagination
class MyCursorPaginationPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
