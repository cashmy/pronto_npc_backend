from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import TableHeader
from .serializers import TableHeaderSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def table_header_list(request):
    if request.method == "GET":
        headers = TableHeader.objects.all()
        serializer = TableHeaderSerializer(headers, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TableHeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def table_header_detail(request, pk):
    try:
        header = TableHeader.objects.get(pk=pk)
    except TableHeader.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TableHeaderSerializer(header)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TableHeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = TableHeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def table_header_list_by_system(request, npc_system_id):
    """
    Returns a list of table headers filtered by the provided npc_system_id.
    """
    # Filter TableHeader objects by their direct npc_system ID
    filtered_table_headers = TableHeader.objects.filter(npc_system_id=npc_system_id)
    serializer = TableHeaderSerializer(filtered_table_headers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def table_header_list_by_system_and_group(request, npc_system_id, table_group_id):
    """
    Returns a list of table headers filtered by both the provided
    npc_system_id and table_group_id.
    """
    filtered_table_headers = TableHeader.objects.filter(
        npc_system_id=npc_system_id,
        table_group_id=table_group_id,
    )
    serializer = TableHeaderSerializer(filtered_table_headers, many=True)
    return Response(serializer.data)
