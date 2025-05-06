from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import TableItem
from .serializers import TableItemSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def table_item_list(request):
    if request.method == "GET":
        items = TableItem.objects.all()
        serializer = TableItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TableItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def table_item_detail(request, pk):
    try:
        item = TableItem.objects.get(pk=pk)
    except TableItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TableItemSerializer(item)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TableItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        serializer = TableItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def table_items_list_by_table_header(request, table_header):
    """
    Returns a list of table headers filtered by both the provided
    npc_system_id and table_group_id.
    """
    filtered_table_items = TableItem.objects.filter(
        table_header=table_header,
    )
    serializer = TableItemSerializer(filtered_table_items, many=True)
    return Response(serializer.data)
