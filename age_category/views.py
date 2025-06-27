from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import AgeCategory
from .serializers import AgeCategorySerializer, AgeCategoryOptionSerializer


class AgeCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows age categories to be viewed or edited.
    Provides list, create, retrieve, update, partial_update, and destroy actions.
    """

    queryset = AgeCategory.objects.all().order_by("age_category_name")
    serializer_class = AgeCategorySerializer
    permission_classes = [IsAuthenticated]


# Optional: Serializer for the dropdown options in the frontend
# This can remain as a function-based view if it serves a distinct, simpler purpose.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def age_category_options(request):
    """
    Provides a simplified list of age categories (id and name)
    suitable for populating dropdown/select options in a frontend.
    """
    categories = AgeCategory.objects.all().order_by(
        "age_category_name"
    )  # optional ordering
    serializer = AgeCategoryOptionSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
