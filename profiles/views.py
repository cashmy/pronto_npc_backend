from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([permissions.IsAuthenticated])
def profile_me(request):
    """
    Retrieve, update or partially update the profile of the currently authenticated user.
    """
    try:
        # Profile is linked one-to-one with User.
        # Accessing request.user.profile will raise Profile.DoesNotExist if no profile exists.
        profile = request.user.profile
    except Profile.DoesNotExist:
        # This scenario implies a user exists without a profile, which might indicate
        # an issue with the profile creation process (e.g., signal not firing).
        return Response(
            {"detail": "Profile not found for this user."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except AttributeError:
        # This can happen if request.user is AnonymousUser, though IsAuthenticated should prevent this.
        return Response(
            {"detail": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED
        )

    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == "PUT":  # Full update
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":  # Partial update
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])  # Typically admin-only
def profile_list(request):
    """
    List all profiles.
    Note: Profile creation is usually handled during user registration.
    """
    if request.method == "GET":
        profiles = Profile.objects.select_related("user").all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([permissions.IsAdminUser])  # Typically admin-only
def profile_detail_by_pk(request, pk):
    """
    Retrieve, update, partially update, or delete a profile by its PK.
    """
    try:
        profile = Profile.objects.select_related("user").get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Re-use the logic from profile_me for GET, PUT, PATCH by passing the fetched profile
    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # Consider implications: deleting a profile might leave a user orphaned
        # or should be tied to user deletion.
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
