from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    # generics
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
