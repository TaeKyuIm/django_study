from django.urls import path
from rest_framework import routers
from .views import BookAPI, BooksAPI, booksAPI, bookAPI, HelloAPI, BooksAPIMixins, BookAPIMixins, BookViewSet

# urlpatterns = [
#     path('hello/', HelloAPI),
#     path('fbv/books/', booksAPI), # 함수형 뷰의 연결
#     path('fbv/book/<int:bid>/', bookAPI),
#     path('cbv/books/', BooksAPI.as_view()),# 클래스형 뷰의 연결
#     # as_view()를 통해 주소를 직접 지정해주어야 했다.
#     path('cbv/book/<int:bid>/', BookAPI.as_view()),
#     path('mixin/books/', BooksAPIMixins.as_view()),
#     path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
# ]

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
