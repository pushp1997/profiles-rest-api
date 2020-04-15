from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only thier own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:  # Get is a safe method
            return True

        return obj.id == request.user.id
