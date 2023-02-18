from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsCustomerOrTasker(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user == obj.customer or user == obj.tasker:
            return True
        raise PermissionDenied()
