from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Picture, Comment, Like
from .serializers import PictureSerializer, UserSerializer, CommentSerializer, LikeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.user.is_superuser:
            return True

        return obj.author.id == request.user.id


class PictureView(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, UserPermission]

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Picture.objects.all()
        user = User.objects.get(username=self.request.user)
        return Picture.objects.filter(author=user.id)


class SinglePictureView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, UserPermission]

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class CommentView(CreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class SingleCommentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, UserPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(CreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer


class SingleLikeView(DestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, UserPermission]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data='ssss', status=status.HTTP_200_OK)


class RegistrationView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
