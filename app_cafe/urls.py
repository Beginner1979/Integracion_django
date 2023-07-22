"""
URL configuration for remerashop project.

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

from django.urls import path
from .router import router
from .views import CafeListView  ,\
                   CafeDetailView,\
                   CafeUpdateView,\
                   CafeDeleteView,\
                   CafeCreateView

app_name = "cafe"
urlpatterns = [

    path("", CafeListView.as_view(), name = "all"),
    path("<int:pk>/detail/", CafeDetailView.as_view(), name = "detail"),
    path("<int:pk>/update/", CafeUpdateView.as_view(), name = "update"),
    path("<int:pk>/delete/", CafeDeleteView.as_view(), name = "delete"),
    path("create/", CafeCreateView.as_view(), name = "create"),
   
]
urlpatterns += router.urls