from django.contrib import admin
from django.urls import path
from aplicacao.views import apiProdutos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apiProdutos/", apiProdutos ), 
]
