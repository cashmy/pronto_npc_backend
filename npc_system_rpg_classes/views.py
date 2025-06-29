"""
This module provides the API views for managing RPG classes within an NPC system.

It includes function-based views for:

- Listing and creating RPG classes (`npc_system_rpg_classes_list`).
- Retrieving, updating, and deleting a specific RPG class (`npc_system_rpg_classes_detail`).
- Fetching a simplified list of classes for UI dropdowns (`npc_system_rpg_class_options`).
- Selecting a random RPG class from a given NPC system (`get_random_npc_system_rpg_class`).

"""

import random

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NpcSystemRpgClass
from .serializers import NpcSystemRpgClassOptionSerializer, NpcSystemRpgClassSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_rpg_classes_list(request):
    """
    Handles listing and creation of `NpcSystemRpgClass` instances.

    - GET: Retrieves a list of all `NpcSystemRpgClass` objects.
    - POST: Creates a new `NpcSystemRpgClass` instance.

    Args:
        request (Request): The incoming HTTP request.

    Returns:
        Response:
            - For GET: A list of serialized `NpcSystemRpgClass` objects with HTTP 200 OK.
            - For POST on success: The serialized new `NpcSystemRpgClass` object with HTTP 201 CREATED.
            - For POST on failure: Serializer errors with HTTP 400 BAD REQUEST.
    """
    if request.method == "GET":
        systems = NpcSystemRpgClass.objects.all()
        serializer = NpcSystemRpgClassSerializer(systems, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NpcSystemRpgClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_rpg_classes_detail(request, pk):
    """
    Handles retrieval, update, and deletion of a single `NpcSystemRpgClass` instance.

    - GET: Retrieves a single `NpcSystemRpgClass` object by its primary key.
    - PUT: Updates an existing `NpcSystemRpgClass` object.
    - PATCH: Partially updates an existing `NpcSystemRpgClass` object.
    - DELETE: Deletes an `NpcSystemRpgClass` object.

    Args:
        request (Request): The incoming HTTP request.
        pk (int): The primary key of the `NpcSystemRpgClass` to interact with.

    Returns:
        Response:
            - For GET: Serialized `NpcSystemRpgClass` object with HTTP 200 OK.
            - For PUT/PATCH on success: Serialized updated object with HTTP 200 OK.
            - For PUT/PATCH on failure: Serializer errors with HTTP 400 BAD REQUEST.
            - For DELETE: HTTP 204 NO CONTENT on successful deletion.
            - If not found: HTTP 404 NOT FOUND.
    """
    try:
        system = NpcSystemRpgClass.objects.get(pk=pk)
    except NpcSystemRpgClass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemRpgClassSerializer(system)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = NpcSystemRpgClassSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = NpcSystemRpgClassSerializer(
            system, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Optional: Serializer for the dropdown options in the frontend
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def npc_system_rpg_class_options(request, npc_system_pk):
    """
    Provides a simplified list of NPC system RPG classes (rpg_class_id and value)
    suitable for populating dropdown/select options in a frontend.

    The list is filtered by the `npc_system_pk` and ordered by the class `value`.

    Args:
        request (Request): The incoming HTTP request.
        npc_system_pk (int): The primary key of the `NpcSystem` to filter classes by.

    Returns:
        Response: A list of serialized `NpcSystemRpgClassOptionSerializer` objects
                  with HTTP 200 OK.
    """
    systems = NpcSystemRpgClass.objects.filter(npc_system_id=npc_system_pk).order_by(
        "value"
    )
    serializer = NpcSystemRpgClassOptionSerializer(systems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_random_npc_system_rpg_class(request, npc_system_pk):
    """
    Returns a randomly selected NpcSystemRpgClass for the given NpcSystem.

    It picks a random existing rpg_class_id for that system.

    Args:
        request (Request): The incoming HTTP request.
        npc_system_pk (int): The primary key of the `NpcSystem` to select a random class from.

    Returns:
        Response:
            - Serialized `NpcSystemRpgClass` object with HTTP 200 OK if a random class is found.
            - JSON object `{"detail": "No classes found for this NPC system."}` with HTTP 404 NOT FOUND if no classes exist for the given system.
    """
    # Get all existing rpg_class_ids for the given npc_system
    rpg_class_ids = list(
        NpcSystemRpgClass.objects.filter(npc_system_id=npc_system_pk).values_list(
            "rpg_class_id", flat=True
        )
    )

    if not rpg_class_ids:
        return Response(
            {"detail": "No classes found for this NPC system."},
            status=status.HTTP_404_NOT_FOUND,
        )

    selected_rpg_class_id = random.choice(rpg_class_ids)
    random_race = NpcSystemRpgClass.objects.get(
        npc_system_id=npc_system_pk, rpg_class_id=selected_rpg_class_id
    )
    serializer = NpcSystemRpgClassSerializer(random_race)
    return Response(serializer.data, status=status.HTTP_200_OK)
