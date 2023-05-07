from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        self.message = (
            'Для доступпа к данной странице необходимо авторизироваться!')

        if request.user.is_authenticated:
            return (request.method in permissions.SAFE_METHODS
                    or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = 'Изменение чужого контента запрещено!'

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
