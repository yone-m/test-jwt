from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'user'

router = routers.DefaultRouter()
router.register(r'create', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]