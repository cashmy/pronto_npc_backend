from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from django.conf import settings

# Note: Since the "POST" requires
#       "multipart/form-data" for the "Content-type"
#       because of the "file object", then the
#       "PUT" will also require this or the
#       "get_object_or_404" function will error out.
#       PATCH does NOT require this.


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def images_list(request):
    if request.method == "GET":
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ImageSerializer(data=request.data, context={"request": request})
        print("\n\n\nData", request.data)
        # print("Data", serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif serializer.errors:
            print("Errors", serializer.errors)
            print("Errors", serializer.errors["image"])
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print("Get object Successful")
    if request.method == "GET":
        serializer = ImageSerializer(image)
        print("Data", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif serializer.errors:
            print("Errors", serializer.errors)
            print("Errors", serializer.errors["image"])
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        print("updating some.")
        serializer = ImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
