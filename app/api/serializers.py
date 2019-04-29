from api.models import Department, Employee
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)
    description = serializers.CharField(max_length=64)

    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

    # def create(self, validated_data):
    #     return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    email = serializers.EmailField()
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')