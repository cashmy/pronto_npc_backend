from django.test import TestCase
from .models import System


class SystemModelTest(TestCase):

    def setUp(self):
        # Create an initial System record
        self.system = System.objects.create(
            system_name="Inventory Management",
            description="Handles inventory tracking and stock levels.",
            standard_app_dsp=True,
        )

    def test_create_system(self):
        system = System.objects.create(
            system_name="CRM System",
            description="Manages customer relationships.",
            standard_app_dsp=False,
        )
        self.assertEqual(system.system_name, "CRM System")
        self.assertEqual(system.standard_app_dsp, False)
        self.assertIsNotNone(system.created_at)
        self.assertIsNotNone(system.updated_at)

    def test_read_system(self):
        system = System.objects.get(system_name="Inventory Management")
        self.assertEqual(
            system.description, "Handles inventory tracking and stock levels."
        )
        self.assertTrue(system.standard_app_dsp)

    def test_update_system(self):
        self.system.description = "Updated description for Inventory System."
        self.system.standard_app_dsp = False
        self.system.save()
        updated_system = System.objects.get(id=self.system.id)
        self.assertEqual(
            updated_system.description, "Updated description for Inventory System."
        )
        self.assertFalse(updated_system.standard_app_dsp)

    def test_delete_system(self):
        system_id = self.system.id
        self.system.delete()
        with self.assertRaises(System.DoesNotExist):
            System.objects.get(id=system_id)
