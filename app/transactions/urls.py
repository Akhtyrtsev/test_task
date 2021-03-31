from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    ]