from django.shortcuts import render
from rest_framework import status, permissions
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import NpcSystem
from .serializers import NpcSystemReadSerializer, NpcSystemWriteSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def npc_system_list(request):
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
        serializer = NpcSystemWriteSerializer( # Use WriteSerializer for input
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            instance = serializer.save()
            # Serialize the created instance using the ReadSerializer for the response
            read_serializer = NpcSystemReadSerializer(instance, context={"request": request})
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def npc_system_detail(request, pk):
    try:
        # Optimize by fetching related owner data
        system = NpcSystem.objects.select_related("owner", "genre").get(pk=pk)
    except NpcSystem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NpcSystemReadSerializer(system, context={"request": request})
        return Response(serializer.data)
    
    elif request.method in ["PUT", "PATCH"]:
        partial = (request.method == "PATCH")
        serializer = NpcSystemWriteSerializer( # Use WriteSerializer for input
            system, data=request.data, partial=partial, context={"request": request}
        )
        if serializer.is_valid():
            instance = serializer.save()
            # Serialize the updated instance using the ReadSerializer for the response
            read_serializer = NpcSystemReadSerializer(instance, context={"request": request})
            return Response(read_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
