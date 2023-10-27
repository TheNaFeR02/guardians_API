from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import  RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


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