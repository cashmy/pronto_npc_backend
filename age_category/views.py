from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import AgeCategory
from .serializers import AgeCategorySerializer, AgeCategoryOptionSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def age_category_list(request):
    if request.method == "GET":
        categories = AgeCategory.objects.all()
        serializer = AgeCategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AgeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def age_category_detail(request, pk):
    try:
        category = AgeCategory.objects.get(pk=pk)
    except AgeCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AgeCategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AgeCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = AgeCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Optional: Serializer for the dropdown options in the frontend
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def age_category_options(request):
    categories = AgeCategory.objects.all().order_by(
        "age_category_name"
    )  # optional ordering
    serializer = AgeCategoryOptionSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
