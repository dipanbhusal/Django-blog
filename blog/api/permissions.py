from rest_framework.permissions import BasePermission, SAFE_METHODS
class OwnerOrReadOnly(BasePermission):
    message = 'Only original author can update the post.' 
    cust_safe_method = ['PUT']
 
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  
        return obj.author   == request.user 