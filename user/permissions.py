from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_moderator:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_moderator:
                return True
        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if not request.user.is_moderator:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if not request.user.is_moderator:
                return True
        return False


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_moderator)
