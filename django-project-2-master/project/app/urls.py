from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('login',views.login),
	path('display',views.display),
	path('register',views.register),
	path('registered',views.registered),
	path('<int:id>',views.edit,name='edit'),
	path('delete/<int:id>',views.delete,name='delete'),
	path('edited',views.edited)
]
