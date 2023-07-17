from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('user/student/',StudentManagerViewSet.as_view(),name='Student operations'),
    path('admin/student/',StudentManagerViewSet.as_view(),name='Student operations by admin')

]