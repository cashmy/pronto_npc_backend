import random

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NpcSystemProfession
from .serializers import (
    NpcSystemProfessionOptionSerializer,
    NpcSystemProfessionSerializer,
)


@extend_schema(
    # For POST requests, the body is described by NpcSystemProfessionSerializer
    request=NpcSystemProfessionSerializer,
    responses={
        200: NpcSystemProfessionSerializer(many=True),  # For GET list response
        201: NpcSystemProfessionSerializer,  # For POST success response
    },
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_professions_list(request):
    """
    Handles listing all NPC system professions and creating new ones.

    GET:
    Retrieves a list of all `NpcSystemProfession` objects.

    Returns:
        Response: A list of serialized `NpcSystemProfession` objects with HTTP 200 OK.

    POST:
    Creates a new `NpcSystemProfession` instance.

    Request Body:
        (JSON): Data for the new `NpcSystemProfession` as defined by `NpcSystemProfessionSerializer`.

    Returns:
        Response:
            - Serialized new `NpcSystemProfession` object with HTTP 201 CREATED on success.
            - Serializer errors with HTTP 400 BAD REQUEST on invalid input.

    """
    if request.method == "GET":
        systems = NpcSystemProfession.objects.all()
        serializer = NpcSystemProfessionSerializer(systems, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NpcSystemProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    # For PUT/PATCH requests
    request=NpcSystemProfessionSerializer,
    responses={
        200: NpcSystemProfessionSerializer,  # For GET/PUT/PATCH success
        204: None,  # For DELETE success (no content)
    },
)
@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_professions_detail(request, pk):
    """
    Handles retrieving, updating, partially updating, or deleting a single
    `NpcSystemProfession` instance by its primary key.

    Args:
        pk (int): The primary key of the `NpcSystemProfession` to retrieve, update, or delete.

    GET:
    Retrieves a single `NpcSystemProfession` object.

    Returns:
        Response: Serialized `NpcSystemProfession` object with HTTP 200 OK.

    PUT:
    Updates an existing `NpcSystemProfession` object.

    PATCH:
    Partially updates an existing `NpcSystemProfession` object.

    DELETE:
    Deletes an `NpcSystemProfession` object.

    Returns (for PUT/PATCH):
        Response:
            - Serialized updated `NpcSystemProfession` object with HTTP 200 OK on success.
            - Serializer errors with HTTP 400 BAD REQUEST on invalid input.
        Response: HTTP 204 NO CONTENT on successful deletion.
    """
    try:
        system = NpcSystemProfession.objects.get(pk=pk)
    except NpcSystemProfession.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemProfessionSerializer(system)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = NpcSystemProfessionSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = NpcSystemProfessionSerializer(
            system, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Optional: Serializer for the dropdown options in the frontend
@extend_schema(responses=NpcSystemProfessionOptionSerializer(many=True))
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def npc_system_profession_options(request, npc_system_pk: int):
    """
    Provides a simplified list of NPC system professions (profession_id and value)
    suitable for populating dropdown/select options in a frontend.

    The list is filtered by the `npc_system_pk` and ordered by the profession `value`.

    Args:
        npc_system_pk (int): The primary key of the `NpcSystem` to filter professions by.

    Returns:
        Response: A list of serialized `NpcSystemProfessionOptionSerializer` objects
                  with HTTP 200 OK.
    """
    professions = NpcSystemProfession.objects.filter(
        npc_system_id=npc_system_pk
    ).order_by("value")
    serializer = NpcSystemProfessionOptionSerializer(professions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(responses=NpcSystemProfessionSerializer)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_random_npc_system_profession(request, npc_system_pk):
    """
    Returns a randomly selected `NpcSystemProfession` for the given `NpcSystem`.

    This endpoint first retrieves all `profession_id` values associated with the
    specified `npc_system_pk`. It then randomly selects one of these IDs and
    fetches the corresponding `NpcSystemProfession` object.

    Args:
        npc_system_pk (int): The primary key of the `NpcSystem` to select a random
                             profession from.

    Returns:
        Response:
            - Serialized `NpcSystemProfession` object with HTTP 200 OK if a random
              profession is found.
            - JSON object `{"detail": "No races found for this NPC system."}`
              with HTTP 404 NOT FOUND if no professions exist for the given system.
    """
    # Get all existing profession_ids for the given npc_system
    profession_ids = list(
        NpcSystemProfession.objects.filter(npc_system_id=npc_system_pk).values_list(
            "profession_id", flat=True
        )
    )

    if not profession_ids:
        return Response(
            {"detail": "No races found for this NPC system."},
            status=status.HTTP_404_NOT_FOUND,
        )

    selected_profession_id = random.choice(profession_ids)
    random_race = NpcSystemProfession.objects.get(
        npc_system_id=npc_system_pk, profession_id=selected_profession_id
    )
    serializer = NpcSystemProfessionSerializer(random_race)
    return Response(serializer.data, status=status.HTTP_200_OK)
