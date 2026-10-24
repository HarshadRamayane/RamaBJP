"""
RamaBJP Authentication Module
Handles user authentication with password hashing.
"""

import os
import hashlib
import secrets
from datetime import datetime, timedelta
from passlib.context import CryptContext


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# In-memory user store (for demo — replace with database in production)
_USERS = {}


def hash_password(password):
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """Verify a password against its hash."""
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        return False


def create_user(username, password, role="viewer", full_name=""):
    """Create a new user."""
    if username in _USERS:
        return False, "Username already exists"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    if role not in ["admin", "engineer", "viewer"]:
        return False, "Invalid role"
    
    _USERS[username] = {
        "username": username,
        "password_hash": hash_password(password),
        "role": role,
        "full_name": full_name or username,
        "created_at": datetime.now().isoformat(),
        "active": True
    }
    return True, "User created successfully"


def authenticate(username, password):
    """Authenticate a user."""
    user = _USERS.get(username)
    if not user:
        return None, "Invalid username or password"
    
    if not user["active"]:
        return None, "Account is disabled"
    
    if not verify_password(password, user["password_hash"]):
        return None, "Invalid username or password"
    
    return user, "Login successful"


def get_user(username):
    """Get user by username."""
    user = _USERS.get(username)
    if user:
        return {k: v for k, v in user.items() if k != "password_hash"}
    return None


def get_all_users():
    """Get all users (without password hashes)."""
    return [
        {k: v for k, v in user.items() if k != "password_hash"}
        for user in _USERS.values()
    ]


def update_user_role(username, new_role):
    """Update a user's role."""
    if username not in _USERS:
        return False, "User not found"
    
    if new_role not in ["admin", "engineer", "viewer"]:
        return False, "Invalid role"
    
    _USERS[username]["role"] = new_role
    return True, "Role updated"


def deactivate_user(username):
    """Deactivate a user."""
    if username not in _USERS:
        return False, "User not found"
    
    _USERS[username]["active"] = False
    return True, "User deactivated"


def has_permission(user, required_role):
    """Check if user has required permission level."""
    role_levels = {"viewer": 1, "engineer": 2, "admin": 3}
    user_level = role_levels.get(user.get("role", "viewer"), 1)
    required_level = role_levels.get(required_role, 1)
    return user_level >= required_level


def init_default_users():
    """Initialize default demo users."""
    if _USERS:
        return
    
    create_user("admin", "admin123", "admin", "Administrator")
    create_user("engineer", "engineer123", "engineer", "Maintenance Engineer")
    create_user("viewer", "viewer123", "viewer", "Read-Only Viewer")


# Initialize on import
init_default_users()
