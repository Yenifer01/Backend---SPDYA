# alimentos_app/urls.py
from django.urls import path
from .views import AlimentosListCreate, AlimentosRetrieveUpdateDestroy

urlpatterns = [
    path('alimentos', AlimentosListCreate.as_view(), name='alimentos-list-create'),
    path('alimentos/<int:pk>', AlimentosRetrieveUpdateDestroy.as_view(), name='alimentos-retrieve-update-destroy'),
]
