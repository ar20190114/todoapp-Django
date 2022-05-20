from django.urls import path, include
from .views import TodoList, TodoDetail, TodoUpdate, TodoCreate, TodoDelete

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('create/', TodoCreate.as_view(), name='create'),
]
