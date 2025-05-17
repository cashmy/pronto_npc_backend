from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Use . for relative import

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(
    r"", views.AgeCategoryViewSet, basename="agecategory"
)  # Empty string for base path

urlpatterns = [
    path("options/", views.age_category_options, name="age_category_options"),
    # The API URLs are now determined automatically by the router.
    path("", include(router.urls)),
]
