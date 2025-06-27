import random

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NpcSystemRace
from .serializers import NpcSystemRaceOptionSerializer, NpcSystemRaceSerializer


class NpcSystemRaceViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing NpcSystemRace instances.

    This ViewSet automatically provides `list`, `create`, `retrieve`, `update`,
    `partial_update`, and `destroy` actions for NpcSystemRace objects.
    Additionally, it includes custom actions for fetching simplified race options
    for dropdowns and selecting a random race for a given NPC system.
    """

    queryset = NpcSystemRace.objects.all()
    serializer_class = NpcSystemRaceSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Retrieves a list of all `NpcSystemRace` objects.

        Returns:
            Response: A list of serialized `NpcSystemRace` objects with HTTP 200 OK.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a new `NpcSystemRace` instance.

        Request Body:
            (JSON): Data for the new `NpcSystemRace` as defined by `NpcSystemRaceSerializer`.

        Returns:
            Response:
                - Serialized new `NpcSystemRace` object with HTTP 201 CREATED on success.
                - Serializer errors with HTTP 400 BAD REQUEST on invalid input.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves a single `NpcSystemRace` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemRace` to retrieve.

        Returns:
            Response: Serialized `NpcSystemRace` object with HTTP 200 OK.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Updates an existing `NpcSystemRace` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemRace` to update.

        Returns:
            Response: Serialized updated `NpcSystemRace` object with HTTP 200 OK on success.
            Response: Serializer errors with HTTP 400 BAD REQUEST on invalid input.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates an existing `NpcSystemRace` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemRace` to partially update.

        Returns:
            Response: Serialized partially updated `NpcSystemRace` object with HTTP 200 OK on success.
            Response: Serializer errors with HTTP 400 BAD REQUEST on invalid input.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes an `NpcSystemRace` object by its primary key.

        Args:
            pk (int): The primary key of the `NpcSystemRace` to delete.

        Returns:
            Response: HTTP 204 NO CONTENT on successful deletion.
        """
        return super().destroy(request, *args, **kwargs)

    @extend_schema(responses=NpcSystemRaceOptionSerializer(many=True))
    @action(detail=False, methods=["get"], url_path="options/(?P<npc_system_pk>[^/.]+)")
    def options(self, request, npc_system_pk: int = None):
        """
        Provides a simplified list of NPC system races (race_id and value)
        suitable for populating dropdown/select options in a frontend.

        The list is filtered by the `npc_system_pk` and ordered by the race `value`.

        Args:
            npc_system_pk (int): The primary key of the `NpcSystem` to filter races by.

        Returns:
            Response: A list of serialized `NpcSystemRaceOptionSerializer` objects
                      with HTTP 200 OK.
        """
        races = NpcSystemRace.objects.filter(npc_system_id=npc_system_pk).order_by(
            "value"
        )
        serializer = NpcSystemRaceOptionSerializer(races, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        responses={
            200: NpcSystemRaceSerializer,
            404: {"description": "No races found for this NPC system."},
        }
    )
    @action(
        detail=False, methods=["get"], url_path="random-race/(?P<npc_system_pk>[^/.]+)"
    )
    def random_race(self, request, npc_system_pk: int = None):
        """
        Returns a randomly selected NpcSystemRace for the given NpcSystem.
        It picks a random existing race_id for that system.

        Args:
            npc_system_pk (int): The primary key of the `NpcSystem` to select a random race from.

        Returns:
            Response:
                - Serialized `NpcSystemRace` object with HTTP 200 OK if a random
                  race is found.
                - JSON object `{"detail": "No races found for this NPC system."}`
                  with HTTP 404 NOT FOUND if no races exist for the given system.
        """
        # Get all existing race_ids for the given npc_system
        race_ids = list(
            NpcSystemRace.objects.filter(npc_system_id=npc_system_pk).values_list(
                "race_id", flat=True
            )
        )

        if not race_ids:
            return Response(
                {"detail": "No races found for this NPC system."},
                status=status.HTTP_404_NOT_FOUND,
            )

        selected_race_id = random.choice(race_ids)
        random_race = get_object_or_404(
            NpcSystemRace, npc_system_id=npc_system_pk, race_id=selected_race_id
        )
        serializer = NpcSystemRaceSerializer(random_race)
        return Response(serializer.data, status=status.HTTP_200_OK)
