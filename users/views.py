from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# Reset Password
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings

from .serializers import ResetPasswordSerializer, ResetPasswordConfirmSerializer


User = get_user_model()

from .serializers import UserRegistrationSerializer, UserUpdateSerializer, UserSerializer, ChangePasswordSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'email': user.email,
        })

class UserUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
    

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return User.objects.none()

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        message = {'message': 'Password updated successfully'}

        return Response({**response.data, **message}, status=response.status_code)


class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    def post(self, request, format=None):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'No user found with that email address.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate a unique token for the password reset email
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        
        # Build the password reset email message
        subject = 'Reset your password'
        message = f'Click the following link to reset your password:\n {settings.FRONTEND_URL}/reset-password/{uidb64}/{token}/'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        
        # Send the password reset email
        send_mail(subject, message, from_email, recipient_list)
        
        return Response({'success': 'Password reset email sent.'}, status=status.HTTP_200_OK)


class PasswordResetConfirm(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    def post(self, request, uidb64, token, format=None):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        
        if user is not None and default_token_generator.check_token(user, token):
            # Set the user's new password
            password = request.data.get('password')
            user.set_password(password)
            user.save()
            return Response({'success': 'Password reset successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid password reset link.'}, status=status.HTTP_400_BAD_REQUEST)
