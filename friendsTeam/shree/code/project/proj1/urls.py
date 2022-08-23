from django.contrib import admin
from django.urls import path,is_valid_path,include
from .  import views
from .views import orderview,customerview,addressview
from rest_framework import routers


router = routers.DefaultRouter()
router.register('address',views.addressview)
router.register('customer',views.customerview)
router.register('order',views.orderview)

urlpatterns = [
    path('',include(router.urls)),
]
