from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    '''Чтение и изменение контента доступно аддмину.'''
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class AdminOrReadOnly(permissions.BasePermission):
    '''Админ или только для чтения.'''
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_admin)


class ModerOrAuthorOrReadOnly(permissions.BasePermission):
    '''Автор, админ, можератор или только для чтения.'''
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
