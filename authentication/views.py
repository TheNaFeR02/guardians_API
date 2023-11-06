from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer, CustomRegisterSerializer
from rest_framework.generics import  RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import RegisterView
from allauth.account import app_settings as allauth_account_settings
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.utils import jwt_encode
from allauth.account.models import EmailConfirmation
from allauth.account.models import EmailAddress

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        # Check if the user authenticated via OAuth (e.g., by checking request data or headers)
        is_oauth_user = 'oauth_provider' in request.data  # Implement logic to check if it's an OAuth user
        print("is_oauth_user: ", is_oauth_user)

        # Continue with user registration logic
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if is_oauth_user:
            email_address = EmailAddress.objects.get(user=user)
            print('email_addrees: ', email_address)

            print('email_address.verified: ', email_address.verified)
            email_address.verified = True
            email_address.save()

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response
    
    

# Create your views here.
def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []

    def get_queryset(self):
        # Retrieve the current authenticated user using self.request.user
        # return User.objects.filter(id=self.request.user.id)
        return User.objects.all()


class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user