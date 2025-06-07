from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employee',views.EmployeeViewset)

urlpatterns = [
    path('studend/',views.StudentView,name = 'StudentView' ),
    path('studend/<int:pk>/',views.studentAction,name = 'studentAction' ),
    
    # path('employee/',views.EmployeeList.as_view(),name = 'employeeList' ),
    # path('employee/<int:pk>',views.EmployeeACtions.as_view(),name = 'employeeACtions' ),
 
    path('',include(router.urls))
]