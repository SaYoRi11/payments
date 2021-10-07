from django.urls import path, include
from .views import CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('card', CardViewSet, basename='card')

urlpatterns = [
    path('api/', include(router.urls))
]