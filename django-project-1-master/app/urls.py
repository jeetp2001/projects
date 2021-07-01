from django.urls import path

from . import views

urlpatterns = [
    path('',views.user),
    path('display',views.display)
]