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
from wikis.models import Wiki
from tags.models import Tag
from tags.serializers import TagSerializers
from wiki_details.models import Wiki_Detail
from wiki_details.serializers import WikiDetailsSerializer, MakeWikiDetailsSerializer
from . import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class Wikis(APIView):  # 위키 생성
    def get(self, request):
        wikis = Wiki.objects.all()
        return Response(serializers.WikiSerializer(wikis, many=True).data)


class WikiDetail(APIView):
    def get_object(self, pk):
        try:
            return Wiki.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        wiki = self.get_object(pk)
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
        serializer = serializers.WikiSerializer(
            wiki,
        )
        return Response({"result": serializer.data, "status": 200})

    def post(self, request, pk):  # wiki_detail 제작
        permission_classes = [IsAuthenticated]

        wiki = self.get_object(pk)
        user_pk = request.user.pk
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
        request.data["wiki_id"] = pk
        request.data["user_id"] = user_pk
        serializer = MakeWikiDetailsSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
        return Response({"result": "here.", "status": 404})

    def delete(self, request, pk):
        permission_classes = [IsAuthenticated]

        wiki = self.get_object(pk)
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
        wiki.delete()
        return Response({"result": "위키 삭제", "status": 200})

class SearchWiki(APIView):
    def get_wiki_list_by_keyword(self, keyword):
        try:
            return Wiki.objects.filter(name=keyword)
        except:
            return None
    def get_wiki_list_by_tag(self, keyword):
        try:
            tag = Tag.objects.filter(name=keyword)
            wiki_list = [t.wiki_id for t in tag]
            return wiki_list
        except:
            return None
    def get(self, request, keyword):
        wiki_list1 = self.get_wiki_list_by_tag(keyword)
        wiki_list2 = self.get_wiki_list_by_keyword(keyword)

        result = serializers.WikiSerializer(wiki_list1, many=True)
        result2 = serializers.WikiSerializer(wiki_list2, many=True)

        return Response({"result":result.data+result2.data, "status":200})       
