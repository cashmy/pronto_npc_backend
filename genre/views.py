from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from .serializers import GenreSerializer, GenreOptionSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def genre_list(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True, context={"request": request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GenreSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GenreSerializer(genre, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = GenreSerializer(
            genre, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = GenreSerializer(
            genre, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Optional: Serializer for the dropdown options in the frontend
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def genre_options(request):
    genres = Genre.objects.all().order_by("name")  # optional ordering
    serializer = GenreOptionSerializer(genres, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
