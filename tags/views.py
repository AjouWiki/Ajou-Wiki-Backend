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
from tags.models import Tag
from wikis.models import Wiki
from tags.serializers import TagSerializers


# Create your views here.


class CreateTag(APIView): # Tag 생성 ( 잘 됨 )
    def post(self, request):
        tag = request.data.get("tag")
        wiki_id = request.data.get("wiki_id")
        if not tag or not wiki_id:
            return ParseError
        wiki = get_object_or_404(Wiki, pk=wiki_id)
        Tag.objects.create(name=tag, wiki_id=wiki)

        return Response({"result": "Tag 만들기 성공", "status": 200})

class DeleteTag(APIView): # Tag 제거 ( 잘 됨 )
    def post(self, request):
        tag = request.data.get("tag")
        wiki_id = request.data.get("wiki_id")
        if not tag or not wiki_id:
            return ParseError
        
        tag_obj = get_object_or_404(Tag, name=tag, wiki_id=wiki_id)
        tag_obj.delete()
        return Response({"result": "Tag 지우기 성공", "status": 200})

        

class GetTagList(APIView): # Tag 조회
    def get_object(self, pk):
        try:
            return Wiki.objects.get(pk=pk)
        except:
            return None
    def get(self, request, pk):
        wiki = self.get_object(pk)
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
    
        tag = Tag.objects.filter(wiki_id=wiki)
        result = serializers.TagSerializers(tag, many=True)
        return Response(result.data)