from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CharacterGroup
from .serializers import CharacterGroupSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def character_group_list(request):
    if request.method == "GET":
        character_groups = CharacterGroup.objects.all()
        serializer = CharacterGroupSerializer(character_groups, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CharacterGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def character_group_detail(request, pk):
    try:
        character_group = CharacterGroup.objects.get(pk=pk)
    except CharacterGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CharacterGroupSerializer(character_group)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CharacterGroupSerializer(character_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        character_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = CharacterGroupSerializer(
            character_group, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
