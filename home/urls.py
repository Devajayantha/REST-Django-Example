from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('inventory', views.InventoryView)

urlpatterns = [
    path('home/', include(router.urls))
]