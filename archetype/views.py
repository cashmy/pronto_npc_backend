from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Archetype
from .serializers import ArchetypeSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def archetype_list(request):
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
def archetype_detail(request, pk):
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
def archetype_list_by_expansion(request):
    """
    Returns a list of archetypes filtered by the 'expansion' flag.
    Use query parameter 'status' (e.g., ?status=true or ?status=false).
    Defaults to false if the parameter is missing or invalid.
    """
    # Get the 'status' query parameter, default to 'false' if missing/invalid
    expansion_status_str = request.query_params.get("status", "false").lower()

    # Convert string to boolean
    is_expansion = expansion_status_str == "true"

    # Filter based on the boolean status
    filtered_archetypes = Archetype.objects.filter(expansion=is_expansion)
    serializer = ArchetypeSerializer(filtered_archetypes, many=True)
    return Response(serializer.data)
