from api.models import Department, Employee
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    email = serializers.EmailField()
    department = DepartmentSerializer()

    def create(self, validated_data):
        dpk = validated_data['department_id']
        emp = Employee()
        emp.name = validated_data['name']
        emp.email = validated_data['email']
        emp.departament = Department.objects.get(pk=dpk)
        emp.save()
        return emp

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('email', instance.department)
        instace.save()
        return instance