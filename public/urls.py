from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),  # Public Homepage
    # path('login/', login_view, name='login'),  # Public Login Page
    # path('signup/', signup_view, name='signup'),  # Public Signup Page
]
