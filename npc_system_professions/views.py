import random

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NpcSystemProfession
from .serializers import (
    NpcSystemProfessionOptionSerializer,
    NpcSystemProfessionSerializer,
)


class NpcSystemProfessionViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing NpcSystemProfession instances.

    This ViewSet automatically provides `list`, `create`, `retrieve`, `update`,
    `partial_update`, and `destroy` actions. It also includes custom actions
    for fetching dropdown options and selecting a random profession.
    """

    queryset = NpcSystemProfession.objects.all()
    serializer_class = NpcSystemProfessionSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Retrieves a list of all `NpcSystemProfession` objects.

        Returns:
            Response: A list of serialized `NpcSystemProfession` objects with HTTP 200 OK.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a new `NpcSystemProfession` instance.

        Request Body:
            (JSON): Data for the new `NpcSystemProfession` as defined by `NpcSystemProfessionSerializer`.

        Returns:
            Response:
                - Serialized new `NpcSystemProfession` object with HTTP 201 CREATED on success.
                - Serializer errors with HTTP 400 BAD REQUEST on invalid input.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves a single `NpcSystemProfession` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemProfession` to retrieve.

        Returns:
            Response: Serialized `NpcSystemProfession` object with HTTP 200 OK.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Updates an existing `NpcSystemProfession` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemProfession` to update.

        Returns:
            Response: Serialized updated `NpcSystemProfession` object with HTTP 200 OK on success.
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes an `NpcSystemProfession` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemProfession` to delete.

        Returns:
            Response: HTTP 204 NO CONTENT on successful deletion.
        """
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Get Profession Options for a System",
        responses=NpcSystemProfessionOptionSerializer(many=True),
    )
    @action(detail=False, methods=["get"], url_path="options/(?P<npc_system_pk>[^/.]+)")
    def options(self, request, npc_system_pk: int = None):
        """
        Provides a simplified list of NPC system professions (profession_id and value)
        suitable for populating dropdown/select options in a frontend.

        The list is filtered by the `npc_system_pk` and ordered by the profession `value`.

        Args:
            npc_system_pk (int): The primary key of the `NpcSystem` to filter professions by.

        Returns:
            Response: A list of serialized `NpcSystemProfessionOptionSerializer` objects with HTTP 200 OK.
        """
        professions = NpcSystemProfession.objects.filter(
            npc_system_id=npc_system_pk
        ).order_by("value")
        serializer = NpcSystemProfessionOptionSerializer(professions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Get a Random Profession for a System",
        responses={
            200: NpcSystemProfessionSerializer,
            404: {"description": "No professions found for this NPC system."},
        },
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="random-profession/(?P<npc_system_pk>[^/.]+)",
    )
    def random_profession(self, request, npc_system_pk: int = None):
        """
        Returns a randomly selected `NpcSystemProfession` for the given `NpcSystem`.

        This endpoint first retrieves all `profession_id` values associated with the
        specified `npc_system_pk`. It then randomly selects one of these IDs and
        fetches the corresponding `NpcSystemProfession` object.

        Args:
            npc_system_pk (int): The primary key of the `NpcSystem` to select a random profession from.

        Returns:
            Response:
                - Serialized `NpcSystemProfession` object with HTTP 200 OK if a random profession is found.
                - JSON object `{"detail": "No professions found for this NPC system."}` with HTTP 404 NOT FOUND if no professions exist for the given system.
        """
        # Get all existing profession_ids for the given npc_system
        profession_ids = list(
            NpcSystemProfession.objects.filter(npc_system_id=npc_system_pk).values_list(
                "profession_id", flat=True
            )
        )

        if not profession_ids:
            return Response(
                {"detail": "No professions found for this NPC system."},
                status=status.HTTP_404_NOT_FOUND,
            )

        selected_profession_id = random.choice(profession_ids)
        random_profession = get_object_or_404(
            NpcSystemProfession,
            npc_system_id=npc_system_pk,
            profession_id=selected_profession_id,
        )
        serializer = NpcSystemProfessionSerializer(random_profession)
        return Response(serializer.data, status=status.HTTP_200_OK)
