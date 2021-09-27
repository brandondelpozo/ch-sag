from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework import mixins

from .models import FieldWorker
from .serializers import FieldWorkerSerializer

class FieldWorkerViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer