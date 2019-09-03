from rest_framework import serializers
from main.models import Main

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['id', 'created', 'exception_type', 'exception_string', 'exception_repr', 'exception_args', 'exception_traceback']