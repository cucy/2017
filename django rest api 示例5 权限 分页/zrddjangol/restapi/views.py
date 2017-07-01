from rest_framework import generics
from rest_framework import permissions

from .models import Author
from .serializer import AuthorSerializer


# ----------------------------
# 自定义权限验证
# ----------------------------
class IsSuperUser_(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff



# 使用Generic class-based views
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,) # 权限校验


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # 使用自定权限
    permission_classes = (IsSuperUser_, )







