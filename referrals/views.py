# referrals/views.py

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from referrals.models import Referral
from referrals.serializers import ReferralSerializer, ReferredUserProfileSerializer
from profiles.models import Profile  # Import Profile model


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def my_referral_link(request):
    """
    Retrieves (or creates if not existing) the referral link
    for the currently authenticated user.
    """
    if request.method == "GET":
        referral, created = Referral.objects.get_or_create(referred_by=request.user)
        # Pass context to serializer if it needs the request (e.g., for build_absolute_uri)
        serializer = ReferralSerializer(referral, context={"request": request})
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def list_referred_users(request):
    """
    Retrieves a list of users (profiles) who were referred by the
    currently authenticated user's email.
    Returns their email, first name, last name, and avatar.
    """
    if not request.user.email:
        return Response(
            {
                "detail": "Authenticated user does not have an email address to check referrals."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Query profiles that were referred by the current user's email.
    # .select_related('user') is used to optimize fetching related User object details (email, names)
    # to prevent N+1 database queries.
    referred_profiles = Profile.objects.filter(
        referred_by_email=request.user.email
    ).select_related("user")

    serializer = ReferredUserProfileSerializer(referred_profiles, many=True)
    return Response(serializer.data)
