"""
Vishwakarma AI - Profile Manager Tests
© 2025 Vishwakarma Industries
"""
import unittest
import os
import json
from engine.profile_manager import ProfileManager

class TestProfileManager(unittest.TestCase):
    """Unit tests for the ProfileManager class."""

    def setUp(self):
        """Set up a temporary database for testing."""
        self.db_name = "test_vishwakarma.db"
        self.profile_manager = ProfileManager(db_name=self.db_name)

    def tearDown(self):
        """Remove the temporary database after testing."""
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_profile(self):
        """Test creating a new user profile."""
        user_id = self.profile_manager.create_profile(
            name="Test User",
            age=30,
            preferences={"theme": "dark"}
        )
        self.assertIsNotNone(user_id)
        profile = self.profile_manager.get_profile(user_id)
        self.assertEqual(profile["name"], "Test User")
        self.assertEqual(profile["age"], 30)
        self.assertEqual(profile["preferences"]["theme"], "dark")

    def test_get_all_profiles(self):
        """Test getting all user profiles."""
        self.profile_manager.create_profile(name="User 1")
        self.profile_manager.create_profile(name="User 2")
        profiles = self.profile_manager.get_all_profiles()
        self.assertEqual(len(profiles), 2)

    def test_update_profile(self):
        """Test updating a user profile."""
        user_id = self.profile_manager.create_profile(name="Old Name")
        self.profile_manager.update_profile(user_id, name="New Name", age=25)
        profile = self.profile_manager.get_profile(user_id)
        self.assertEqual(profile["name"], "New Name")
        self.assertEqual(profile["age"], 25)

    def test_delete_profile(self):
        """Test deleting a user profile."""
        user_id = self.profile_manager.create_profile(name="To Be Deleted")
        self.profile_manager.delete_profile(user_id)
        profile = self.profile_manager.get_profile(user_id)
        self.assertEqual(profile["is_active"], 0)

    def test_has_profiles(self):
        """Test checking if profiles exist."""
        self.assertFalse(self.profile_manager.has_profiles())
        self.profile_manager.create_profile(name="Test User")
        self.assertTrue(self.profile_manager.has_profiles())

    def test_set_and_get_preference(self):
        """Test setting and getting a user preference."""
        user_id = self.profile_manager.create_profile(name="Test User")
        self.profile_manager.set_preference(user_id, "language", "en")
        language = self.profile_manager.get_preference(user_id, "language")
        self.assertEqual(language, "en")

if __name__ == '__main__':
    unittest.main()
