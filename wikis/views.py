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
from users.models import User
from django.conf import settings
from wikis.models import Wiki
from tags.models import Tag
from tags.serializers import TagSerializers
from wiki_details.models import Wiki_Detail
from wiki_details.serializers import WikiDetailsSerializer, MakeWikiDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from . import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class Wikis(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 유저만

    def get(self, request):
        wikis = Wiki.objects.all()
        return Response(serializers.WikiSerializer(wikis, many=True).data)

    def post(self, request):  # 위키 생성
        user_pk = request.user.pk
        serializer = serializers.WikiSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=user_pk)
            return Response({"result": serializer.data, "status": 200})
        return Response({"result": "데이터 이상", "status": 404})


class WikiDetail(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 유저만

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

    def put(self, request, pk):
        wiki = self.get_object(pk)

        serializer = serializers.WikiSerializer(
            wiki,
            data=request.data,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save(user_id=User.objects.filter(id=request.user.pk)[0])
        return Response(serializer.data)

    def post(self, request, pk):  # wiki_detail 제작
        wiki = self.get_object(pk)
        user_pk = request.user.pk
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
        request.data["wiki_id"] = pk
        request.data["user_id"] = user_pk
        serializer = MakeWikiDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "status": 200})
        return Response({"result": "데이터 이상", "status": 404})

    def delete(self, request, pk):
        wiki = self.get_object(pk)
        if wiki == None:
            return Response({"result": "존재하지 않는 위키입니다.", "status": 404})
        wiki.delete()
        return Response({"result": "위키 삭제", "status": 200})


class WikiDetailAPi(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 유저만

    def get_object(self, pk):
        try:
            return Wiki.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk, detail_pk):
        wiki_detail = Wiki_Detail.objects.get(pk=detail_pk)
        serializer = serializers.WikiDetailsSerializer(
            wiki_detail,
        )
        return Response({"result": serializer.data, "status": 200})

    def put(self, request, pk, detail_pk):
        wiki_detail = Wiki_Detail.objects.get(pk=detail_pk)
        serializer = serializers.WikiDetailsSerializer(
            wiki_detail,
            data=request.data,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save(user_id=User.objects.filter(id=request.user.pk)[0])
        return Response(serializer.data)

    def delete(self, request, pk, detail_pk):
        wiki_detail = Wiki_Detail.objects.get(pk=detail_pk)
        wiki_detail.delete()
        return Response({"result": "위키 삭제", "status": 200})


class SearchWiki(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 유저만

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
        res = []
        for i in result2.data:
            if i in result.data:
                res.append(i)

        return Response({"result": res, "status": 200})
