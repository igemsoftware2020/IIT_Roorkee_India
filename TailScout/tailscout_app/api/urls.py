from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')
urlpatterns = router.urls
