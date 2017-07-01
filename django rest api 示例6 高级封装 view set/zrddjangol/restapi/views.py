from rest_framework import viewsets
from rest_framework import permissions

from .models import Author
from .serializer import AuthorSerializer


# ----------------------------
# 自定义权限验证
# ----------------------------
class IsSuperUser_(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff



# 使用 view set
# version 1
''' 
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
        This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
'''


# version 2

class AuthorViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


