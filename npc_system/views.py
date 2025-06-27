from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import NpcSystem
from .serializers import NpcSystemSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_list(request):
    if request.method == "GET":
        systems = NpcSystem.objects.all()
        serializer = NpcSystemSerializer(systems, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NpcSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_detail(request, pk):
    try:
        system = NpcSystem.objects.get(pk=pk)
    except NpcSystem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemSerializer(system)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = NpcSystemSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = NpcSystemSerializer(system, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
