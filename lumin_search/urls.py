"""lumin_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from hello import views
from django.urls import path
from hello import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.gene),
    path('admin/', admin.site.urls),
    path('gene/', views.gene, name='gene'),
    path('insert/', views.insert, name='register'),
    path('gene_upload/', views.gene_upload, name='gene_upload'),
    path('delete_gene/', views.delete_gene,name='delete_gene'),
]
