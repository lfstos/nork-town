from django.urls import path
from . import views


urlpatterns = [
    path('owner/', views.OwnerListCreateView.as_view(), name='owner-list-create'),
    path('owner/<int:pk>/', views.OwnerRetrieveUpdateDestroyView.as_view(), name='owner-retrieve-update-destroy'),
    path('cars/', views.CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', views.CarRetrieveUpdateDestroyView.as_view(), name='car-retrieve-update-destroy'),
]
