from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('user/application/',ApplicationManagerViewSet.as_view(),name='Application operations by user'),
    path('admin/application/',ApplicationManagerViewSet.as_view(),name='Application operations by admin')

]