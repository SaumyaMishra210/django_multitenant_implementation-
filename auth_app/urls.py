from django.urls import path
from .views import CustomTokenObtainPairView, signup, logout
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup/', signup, name='signup'),
    path('auth/logout/', logout, name='logout'),
]
