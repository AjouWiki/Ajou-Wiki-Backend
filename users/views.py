from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
from users.models import User
from . import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect


class Users(APIView):  # 일반 유저 생성
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.is_active = False
            user.save()
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            message = (
                "아래 URL로 접속하여 계정을 활성화 해주세요.\n URL = http://127.0.0.1:8000/api/v1/users/activate/"
                + token
            )
            mail_title = "[아주위키] " + str(user.name) + "님 계정 활성화 이메일"
            mail_to = request.data.get("email")
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

            serializer = serializers.UserSerializer(user)
            return Response({"result": "회원가입 성공!", "status": 200})
        else:
            return Response({"result": serializer.errors, "status": 403})


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            if user.is_active:
                login(request, user)
                serializer = serializers.PrivateUserSerializer(user)
                return Response(
                    {"result": "로그인 성공!", "status": 200, "user_info": serializer.data}
                )
            else:
                return Response({"result": "이메일 인증을 해주세요.", "status": 403})    
        else:
            return Response({"result": "아이디와 비밀번호를 확인해주세요.", "status": 403})


from rest_framework.exceptions import AuthenticationFailed


class Activate(APIView):
    def get(self, request, Jwt):
        token = Jwt
        if not token:
            return None
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )
        pk = decoded.get("pk")
        if not pk:
            return Response({"result": "Invalid Token", "status": 403})
            # raise AuthenticationFailed("Invalid Token")
        try:
            user = User.objects.get(pk=pk)
            user.is_active = True
            user.save()
            return redirect(
                "https://ajouwiki-email.nicepage.io/?version=ff087e76-3171-452f-92ab-337619d75d7e&uid=33c81b50-d7f4-45e3-bdb2-875a620d2ae8",
            )
            # return Response({"result": "Authentication PASS", "status": 200})
        except User.DoesNotExist:
            return Response({"result": "User Not Found", "status": 403})
            # raise AuthenticationFailed("User Not Found")


class is_email_available(APIView):
    def post(self, request):
        email = request.data.get("email", "None")
        if email == "None":
            return Response({"result": "None input", "status": 403})
        try:
            User.objects.get(email=email)
            return Response({"result": "impossible email", "status": 403})
        except User.DoesNotExist:
            return Response({"result": "possible email", "status": 200})


class is_username_available(APIView):
    def post(self, request):
        username = request.data.get("username", "None")
        if username == "None":
            return Response({"result": "None input", "status": 403})
        try:
            User.objects.get(username=username)
            return Response({"result": "impossible username", "status": 403})
        except User.DoesNotExist:
            return Response({"result": "possible username", "status": 200})
