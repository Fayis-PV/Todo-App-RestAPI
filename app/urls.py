from django.urls import path
from . import views

# All urls here
urlpatterns = [
    #home url
    path('',views.index, name = 'home')
]
