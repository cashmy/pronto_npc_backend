from rest_framework import serializers
from .models import Image
from django.contrib.auth import get_user_model

User = get_user_model()


class OwnerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name")


class ImageSerializer(serializers.ModelSerializer):
    # Display owner's username (read-only) instead of the full user object or ID
    owner_username = serializers.CharField(
        source="owner.username", read_only=True, allow_null=True
    )
    # Make image and thumbnail fields return URLs
    image = serializers.ImageField(use_url=True)
    thumbnail = serializers.ImageField(
        use_url=True, required=False, allow_null=True
    )  # Mark as not required
    # Flag to indicate if the owner should be the current user
    use_current_user = serializers.BooleanField(
        write_only=True, required=False, default=False
    )

    owner = OwnerSummarySerializer(read_only=True)

    class Meta:
        model = Image
        fields = [
            "id",
            "file_name",
            "alt_text",  # Correctly included now
            "mime_type",
            "file_size",
            "image",  # Will now be a URL
            "thumbnail",  # Will now be a URL (optional)
            "image_type",
            "owner_username",  # Use username instead of user/user_id
            "owner",  # Owner serializer for detailed info (read-only)
            "use_current_user",  # Include the flag for input
            "created_at",
            "updated_at",
        ]
        # Fields that are set automatically or shouldn't be directly input
        read_only_fields = [
            "owner_username",
            "created_at",
            "updated_at",
            "file_size",  # Often set based on uploaded file
            "mime_type",  # Often set based on uploaded file
            "file_name",  # Often set based on uploaded file
            "owner",
        ]
        # Avoid depth = 1, use explicit fields like owner_username

    # Correctly indented create method
    def create(self, validated_data):
        """
        Set the owner to the logged-in user from the request context.
        Set file metadata from the uploaded image file.
        """
        owner_instance = None

        # Pop the flag before creating the model instance
        use_current_user_flag = validated_data.pop("use_current_user", False)

        request = self.context.get("request")
        image_file = validated_data.get("image")

        # Set owner based on the flag
        if use_current_user_flag:
            if request and hasattr(request, "user") and request.user.is_authenticated:
                owner_instance = request.user
            # else: owner remains None (global image) if flag is true but user not logged in
            # This case might indicate a potential issue if IsAuthenticated permission is used.
            print(
                f"\n\n\nSimplified: Owner set to current user: {owner_instance} (ID: {getattr(owner_instance, 'id', None)})"
            )
            print(
                f"Simplified: Request user: {request.user} (ID: {getattr(request.user, 'id', None)})\n\n\n"
            )

        # Set file metadata automatically if not provided
        if image_file:
            if "file_name" not in validated_data or not validated_data.get("file_name"):
                validated_data["file_name"] = image_file.name
            if "file_size" not in validated_data or not validated_data.get("file_size"):
                validated_data["file_size"] = image_file.size
            if "mime_type" not in validated_data or not validated_data.get("mime_type"):
                validated_data["mime_type"] = image_file.content_type

        # Handle potential thumbnail generation here if desired

        # Create the instance, passing owner explicitly
        instance = Image.objects.create(owner=owner_instance, **validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        Handle updates. Prevent owner change.
        Update file metadata only if a new image file is uploaded.
        """
        # Pop the flag if it was somehow included in PATCH/PUT data
        validated_data.pop("use_current_user", None)
        # Prevent owner from being changed during update
        validated_data.pop("owner", None)

        return super().update(instance, validated_data)


# Serializer for the dropdown options in the frontend
class ImageOptionSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image")
    thumbnail_url = serializers.ImageField(source="thumbnail", allow_null=True)

    class Meta:
        model = Image
        fields = [
            "id",
            "file_name",
            "alt_text",  # Correctly included now
            "image_url",  # Will now be a URL
            "thumbnail_url",  # Will now be a URL (optional)
            "image_type",
            "mime_type",
            "file_size",
            "owner",  # Owner serializer for detailed info (read-only)
        ]
