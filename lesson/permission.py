from rest_framework import permissions
from .models import StudentPay


class IsOwnerAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if StudentPay.objects.filter(student=request.user, course=obj.course):
            return True

        return request.user.is_staff


