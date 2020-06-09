from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.CategoriaList.as_view(), name='categoria-list'),
]