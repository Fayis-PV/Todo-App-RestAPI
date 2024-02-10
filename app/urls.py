from django.urls import path
from .views import *

# All urls here
urlpatterns = [
    #home url
    path('',TodoListView.as_view() , name = 'home'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name = 'todo_detail'),

]
