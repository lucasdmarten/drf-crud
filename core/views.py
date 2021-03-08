from django.contrib.auth import get_user_model
from .serializers import UserSerializer, NaverSerializer, ProjetoSerializer\
    # ,RegisterSerializer
from core.models import Naver, Projeto
from rest_framework import generics, permissions, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsResponsibleForNaverOrReadOnly, IsResponsibleForProjectOrReadOnly




User = get_user_model()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NaverViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, IsResponsibleForNaverOrReadOnly, )
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, IsResponsibleForProjectOrReadOnly)
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
