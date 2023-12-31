"""
URL configuration for crud_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from crud_blog_web.views import test_response
from crud_blog_web.views import all_articles
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
    path('crud-blog/', include("crud_blog_web.urls")),
    path('templates/', all_articles),
]
