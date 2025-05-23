from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import NpcSystemRace
from .serializers import NpcSystemRaceSerializer, NpcSystemRaceOptionSerializer
import random


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_races_list(request):
    if request.method == "GET":
        systems = NpcSystemRace.objects.all()
        serializer = NpcSystemRaceSerializer(systems, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NpcSystemRaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_races_detail(request, pk):
    try:
        system = NpcSystemRace.objects.get(pk=pk)
    except NpcSystemRace.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemRaceSerializer(system)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = NpcSystemRaceSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = NpcSystemRaceSerializer(system, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Optional: Serializer for the dropdown options in the frontend
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def npc_system_race_options(request, npc_system_pk):
    races = NpcSystemRace.objects.filter(npc_system_id=npc_system_pk).order_by("value")
    serializer = NpcSystemRaceOptionSerializer(races, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_random_npc_system_race(request, npc_system_pk):
    """
    Returns a randomly selected NpcSystemRace for the given NpcSystem.
    It picks a random existing race_id for that system.
    """
    # Get all existing race_ids for the given npc_system
    race_ids = list(
        NpcSystemRace.objects.filter(npc_system_id=npc_system_pk).values_list(
            "race_id", flat=True
        )
    )

    if not race_ids:
        return Response(
            {"detail": "No races found for this NPC system."},
            status=status.HTTP_404_NOT_FOUND,
        )

    selected_race_id = random.choice(race_ids)
    random_race = NpcSystemRace.objects.get(
        npc_system_id=npc_system_pk, race_id=selected_race_id
    )
    serializer = NpcSystemRaceSerializer(random_race)
    return Response(serializer.data, status=status.HTTP_200_OK)
