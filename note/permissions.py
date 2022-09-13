from rest_framework.permissions import BasePermission


class isOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return obj.user == request.user
