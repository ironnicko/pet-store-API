from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from be import views

urlpatterns = [
    path('pets/', views.PetsList.as_view()),
    path('pets/<int:pk>/', views.PetsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)