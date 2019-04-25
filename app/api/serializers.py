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
    department = serializers.ModelField(model_field='department')