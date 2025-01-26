from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """

    def has_permission(self, request, view):
        # Разрешаем только авторизованным пользователям добавлять новые карты
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешаем редактирование и удаление только владельцу
        return obj.author == request.user
