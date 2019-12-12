from django.urls import path
from .views import all_transfers

urlpatterns = [
    path('transfers/', all_transfers),
]