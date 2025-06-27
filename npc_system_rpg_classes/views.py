from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import NpcSystemRpgClass
from .serializers import NpcSystemRpgClassSerializer, NpcSystemRpgClassOptionSerializer
import random


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_rpg_classes_list(request):
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
    """
    # Get all existing rpg_class_ids for the given npc_system
    rpg_class_ids = list(
        NpcSystemRpgClass.objects.filter(npc_system_id=npc_system_pk).values_list(
            "rpg_class_id", flat=True
        )
    )

    if not rpg_class_ids:
        return Response(
            {"detail": "No races found for this NPC system."},
            status=status.HTTP_404_NOT_FOUND,
        )

    selected_rpg_class_id = random.choice(rpg_class_ids)
    random_race = NpcSystemRpgClass.objects.get(
        npc_system_id=npc_system_pk, rpg_class_id=selected_rpg_class_id
    )
    serializer = NpcSystemRpgClassSerializer(random_race)
    return Response(serializer.data, status=status.HTTP_200_OK)
