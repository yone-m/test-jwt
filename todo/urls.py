from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'todo'

router = routers.DefaultRouter()
router.register(r'all', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
]