# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.db.models import Q
# from .models import Employee
# from .serializers import EmployeeSerializer

# @api_view(['GET'])
# def employee_directory(request):
#     """
#     API to fetch employee directory with optional filtering.
#     """
#     query = request.GET.get('query', '')  # Search query for name, department, or position
#     employees = Employee.objects.all()

#     if query:
#         employees = employees.filter(
#             Q(name__icontains=query) |
#             Q(department__icontains=query) |
#             Q(position__icontains=query)
#         )

#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(["GET"])
def employee_directory(request):
    """
    API to fetch employee directory with optional filtering.
    """
    query = request.GET.get("query", "")  # Search query for name, department, or position
    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(department__icontains=query) |
            Q(position__icontains=query)
        )

    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_employee(request):
    """
    API to add a new employee.
    """
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
