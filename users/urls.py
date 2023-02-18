from django.urls import path, include

from . import views

from  rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('update-user/<int:pk>/', views.UserUpdateView.as_view(), name='update_user'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name="change-password"),


    path('reset-password/', views.ResetPassword.as_view(), name='reset-password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.PasswordResetConfirm.as_view(), name='reset-password-confirm'),

]
