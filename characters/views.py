from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Character
from .serializers import CharacterSerializer


@extend_schema(
    tags=["Characters"],
    summary="List and create characters",
    description="""
    Handles the listing of all characters accessible to the user and the creation of new characters.
    - **GET**: Returns a list of characters. Non-staff users see only characters they own or global characters.
    - **POST**: Creates a new character. The request body must contain the character data.
    """,
    responses={
        200: CharacterSerializer(many=True),
        201: CharacterSerializer,
        400: "Bad Request",
    },
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def character_list(request):
    """
    List all characters for the current user or create a new character.

    Args:
        request: The HTTP request object.

    Returns:
        A Response object containing a list of characters or the newly created character.
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


@extend_schema(
    tags=["Characters"],
    summary="Retrieve, update, or delete a character",
    description="""
    Handles operations on a single character instance, identified by its primary key.
    - **GET**: Retrieve the details of a specific character.
    - **PUT**: Fully update a character's details.
    - **PATCH**: Partially update a character's details.
    - **DELETE**: Delete a character.
    Requires ownership or staff/superuser privileges.
    """,
    responses={
        200: CharacterSerializer,
        204: "No Content",
        400: "Bad Request",
        403: "Permission Denied",
        404: "Not Found",
    },
)
@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def character_detail(request, pk):
    """
    Retrieve, update, or delete a specific character instance.

    Args:
        request: The HTTP request object.
        pk (int): The primary key of the character to retrieve, update, or delete.

    Returns:
        A Response object containing the character data or a success/error status.
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
