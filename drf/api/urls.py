from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')


urlpatterns = [
  path('students/',views.studentsview),
  path('students/<int:pk>/',views.studentDetailView),
  # path('employees/',views.Employees.as_view()), 
  path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
  path('',include(router.urls)),
  path('blogs/',views.BlogView.as_view()),
  path('comments/',views.commentsView.as_view()),
  path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
  path('comments/<int:pk>/',views.commentsDetailView.as_view())

]
  