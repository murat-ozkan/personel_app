from .serializers import Profile, ProfileSerializer

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer