from django.contrib import admin
from django.urls import path

from .views import ProdutoViewSet

urlpatterns = [
    path('produtos', ProdutoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('produtos/<str:pk>', ProdutoViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'delete',
        })),
]
