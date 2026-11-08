from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner or editors can change data."

    def has_permission(self, request, view):
        # Pengunjung bebas membaca (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
            
        # Jika belum login, tolak
        if not request.user or not request.user.is_authenticated:
            return False
            
        # Superuser memiliki akses penuh
        if request.user.is_superuser:
            return True
            
        # Editor diizinkan melakukan PUT atau PATCH, tetapi tidak boleh POST atau DELETE
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )