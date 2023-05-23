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
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Tag
from .serializers import TagSerializers

# Create your views here.


class CreateTag(APIView): # Tag 생성
    def post(self, request):
        tag = request.data.get("tag")
        wiki_id = request.data.get("wiki_id")
        if not tag or not wiki_id:
            return ParseError
        
        Tag.objects.create(name=tag, wiki_id=wiki_id)

        return Response({"result": "Tag 만들기 성공", "status": 200})

class DeleteTag(APIView): # Tag 제거
    def post(self, request):
        tag = request.data.get("tag")
        wiki_id = request.data.get("wiki_id")
        if not tag or not wiki_id:
            return ParseError
        
        tag_obj = get_object_or_404(Tag, name=tag, wiki_id=wiki_id)
        tag_obj.delete()
        return Response({"result": "Tag 지우기 성공", "status": 200})

        

class GetTagList(APIView): # Tag 조회
    def get(self, request):

    
        wiki_id = request.data.get("wiki_id")
        if not wiki_id:
            return ParseError
        tag_list = get_list_or_404(Tag, wiki_id=wiki_id)
        result = TagSerializers(tag_list, many=True)
        print(result)
        return Response({"data":result, "result": "Tag 리스트 가져오기 성공", "status": 200})