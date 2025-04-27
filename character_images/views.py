from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CharacterImage
from .serializers import CharacterImageSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def character_image_list(request):
    """
    List all character images or create a new character image.
    """
    if request.method == "GET":
        character_images = CharacterImage.objects.all()
        serializer = CharacterImageSerializer(character_images, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CharacterImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def character_image_detail(request, pk):
    """
    Retrieve, update or delete a character image.
    """
    try:
        character_image = CharacterImage.objects.get(pk=pk)
    except CharacterImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CharacterImageSerializer(character_image)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CharacterImageSerializer(character_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        character_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = CharacterImageSerializer(
            character_image, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
