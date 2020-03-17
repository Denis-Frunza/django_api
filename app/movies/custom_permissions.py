from rest_framework import permissions


class PostPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_authenticated is False:
            return False
        return True
