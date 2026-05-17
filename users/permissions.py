from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"
    
class IsAdminOrOnlyPatch(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "admin":
            return True
        
        else:
            MEMBER_ONLY_METHOD = SAFE_METHODS + ("PATCH", )
            if request.method in MEMBER_ONLY_METHOD:
                return True
            
            else:
                return False