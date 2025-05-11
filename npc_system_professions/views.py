from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import NpcSystemProfession
from .serializers import (
    NpcSystemProfessionSerializer,
    NpcSystemProfessionOptionSerializer,
)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_professions_list(request):
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


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_professions_detail(request, pk):
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
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def npc_system_profession_options(request, npc_system_pk):
    professions = NpcSystemProfession.objects.filter(
        npc_system_id=npc_system_pk
    ).order_by("value")
    serializer = NpcSystemProfessionOptionSerializer(professions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
