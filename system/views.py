from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import System
from .serializers import SystemSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def system_list(request):
    if request.method == "GET":
        systems = System.objects.all()
        serializer = SystemSerializer(systems, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def system_detail(request, pk):
    try:
        system = System.objects.get(pk=pk)
    except System.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SystemSerializer(system)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SystemSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = SystemSerializer(system, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
