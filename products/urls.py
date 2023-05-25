from django.urls import path
from . import views

urlpatterns = [
	path('check_product/', views.check_product, name="check_product"),
	path('insert_product/', views.insert_product, name="insert_product")
]