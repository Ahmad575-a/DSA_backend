from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User(username=serializer.validated_data['username'])
            user.set_password(serializer.validated_data['password'])  # set password before save
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all().values('id', 'username')
        return Response(users)
