from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usage_tracking.models import UsageTracking
from usage_tracking.serializers import UsageTrackingSerializer


# Create your views here.
@api_view(["GET", "PUT", "PATCH"])
@permission_classes([permissions.IsAuthenticated])
def usage_tracking_me(request):
    """
    Retrieve, update or partially update the usage tracking of the currently authenticated user.
    """
    try:
        print("Request user:", request.user)  # Debugging line to check the user
        # UsageTracking is linked one-to-one with User.
        # Accessing request.user.usage_tracking will raise UsageTracking.DoesNotExist if no usage tracking exists.
        usage_tracking = request.user.usage_metrics
    except UsageTracking.DoesNotExist:
        # This scenario implies a user exists without usage tracking, which might indicate
        # an issue with the usage tracking creation process (e.g., signal not firing).
        return Response(
            {"detail": "Usage tracking not found for this user."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except AttributeError:
        # This can happen if request.user is AnonymousUser, though IsAuthenticated should prevent this.
        return Response(
            {"detail": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED
        )

    if request.method == "GET":
        serializer = UsageTrackingSerializer(usage_tracking)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UsageTrackingSerializer(usage_tracking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = UsageTrackingSerializer(
            usage_tracking, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])  # Typically admin-only
def usage_tracking_list(request):
    """
    List all usage tracking records.
    Note: Usage tracking creation is usually handled during user registration or activity.
    """
    if request.method == "GET":
        usage_trackings = UsageTracking.objects.all()
        serializer = UsageTrackingSerializer(usage_trackings, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([permissions.IsAdminUser])  # Typically admin-only
def usage_tracking_detail_by_pk(request, pk):
    """
    Retrieve, update, partially update or delete a specific usage tracking record by its primary key.
    """
    try:
        usage_tracking = UsageTracking.objects.get(pk=pk)
    except UsageTracking.DoesNotExist:
        return Response(
            {"detail": "Usage tracking not found."}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = UsageTrackingSerializer(usage_tracking)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UsageTrackingSerializer(usage_tracking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = UsageTrackingSerializer(
            usage_tracking, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        usage_tracking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
