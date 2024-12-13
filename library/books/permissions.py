from rest_framework import permissions

def is_admin(user):
    return user.is_superuser

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return is_admin(request.user)
        return True