from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer


def autologin(request: HttpRequest) -> HttpResponse:
    print('called', request.user)
    if request.user.is_authenticated:
        token = str(Token.objects.get(user=request.user))
        context = {
            "token": token,
        }

        response = render(request, 'autologin.html', context)
        response["X-Frame-Options"] = "ALLOW-FROM:http://127.0.0.1:3000"
        return response
    else:
        return HttpResponseBadRequest("Auth failed")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
