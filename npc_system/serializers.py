from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NpcSystem
from genre.models import Genre  # Import the Genre model
from genre.serializers import GenreSerializer


class OwnerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name")


class NpcSystemReadSerializer(serializers.ModelSerializer):
    """
    Serializer for reading NpcSystem instances, with nested genre and owner.
    """
    genre = GenreSerializer(read_only=True)
    owner = OwnerSummarySerializer(read_only=True)

    class Meta:
        model = NpcSystem
        fields = [
            "id",
            "npc_system_name",
            "description",
            "genre",
            "npc_system_image",
            "npc_system_icon",
            "npc_system_color",
            "npc_system_color_name",
            "race_table_header",
            "profession_table_header",
            "rpg_class_table_header",
            "standard_app_dsp",
            "is_global",
            "owner",
            "created_at",
            "updated_at",
        ]
        # For a read-only serializer, read_only_fields are somewhat implicit,
        # but this list was in the original and can be kept for clarity if desired.
        # However, explicit read_only=True on nested serializers is more direct.


class NpcSystemWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for writing (create/update) NpcSystem instances.
    Accepts a PK for genre.
    """
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        allow_null=True, # Corresponds to model's null=True
        required=False   # Corresponds to model's blank=True
    )
    # Accept string paths for images/icons instead of file uploads
    npc_system_image = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )
    npc_system_icon = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )
    use_current_user = serializers.BooleanField(
        write_only=True, required=False, default=False
    )

    class Meta:
        model = NpcSystem
        fields = [
            "npc_system_name", "description", "genre",
            "npc_system_image", "npc_system_icon", "npc_system_color",
            "npc_system_color_name", "race_table_header",
            "profession_table_header", "rpg_class_table_header",
            "standard_app_dsp", "use_current_user",            
        ]
        read_only_fields = ["id", "created_at", "updated_at", "is_global", "owner"]

    def create(self, validated_data):
        request = self.context.get("request")
        owner_instance = None
        is_global_system = True  # Default to global

        # Pop the flag before creating the model instance
        use_current_user_flag = validated_data.pop("use_current_user", False)

        # If flag is set, try to assign the current authenticated user
        if use_current_user_flag:
            if request and hasattr(request, "user") and request.user.is_authenticated:
                owner_instance = request.user
                is_global_system = False  # Not global if owner is set
            else:
                # Flag was set, but user is not authenticated (should ideally not happen with IsAuthenticated permission)
                # Or request context is missing. Treat as global or raise error? Let's treat as global for now.
                pass  # owner_instance remains None, is_global_system remains True

        # Note: is_global is also a read_only_field, so we must pass it explicitly to create

        # Create the instance, passing owner and is_global directly
        instance = NpcSystem.objects.create(
            owner=owner_instance, is_global=is_global_system, **validated_data
        )
        return instance

    def update(self, instance, validated_data):
        # Pop the flag if it was somehow included in PATCH/PUT data
        validated_data.pop("use_current_user", None)
        
        # Prevent changing owner or global status implicitly during update
        # These fields are not in the `fields` list of this serializer for direct input,
        # and `read_only_fields` further protects them if they were.
        # If `use_current_user` should affect owner/is_global on update,
        # that logic would be added here.
        
        return super().update(instance, validated_data)
