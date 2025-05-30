from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Image
from .serializers import ImageSerializer, ImageOptionSerializer
from django.db.models import Q

# Note: Since the "POST" requires
#       "multipart/form-data" for the "Content-type"
#       because of the "file object", then the
#       "PUT" will also require this or the
#       "get_object_or_404" function will error out.
#       PATCH does NOT require this.


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def images_list(request):
    if request.method == "GET":
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ImageSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == "GET":
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ImageSerializer(image, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = ImageSerializer(image, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Optional: Serializer for the dropdown options in the frontend
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def image_select_options(request, image_type, owner):
    """
    Returns image options for a dropdown.
    Filters by the given image_type.
    Includes images with no owner (global/blank owner) AND images owned by the specified 'owner' id.
    """
    # Validate image_type against the choices defined in the model
    valid_image_types = Image.ImageType.values
    if image_type not in valid_image_types:
        return Response(
            {"error": f"Invalid image_type. Valid types are: {', '.join(valid_image_types)}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Construct the query using Q objects:
    # (image_type = provided_type) AND (owner IS NULL OR owner_id = provided_owner_id)
    query_conditions = Q(image_type=image_type) & (
        Q(owner__isnull=True) | Q(owner_id=owner))
    
    images = Image.objects.filter(query_conditions).order_by("file_name")
    
    # Use the specified ImageOptionSerializer
    serializer = ImageOptionSerializer(images, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)