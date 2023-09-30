from django.urls import path
from . import views

urlpatterns = [
    path("", views.default),
    path("<int:num>", views.calculate),
    path("taxrate", views.tax_rate),
]