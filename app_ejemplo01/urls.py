from django.urls import path
from . import views

urlpatterns = [
    path("ejemplo01/", views.index, name="index"),
    path("ejemplo01/<int:pk>/", views.detalle, name="detalle"),
]
