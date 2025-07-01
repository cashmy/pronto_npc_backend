from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Archetype
from .serializers import ArchetypeSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@extend_schema(
    tags=["archetype"],
    summary="List or create archetypes",
    description="Handles listing all archetypes and creating a new one.",
    responses={
        200: ArchetypeSerializer(many=True),
        201: ArchetypeSerializer,
        400: {"description": "Bad Request - Invalid data provided."},
    },
)
def archetype_list(request):
    """Handles listing all archetypes and creating new ones.

    - **GET**: Retrieves a list of all `Archetype` objects.
    - **POST**: Creates a new `Archetype` instance.

    Args:
        request (Request): The incoming HTTP request.

    Returns:
        Response: A DRF Response object containing serialized data or errors.
    """
    if request.method == "GET":
        archetypes = Archetype.objects.all()
        serializer = ArchetypeSerializer(archetypes, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArchetypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
@extend_schema(
    tags=["archetype"],
    summary="Retrieve, update, or delete an archetype",
    description="Handles retrieving, updating, and deleting a single archetype by its primary key.",
    responses={
        200: ArchetypeSerializer,
        204: {"description": "No Content - Archetype successfully deleted."},
        400: {"description": "Bad Request - Invalid data provided."},
        404: {"description": "Not Found - Archetype with the given PK does not exist."},
    },
)
def archetype_detail(request, pk):
    """Handles retrieving, updating, and deleting a single archetype.

    Args:
        request (Request): The incoming HTTP request.
        pk (int): The primary key of the archetype to interact with.

    Returns:
        Response: A DRF Response object.
    """
    try:
        archetype = Archetype.objects.get(pk=pk)
    except Archetype.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArchetypeSerializer(archetype)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArchetypeSerializer(archetype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        archetype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = ArchetypeSerializer(archetype, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    tags=["archetype"],
    summary="List archetypes by expansion status",
    description="Returns a list of archetypes filtered by the 'expansion' flag. Use query parameter 'status' (e.g., ?status=true or ?status=false). Defaults to false if the parameter is missing or invalid.",
    responses={200: ArchetypeSerializer(many=True)},
)
def archetype_list_by_expansion(request):
    """Returns a list of archetypes filtered by the 'expansion' flag.

    This view uses the 'status' query parameter to filter archetypes.
    - `?status=true` returns archetypes where `expansion` is True.
    - `?status=false` returns archetypes where `expansion` is False.
    If the parameter is omitted or invalid, it defaults to `false`.

    Args:
        request (Request): The incoming HTTP request.

    Returns:
        Response: A DRF Response object containing the filtered list of archetypes.
    """
    # Get the 'status' query parameter, default to 'false' if missing/invalid
    expansion_status_str = request.query_params.get("status", "false").lower()

    # Convert string to boolean
    is_expansion = expansion_status_str == "true"

    # Filter based on the boolean status
    filtered_archetypes = Archetype.objects.filter(expansion=is_expansion)
    serializer = ArchetypeSerializer(filtered_archetypes, many=True)
    return Response(serializer.data)
