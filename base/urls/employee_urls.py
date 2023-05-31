from django.urls import path
from base.views import employee_views as views


urlpatterns = [
    path('', views.getEmployees, name='employees'),
    path('add/', views.addEmployee, name='employees-add'),
]