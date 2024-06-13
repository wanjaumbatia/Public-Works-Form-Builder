from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id or request.user.is_staff
    
class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user)
        return request.user.is_staff