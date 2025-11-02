"""
Vishwakarma AI - User Profile Manager
© 2025 Vishwakarma Industries

This module manages user profiles for personalized experience.
"""

import sqlite3
import json
from datetime import datetime


from engine.config import DATABASE_NAME

class ProfileManager:
    """Manages user profiles and preferences"""
    
    def __init__(self, db_name=DATABASE_NAME):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize the profiles table"""
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        # Create profiles table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                age INTEGER,
                preferences TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        # Create profile settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                setting_key VARCHAR(100),
                setting_value TEXT,
                FOREIGN KEY (user_id) REFERENCES profiles(user_id)
            )
        ''')
        
        con.commit()
        con.close()
    
    def create_profile(self, name, age=None, preferences=None):
        """
        Create a new user profile
        
        Args:
            name (str): User's name
            age (int): User's age (optional)
            preferences (dict): User preferences (optional)
        
        Returns:
            int: User ID of created profile
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        preferences_json = json.dumps(preferences) if preferences else "{}"
        
        cursor.execute('''
            INSERT INTO profiles (name, age, preferences, created_at)
            VALUES (?, ?, ?, ?)
        ''', (name, age, preferences_json, datetime.now()))
        
        user_id = cursor.lastrowid
        con.commit()
        con.close()
        
        return user_id
    
    def get_profile(self, user_id):
        """
        Get profile by user ID
        
        Args:
            user_id (int): User ID
        
        Returns:
            dict: User profile data
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('''
            SELECT user_id, name, age, preferences, created_at, last_login, is_active
            FROM profiles
            WHERE user_id = ?
        ''', (user_id,))
        
        row = cursor.fetchone()
        con.close()
        
        if row:
            return {
                'user_id': row[0],
                'name': row[1],
                'age': row[2],
                'preferences': json.loads(row[3]) if row[3] else {},
                'created_at': row[4],
                'last_login': row[5],
                'is_active': row[6]
            }
        return None
    
    def get_all_profiles(self):
        """
        Get all user profiles
        
        Returns:
            list: List of all profiles
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('''
            SELECT user_id, name, age, preferences, created_at, last_login, is_active
            FROM profiles
            WHERE is_active = 1
            ORDER BY last_login DESC
        ''')
        
        rows = cursor.fetchall()
        con.close()
        
        profiles = []
        for row in rows:
            profiles.append({
                'user_id': row[0],
                'name': row[1],
                'age': row[2],
                'preferences': json.loads(row[3]) if row[3] else {},
                'created_at': row[4],
                'last_login': row[5],
                'is_active': row[6]
            })
        
        return profiles
    
    def update_profile(self, user_id, **kwargs):
        """
        Update profile information
        
        Args:
            user_id (int): User ID
            **kwargs: Fields to update (name, age, preferences)
        
        Returns:
            bool: Success status
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        update_fields = []
        values = []
        
        if 'name' in kwargs:
            update_fields.append('name = ?')
            values.append(kwargs['name'])
        
        if 'age' in kwargs:
            update_fields.append('age = ?')
            values.append(kwargs['age'])
        
        if 'preferences' in kwargs:
            update_fields.append('preferences = ?')
            values.append(json.dumps(kwargs['preferences']))
        
        if not update_fields:
            return False
        
        values.append(user_id)
        query = f"UPDATE profiles SET {', '.join(update_fields)} WHERE user_id = ?"
        
        cursor.execute(query, values)
        con.commit()
        con.close()
        
        return True
    
    def update_last_login(self, user_id):
        """Update last login timestamp"""
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('''
            UPDATE profiles
            SET last_login = ?
            WHERE user_id = ?
        ''', (datetime.now(), user_id))
        
        con.commit()
        con.close()
    
    def delete_profile(self, user_id):
        """
        Soft delete a profile (mark as inactive)
        
        Args:
            user_id (int): User ID
        
        Returns:
            bool: Success status
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('''
            UPDATE profiles
            SET is_active = 0
            WHERE user_id = ?
        ''', (user_id,))
        
        con.commit()
        con.close()
        
        return True
    
    def has_profiles(self):
        """
        Check if any profiles exist
        
        Returns:
            bool: True if profiles exist
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM profiles WHERE is_active = 1')
        count = cursor.fetchone()[0]
        con.close()
        
        return count > 0
    
    def set_preference(self, user_id, key, value):
        """
        Set a user preference
        
        Args:
            user_id (int): User ID
            key (str): Setting key
            value (str): Setting value
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        # Check if setting exists
        cursor.execute('''
            SELECT id FROM profile_settings
            WHERE user_id = ? AND setting_key = ?
        ''', (user_id, key))
        
        if cursor.fetchone():
            # Update existing
            cursor.execute('''
                UPDATE profile_settings
                SET setting_value = ?
                WHERE user_id = ? AND setting_key = ?
            ''', (value, user_id, key))
        else:
            # Insert new
            cursor.execute('''
                INSERT INTO profile_settings (user_id, setting_key, setting_value)
                VALUES (?, ?, ?)
            ''', (user_id, key, value))
        
        con.commit()
        con.close()
    
    def get_preference(self, user_id, key, default=None):
        """
        Get a user preference
        
        Args:
            user_id (int): User ID
            key (str): Setting key
            default: Default value if not found
        
        Returns:
            str: Setting value
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        cursor.execute('''
            SELECT setting_value FROM profile_settings
            WHERE user_id = ? AND setting_key = ?
        ''', (user_id, key))
        
        row = cursor.fetchone()
        con.close()
        
        return row[0] if row else default
