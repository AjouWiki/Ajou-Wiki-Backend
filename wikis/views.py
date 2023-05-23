from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from django.conf import settings
from .models import Wiki
from . import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect


class Wikis(APIView):  # 일반 유저 생성
    def get(self, request):
        wikis = Wiki.objects.all()
        return Response(serializers.WikiSerializer(wikis, many=True).data)


class WikiDetail(APIView):
    def get_object(self, pk):
        try:
            for i in Wiki.objects.all():
                print(i)
            return Wiki.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        wiki = self.get_object(pk)
        serializer = serializers.WikiSerializer(
            wiki,
        )
        return Response(serializer.data)
