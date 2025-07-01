from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreOptionSerializer, GenreSerializer


# Create your views here.
@extend_schema(
    tags=["Genres"],
    summary="List and create genres",
    description="Allows for listing all existing genres or creating a new one.",
    responses={
        200: GenreSerializer(many=True),
        201: GenreSerializer,
        400: {"description": "Invalid data provided"},
    },
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def genre_list(request):
    """
    Handle GET and POST requests for the genre list.

    GET: Returns a list of all genres.
    POST: Creates a new genre.

    Args:
        request: The HTTP request object.

    Returns:
        A Response object containing serialized genre data or errors.
    """
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


@extend_schema(
    tags=["Genres"],
    summary="Retrieve, update, or delete a genre",
    description="Handles retrieving, updating (full or partial), and deleting a specific genre by its ID.",
    responses={
        200: GenreSerializer,
        204: {"description": "Genre deleted successfully"},
        400: {"description": "Invalid data provided"},
        404: {"description": "Genre not found"},
    },
)
@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def genre_detail(request, pk):
    pass  # This function-based view is replaced by the class-based view below


@extend_schema(
    tags=["Genres"],
    summary="Retrieve, update, or delete a genre",
    description="Handles retrieving, updating (full or partial), and deleting a specific genre by its ID.",
    responses={
        200: GenreSerializer,
        204: {"description": "Genre deleted successfully"},
        400: {"description": "Invalid data provided"},
        404: {"description": "Genre not found"},
    },
)
class GenreDetail(APIView):
    """
    Retrieve, update or delete a genre instance.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(
            genre, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(
            genre, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Optional: Serializer for the dropdown options in the frontend
@extend_schema(
    tags=["Genres"],
    summary="Get genre options for dropdowns",
    description="Provides a simplified list of genres suitable for frontend dropdown menus.",
    responses={200: GenreOptionSerializer(many=True)},
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def genre_options(request):
    """
    Retrieve a list of genres formatted for dropdown options.

    Args:
        request: The HTTP request object.

    Returns:
        A Response object containing a list of genre options.
    """
    genres = Genre.objects.all().order_by("name")  # optional ordering
    serializer = GenreOptionSerializer(genres, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=["Genres"],
    summary="Get a random genre",
    description="Returns a single, randomly selected genre from the database.",
    responses={
        200: GenreSerializer,
        404: {"description": "No genres found in the database"},
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_random_genre(request):
    """
    Returns a randomly selected Genre.

    Args:
        request: The HTTP request object.

    Returns:
        A Response object containing a single random genre or a 404 error.
    """
    # Efficiently select a random genre from the database
    random_genre = Genre.objects.order_by("?").first()

    if not random_genre:
        return Response(
            {"detail": "No genres found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = GenreSerializer(random_genre, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
