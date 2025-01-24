from rest_framework.permissions import BasePermission


class IsActiveAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active)