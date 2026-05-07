from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tours.views import TourViewSet

router = routers.DefaultRouter()
router.register(r'tours', TourViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]