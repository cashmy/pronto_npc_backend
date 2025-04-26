from rest_framework import serializers
from .models import Image
from django.contrib.auth import get_user_model

User = get_user_model()


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
        ]
        # Avoid depth = 1, use explicit fields like owner_username

    # Correctly indented create method
    def create(self, validated_data):
        """
        Set the owner to the logged-in user from the request context.
        Set file metadata from the uploaded image file.
        """
        request = self.context.get("request")
        image_file = validated_data.get("image")

        # Set owner
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data["owner"] = request.user
        else:
            validated_data["owner"] = None  # Explicitly set to None for global images

        # Set file metadata automatically if not provided
        if image_file:
            if "file_name" not in validated_data or not validated_data.get("file_name"):
                validated_data["file_name"] = image_file.name
            if "file_size" not in validated_data or not validated_data.get("file_size"):
                validated_data["file_size"] = image_file.size
            if "mime_type" not in validated_data or not validated_data.get("mime_type"):
                validated_data["mime_type"] = image_file.content_type

        # Handle potential thumbnail generation here if desired

        return super().create(validated_data)

    # Optional: Add update method if needed, prevent owner change
    # def update(self, instance, validated_data):
    #     validated_data.pop('owner', None) # Owner should not be changed via update
    #     # Handle file metadata updates if image changes
    #     return super().update(instance, validated_data)
