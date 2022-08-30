from django.urls import path
from .views import AnimalList, AnimalDetail

urlpatterns = [
    path('', AnimalList.as_view(), name='animal_list'),
    path('<int:pk>/', AnimalDetail.as_view(), name='animal_detail'),
]