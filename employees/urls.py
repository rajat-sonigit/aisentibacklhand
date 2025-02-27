# from django.urls import path
# from .views import employee_directory

# urlpatterns = [
#     path('employees/', employee_directory, name='employee_directory'),
# ]

from django.urls import path
from .views import add_employee, employee_directory

urlpatterns = [
    path("", employee_directory, name="employee_directory"),  # No need for "employees/" again
     path('add/', add_employee, name='add_employee'),
]
