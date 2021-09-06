"""portifolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from portifolio.cadastro.views import Home, ClienteNew, ClienteUpdate, ClienteUpdateSlug, ClienteList, ClienteDelete

urlpatterns = [
    path('', Home),
    path('admin/', admin.site.urls),
    path('cliente/add', ClienteNew, name='url_cliente_new'),
    path('cliente/', ClienteList, name='url_cliente_list'),
    path('cliente/<int:pk>/', ClienteUpdate, name='url_cliente_update'),
    path('delete/<int:pk>/', ClienteDelete, name='url_cliente_delete'),
    path('cliente/<slug:slug>/', ClienteUpdateSlug, name='url_cliente_update'),
]
