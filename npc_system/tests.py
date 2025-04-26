from django.test import TestCase
from .models import NpcSystem


class NpcSystemModelTest(TestCase):

    def setUp(self):
        # Create an initial NpcSystem record
        self.npc_system = NpcSystem.objects.create(
            npc_system_name="Inventory Management",
            description="Handles inventory tracking and stock levels.",
            standard_app_dsp=True,
        )

    def test_create_npc_system(self):
        npc_system = NpcSystem.objects.create(
            npc_system_name="CRM NpcSystem",
            description="Manages customer relationships.",
            standard_app_dsp=False,
        )
        self.assertEqual(npc_system.npc_system_name, "CRM NpcSystem")
        self.assertEqual(npc_system.standard_app_dsp, False)
        self.assertIsNotNone(npc_system.created_at)
        self.assertIsNotNone(npc_system.updated_at)

    def test_read_npc_system(self):
        npc_system = NpcSystem.objects.get(npc_system_name="Inventory Management")
        self.assertEqual(
            npc_system.description, "Handles inventory tracking and stock levels."
        )
        self.assertTrue(npc_system.standard_app_dsp)

    def test_update_npc_system(self):
        self.npc_system.description = "Updated description for Inventory NpcSystem."
        self.npc_system.standard_app_dsp = False
        self.npc_system.save()
        updated_npc_system = NpcSystem.objects.get(id=self.npc_system.id)
        self.assertEqual(
            updated_npc_system.description,
            "Updated description for Inventory NpcSystem.",
        )
        self.assertFalse(updated_npc_system.standard_app_dsp)

    def test_delete_npc_system(self):
        npc_system_id = self.npc_system.id
        self.npc_system.delete()
        with self.assertRaises(NpcSystem.DoesNotExist):
            NpcSystem.objects.get(id=npc_system_id)
