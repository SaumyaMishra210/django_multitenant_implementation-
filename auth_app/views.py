from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Login (Generate JWT Tokens)
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({"access": response.data["access"], "refresh": response.data["refresh"]})


# Signup (Register User)
@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({"access": str(refresh.access_token), "refresh": str(refresh)}, status=status.HTTP_201_CREATED)


# Logout (Blacklist Refresh Token)
@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data.get("refresh")
        print(f"Received Refresh Token: {refresh_token}")  # Debugging
        token = RefreshToken(refresh_token)
        print(token)
        token.blacklist()
        return Response({"message": "Logged out successfully"}, status=200)
    except Exception as e:
        print(f"Logout Error: {str(e)}")  # Debugging
        return Response({"error": "Invalid token"}, status=400)
