from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            print("Usuario",request.user)
            print("Permiso: ", request.user.has_perm('core.add_cliente' ))
            return request.user.has_perm('pruebas.set_password' )
        else:
            return request.user.is_staff


    def has_object_permission(self, request, view, obj):
        print("Evaluando el has object permissions")
        return False