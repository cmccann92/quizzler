from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]