from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает чтение всем пользователям.
    Изменение доступно только администраторам.
    """
    def has_permission(self, request, view):
        # Чтение разрешено всем
        if request.method in SAFE_METHODS:
            return True
        # Изменение только для администраторов
        return request.user and request.user.is_staff
