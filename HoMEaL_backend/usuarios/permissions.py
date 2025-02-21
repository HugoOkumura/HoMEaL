from rest_framework.permissions import BasePermission

class GerentePermissao(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo_usuario == 'gerente'