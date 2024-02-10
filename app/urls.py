from django.urls import path
from . import views

# All urls here
urlpatterns = [
    #home url
    path('',views.TodoListView.as_view() , name = 'home')
]
