from rest_framework.permissions import SAFE_METHODS, BasePermission


class OnlyOwnerCanEditLigneOrdonnance(BasePermission):
    """
    Create and update only allowed by owner
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == obj.ordonnance.owner
