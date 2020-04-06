from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    """
    Admin permission
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # if view.action in ('retrieve', 'list'):
            return request.user.has_perm('user.admin')
        return False


class ReadOnlyPermission(permissions.BasePermission):
    """
    Read Only permission
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ('retrieve', 'list'):
                return request.user.has_perm('user.read_only')
        return False
