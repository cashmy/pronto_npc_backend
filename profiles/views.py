from rest_framework import generics, permissions
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileMeView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
