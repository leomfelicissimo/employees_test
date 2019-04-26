from api.models import Department, Employee
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    email = serializers.EmailField()
    department_id = serializers.IntegerField()

    def create(self, validated_data):
        print('validated_data', validated_data)
        dpk = validated_data.get('department_id')
        dp = Department.objects.get(pk=dpk)
        emp_name = validated_data.get('name')
        emp_email = validated_data.get('email')
        emp_dep = Department.objects.get(pk=dpk)
        emp = Employee(emp_name, emp_email, emp_dep)
        return emp.save()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('email', instance.department)
        instace.save()
        return instance