from django.urls import path
from . import views

urlpatterns = [
    path('studend/',views.StudentView,name = 'StudentView' ),
    path('studend/<int:pk>/',views.studentAction,name = 'studentAction' ),
    
    path('employee/',views.EmployeeList.as_view(),name = 'employeeList' ),
    path('employee/<int:pk>',views.EmployeeACtions.as_view(),name = 'employeeACtions' ),


]