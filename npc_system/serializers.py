from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NpcSystem, Genre


class OwnerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name")


class NpcSystemSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field="name", queryset=Genre.objects.all()
    )

    use_current_user = serializers.BooleanField(
        write_only=True, required=False, default=False
    )

    owner = OwnerSummarySerializer(read_only=True)

    class Meta:
        model = NpcSystem
        fields = [
            "id",
            "npc_system_name",
            "description",
            "genre",
            "race_table_header",
            "profession_table_header",
            "rpg_class_table_header",
            "standard_app_dsp",
            "is_global",
            "owner",
            "use_current_user",
            "created_at",
            "updated_at",
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
                # Optional: Add debug prints here if needed for the IntegrityError
                print(
                    f"\n\n\nSimplified: Owner set to current user: {owner_instance} (ID: {getattr(owner_instance, 'id', None)})"
                )
                print(
                    f"Simplified: Request user: {request.user} (ID: {getattr(request.user, 'id', None)})\n\n\n"
                )
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
        # If these need to be updatable, add specific logic here.
        validated_data.pop("owner", None)
        validated_data.pop("is_global", None)

        return super().update(instance, validated_data)
