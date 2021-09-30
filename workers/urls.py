from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import FieldWorkerViewSet


router = SimpleRouter()
router.register('', FieldWorkerViewSet, basename='field_workers')

app_name = 'workers'
urlpatterns = router.urls