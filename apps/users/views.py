from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

from apps.users.models import User
from apps.users.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    AvatarSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def profile(self, request, user_id=None):
        queryset = User.objects.filter(id=user_id or request.user.id)
        user = get_object_or_404(queryset)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def edit(self, request, user_id=None):
        queryset = User.objects.filter(id=user_id or request.user.id)
        user = get_object_or_404(queryset)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def post_avatar_profile(self, request, user_id=None):
        queryset = User.objects.filter(id=user_id or request.user.id)
        user = get_object_or_404(queryset)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get', 'put'])
    def avatar(self, request, user_id=None):
        queryset = User.objects.filter(id=user_id or request.user.id)
        user = get_object_or_404(queryset)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User, email=serializer.data.get('email')
        )
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        response = {
            'status': 'error',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': 'Password update failed',
            'data': {}
        }

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")
            new_confirm_password = serializer.data.get("new_confirm_password")

            if not self.object.check_password(old_password):
                response['data'] = {"old_password": ["Wrong password"]}
            elif new_password != new_confirm_password:
                response['data'] = {"new_password": ["New passwords do not match."]}
            else:
                self.object.set_password(new_password)
                self.object.save()

                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': {}
                }

        return Response(response)


class ResetPasswordAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'No user found with this email'}, status=400)
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            send_mail(
                'Password Reset Request',
                f'Ваш новый пароль  {password}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'success': 'Password reset email has been sent'})
        return Response({'error': 'Email field is required'}, status=400)
