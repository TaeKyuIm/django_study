from django.urls import path
from .views import TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()), # cbv 이므로 as_view()필요
    path('todo/<int:pk>/', TodoAPIView.as_view()),
    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),
]