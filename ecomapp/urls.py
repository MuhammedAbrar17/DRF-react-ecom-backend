from ecomapp import views
from django.urls import path

urlpatterns = [
    path('api/',views.getRoutes,name="getRoutes"),
]