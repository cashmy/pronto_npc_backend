from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CharacterSubGroup
from .serializers import CharacterSubGroupSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def character_sub_group_list(request):
    if request.method == "GET":
        character_sub_groups = CharacterSubGroup.objects.all()
        serializer = CharacterSubGroupSerializer(character_sub_groups, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CharacterSubGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def character_sub_group_detail(request, pk):
    try:
        character_sub_group = CharacterSubGroup.objects.get(pk=pk)
    except CharacterSubGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CharacterSubGroupSerializer(character_sub_group)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CharacterSubGroupSerializer(character_sub_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        character_sub_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = CharacterSubGroupSerializer(
            character_sub_group, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def character_sub_group_list_by_system(request, npc_system_id):
    """
    Returns a list of character sub-groups filtered by the provided npc_system_id
    (via the parent CharacterGroup).
    """
    # Filter CharacterSubGroup objects by the parent CharacterGroup's npc_system ID
    filtered_sub_groups = CharacterSubGroup.objects.filter(
        character_group__npc_system_id=npc_system_id
    )
    serializer = CharacterSubGroupSerializer(filtered_sub_groups, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def character_sub_group_list_by_system_and_group(
    request, npc_system_id, character_group_id
):
    """
    Returns a list of character sub-groups filtered by both the provided
    npc_system_id and character_group_id.
    """
    filtered_sub_groups = CharacterSubGroup.objects.filter(
        character_group__npc_system_id=npc_system_id,
        character_group_id=character_group_id,
    )
    serializer = CharacterSubGroupSerializer(filtered_sub_groups, many=True)
    return Response(serializer.data)
