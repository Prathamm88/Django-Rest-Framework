from . import views
from django.urls import path


urlpatterns = [
  path('students/', views.student_list, name='student-list'),
  path('students/<int:pk>/', views.student_detail, name='student-detail'),

]