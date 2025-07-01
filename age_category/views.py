from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import AgeCategory
from .serializers import AgeCategorySerializer, AgeCategoryOptionSerializer


@extend_schema(
    tags=["age_category"],
    summary="Manage Age Categories",
    description="Provides standard CRUD operations for age categories.",
)
class AgeCategoryViewSet(viewsets.ModelViewSet):
    """A ViewSet for managing AgeCategory instances.

    This ViewSet provides the standard `list`, `create`, `retrieve`, `update`,
    and `destroy` actions for the AgeCategory model. It ensures that users
    are authenticated to perform any action.
    """

    queryset = AgeCategory.objects.all().order_by("age_category_name")
    serializer_class = AgeCategorySerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    tags=["age_category"],
    summary="Get Age Category Options",
    description="Provides a simplified list of age categories for UI dropdowns.",
    responses=AgeCategoryOptionSerializer(many=True),
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def age_category_options(request):
    """Provides a simplified list of age categories for UI dropdowns.

    This endpoint returns a lightweight list of age categories, containing only
    the `id` and `value` (name), suitable for populating select/option lists
    in a frontend application.

    Args:
        request: The Django REST Framework request object.

    Returns:
        A Response object containing a list of serialized age category options.
    """
    categories = AgeCategory.objects.all().order_by("age_category_name")
    serializer = AgeCategoryOptionSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
