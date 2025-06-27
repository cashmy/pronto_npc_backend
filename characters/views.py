from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Character
from .serializers import CharacterSerializer
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def character_list(request):
    """
    List all characters or create a new character.
    """
    if request.method == "GET":
        characters = Character.objects.all()
        # serializer = CharacterSerializer(characters, many=True)
        user = request.user
        if not user.is_staff or user.is_superuser:
            characters = Character.objects.all()
        else:
            # If the user is not staff, filter characters by owner
            characters = Character.objects.filter(Q(owner=user) | Q(owner__isnull=True))
        serializer = CharacterSerializer(
            characters, many=True, context={"request": request}
        )
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # After saving, re-serialize with context if needed for display fields
            # Although CharacterSerializer doesn't strictly need context for its display fields,
            # it's good practice to pass it if the serializer might use it.
            # For simplicity, we can just return the validated data which includes the saved instance.
            # Or fetch the instance again if complex display fields are critical post-save.
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def character_detail(request, pk):
    """
    Retrieve, update or delete a character.
    """
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Object-level permission check: Only owner or admin can access/modify
    user = request.user
    if not (user.is_staff or user.is_superuser or character.owner == user):
        raise PermissionDenied("You do not have permission to access this character.")

    if request.method == "GET":
        serializer = CharacterSerializer(character, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CharacterSerializer(
            character, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = CharacterSerializer(
            character, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
