import django_filters
from .models import Employee




class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name = 'designation', lookup_expr = 'icontains')
    emp_name = django_filters.CharFilter(field_name = 'emp_name', lookup_expr = 'icontains')
    id = django_filters.RangeFilter(field_name = 'id',label='ID')

    class Meta:
        model = Employee    
        fields = ['designation','emp_name','id'] 


        