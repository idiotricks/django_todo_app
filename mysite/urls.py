from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from todos.views import TodoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
urlpatterns += router.urls

