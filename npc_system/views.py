from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NpcSystem
from .serializers import NpcSystemReadSerializer, NpcSystemWriteSerializer


@extend_schema(
    summary="List and Create NPC Systems",
    description="""
    Handles listing all accessible NPC systems and creating new ones.

    - **GET**: Retrieves a list of `NpcSystem` objects. Regular users see global systems and their own. Admins see all systems.
    - **POST**: Creates a new `NpcSystem` instance. The owner is automatically set to the current user if `use_current_user` is true.
    """,
    request=NpcSystemWriteSerializer,
    responses={
        200: NpcSystemReadSerializer(many=True),  # For GET success
        201: NpcSystemReadSerializer,  # For POST success
        400: {"description": "Bad Request - Invalid data provided."},
    },
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_list(request):
    """
    List all accessible NPC systems or create a new NPC system.

    - **GET**: Returns a list of NPC systems. Non-admin users will only see
      global systems and systems they own.
    - **POST**: Creates a new NPC system. Use the `NpcSystemWriteSerializer` format.
      The response will be the newly created object in `NpcSystemReadSerializer` format.
    """
    if request.method == "GET":
        user = request.user
        # Admins can see all systems
        if user.is_staff or user.is_superuser:
            systems = NpcSystem.objects.select_related("owner", "genre").all()
        else:
            # Regular users see global systems and their own systems
            systems = NpcSystem.objects.select_related("owner", "genre").filter(
                Q(owner__isnull=True) | Q(owner=user)
            )

        serializer = NpcSystemReadSerializer(
            systems, many=True, context={"request": request}
        )
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NpcSystemWriteSerializer(  # Use WriteSerializer for input
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            instance = serializer.save()
            # Serialize the created instance using the ReadSerializer for the response
            read_serializer = NpcSystemReadSerializer(
                instance, context={"request": request}
            )
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="Retrieve, Update, or Delete an NPC System",
    description="""
    Handles retrieving, updating, partially updating, or deleting a single
    `NpcSystem` instance by its primary key.

    - **GET**: Retrieves a single `NpcSystem` object.
    - **PUT**: Updates an existing `NpcSystem` object.
    - **PATCH**: Partially updates an existing `NpcSystem` object.
    - **DELETE**: Deletes an `NpcSystem` object.
    """,
    request=NpcSystemWriteSerializer,
    responses={
        200: NpcSystemReadSerializer,  # For GET, PUT, PATCH success
        204: {"description": "No Content - The system was successfully deleted."},
        404: {
            "description": "Not Found - The system with the given PK does not exist."
        },
    },
)
@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_detail(request, pk):
    """
    Retrieve, update, or delete an NPC system instance.
    Uses `NpcSystemWriteSerializer` for input and `NpcSystemReadSerializer` for output.
    """
    try:
        # Optimize by fetching related owner data
        system = NpcSystem.objects.select_related("owner", "genre").get(pk=pk)
    except NpcSystem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemReadSerializer(system, context={"request": request})
        return Response(serializer.data)

    elif request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = NpcSystemWriteSerializer(  # Use WriteSerializer for input
            system, data=request.data, partial=partial, context={"request": request}
        )
        if serializer.is_valid():
            instance = serializer.save()
            # Serialize the updated instance using the ReadSerializer for the response
            read_serializer = NpcSystemReadSerializer(
                instance, context={"request": request}
            )
            return Response(read_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
