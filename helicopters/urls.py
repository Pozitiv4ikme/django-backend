from django.urls import path
from helicopters import views

urlpatterns = [
    path("helicopters", views.HelicoptersListCreateAPIView.as_view()),
    path("helicopters/<pk>", views.HelicopterRetrieveUpdateDeleteAPIView.as_view())
]