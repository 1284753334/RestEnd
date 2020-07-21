 #加权限
from rest_framework.permissions import BasePermission

from App.models import UserModel

#权限 添加
class RequireLoginPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return isinstance(request.user,UserModel)
















