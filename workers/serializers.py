from rest_framework import serializers
from .models import FieldWorker


class FieldWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name','function', 'created_at')
        model = FieldWorker