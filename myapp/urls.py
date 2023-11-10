from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSets

router=DefaultRouter()

router.register(r'items',ItemViewSets)

urlpatterns=[
    path('',include(router.urls))
]