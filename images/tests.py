import os
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Image

# Get the custom user model
User = get_user_model()


# Helper function to create a dummy image file
def create_dummy_image(name="test_image.png", content=b"dummy_content"):
    """Creates a simple dummy image file for testing."""
    return SimpleUploadedFile(name, content, content_type="image/png")


class ImageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        # Create a test user
        cls.user = User.objects.create_user(username="testuser", password="password123")

        # Create a dummy image file for initial setup
        cls.initial_image_file = create_dummy_image("initial.png")

        # Create an initial Image record associated with the user
        cls.image = Image.objects.create(
            file_name="initial.png",
            file_size=cls.initial_image_file.size,  # <-- Use .size instead of len(.content)
            mime_type=cls.initial_image_file.content_type,
            image=cls.initial_image_file,
            image_type=Image.ImageType.IMAGE,
            owner=cls.user,
            # alt_text="Initial test image", # Optional
        )

        # Create a dummy thumbnail file (optional, if needed)
        cls.initial_thumbnail_file = create_dummy_image("initial_thumb.png", b"thumb")
        cls.image.thumbnail = cls.initial_thumbnail_file
        cls.image.save()

    def tearDown(self):
        """Clean up files after each test."""
        # Ensure files associated with the test image instance are deleted if they exist
        if self.image and self.image.pk:  # Check if image still exists
            try:
                img_instance = Image.objects.get(pk=self.image.pk)
                if img_instance.image:
                    if hasattr(img_instance.image, "path") and os.path.exists(
                        img_instance.image.path
                    ):
                        os.remove(img_instance.image.path)
                if img_instance.thumbnail:
                    if hasattr(img_instance.thumbnail, "path") and os.path.exists(
                        img_instance.thumbnail.path
                    ):
                        os.remove(img_instance.thumbnail.path)
            except Image.DoesNotExist:
                pass  # Object already deleted, files might be gone too

        # Clean up any other potential test files created directly
        # Get image and thumbnail directories from settings if possible, fallback otherwise
        image_dir = os.path.join(settings.MEDIA_ROOT, "images")
        thumb_dir = os.path.join(settings.MEDIA_ROOT, "thumbnails")

        for filename in [
            "test_create.png",
            "test_global.png",
            "delete_me.png",
            "initial.png",
            "initial_thumb.png",
        ]:
            filepath = os.path.join(image_dir, filename)
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except OSError:  # Handle potential errors during cleanup
                    pass
            thumb_filepath = os.path.join(thumb_dir, filename)
            if os.path.exists(thumb_filepath):
                try:
                    os.remove(thumb_filepath)
                except OSError:
                    pass

    def test_create_image(self):
        """Test creating a new Image instance with an owner."""
        image_file = create_dummy_image("test_create.png")
        image = Image.objects.create(
            file_name="test_create.png",
            file_size=image_file.size,  # <-- Use .size instead of len(.content)
            mime_type=image_file.content_type,
            image=image_file,
            image_type=Image.ImageType.AVATAR,
            owner=self.user,
            # alt_text="Created test image",
        )
        self.assertEqual(image.file_name, "test_create.png")
        self.assertEqual(image.owner, self.user)
        self.assertEqual(image.image_type, Image.ImageType.AVATAR)
        self.assertTrue(image.image.name.endswith("test_create.png"))
        self.assertIsNotNone(image.created_at)
        self.assertIsNotNone(image.updated_at)
        # Clean up the created file explicitly if tearDown doesn't catch it
        # Note: tearDown should ideally handle this, but explicit cleanup can be safer
        # if image.image and hasattr(image.image, 'path') and os.path.exists(image.image.path):
        #     os.remove(image.image.path)

    def test_create_global_image(self):
        """Test creating a new Image instance without an owner (global)."""
        image_file = create_dummy_image("test_global.png")
        image = Image.objects.create(
            file_name="test_global.png",
            file_size=image_file.size,  # <-- Use .size instead of len(.content)
            mime_type=image_file.content_type,
            image=image_file,
            image_type=Image.ImageType.TOKEN,
            owner=None,
            # alt_text="Global test image",
        )
        self.assertEqual(image.file_name, "test_global.png")
        self.assertIsNone(image.owner)
        self.assertEqual(image.image_type, Image.ImageType.TOKEN)
        self.assertTrue(image.image.name.endswith("test_global.png"))
        # Clean up the created file explicitly
        # if image.image and hasattr(image.image, 'path') and os.path.exists(image.image.path):
        #     os.remove(image.image.path)

    def test_read_image(self):
        """Test retrieving an Image instance."""
        image = Image.objects.get(pk=self.image.pk)
        self.assertEqual(image.file_name, "initial.png")
        self.assertEqual(image.owner, self.user)
        self.assertEqual(image.image_type, Image.ImageType.IMAGE)
        # self.assertEqual(image.alt_text, "Initial test image") # Add alt_text if you set it in setUpTestData
        self.assertTrue(image.image.name.endswith("initial.png"))
        self.assertTrue(image.thumbnail.name.endswith("initial_thumb.png"))

    def test_update_image(self):
        """Test updating fields of an Image instance."""
        image = Image.objects.get(pk=self.image.pk)
        original_update_time = image.updated_at

        # Update fields
        image.file_name = "updated_name.png"
        image.alt_text = "Updated alt text"  # Test updating alt_text
        image.image_type = Image.ImageType.SIDEBAR
        image.save()

        # Refresh from DB and check
        updated_image = Image.objects.get(pk=self.image.pk)
        self.assertEqual(updated_image.file_name, "updated_name.png")
        self.assertEqual(
            updated_image.alt_text, "Updated alt text"
        )  # Check updated alt_text
        self.assertEqual(updated_image.image_type, Image.ImageType.SIDEBAR)
        self.assertNotEqual(updated_image.updated_at, original_update_time)
        self.assertEqual(updated_image.owner, self.user)

    def test_delete_image(self):
        """Test deleting an Image instance."""
        # Create a dedicated image for deletion test to avoid conflicts
        delete_file = create_dummy_image("delete_me.png")
        image_to_delete = Image.objects.create(
            file_name="delete_me.png",
            file_size=delete_file.size,  # <-- Use .size instead of len(.content)
            mime_type=delete_file.content_type,
            image=delete_file,
            image_type=Image.ImageType.IMAGE,
            owner=self.user,
        )
        image_id = image_to_delete.id
        image_path = (
            image_to_delete.image.path
            if image_to_delete.image and hasattr(image_to_delete.image, "path")
            else None
        )

        # Delete the image
        image_to_delete.delete()

        # Verify it's gone from the database
        with self.assertRaises(Image.DoesNotExist):
            Image.objects.get(id=image_id)

        # Optional: Verify the file was deleted (relies on model's delete method working correctly)
        if image_path:
            self.assertFalse(os.path.exists(image_path))
