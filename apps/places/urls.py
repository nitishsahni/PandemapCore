from django.urls import path
from . import views

urlpatterns = [
    path('students_list', views.places_list, name='students_list'),
    path('student_detail/<int:pk>', views.place_detail, name='student_detail'),
    path('students_list', views.intervals_list, name='students_list'),
    path('student_detail/<int:pk>', views.interval_detail, name='student_detail'),
]