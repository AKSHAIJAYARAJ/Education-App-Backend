from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/course/',CourseManagerViewSet.as_view(),name='Course operations by admin'),
    path('user/student/course/',UserCourseDetailsViewSet.as_view(),name='Student operations by admin')

]