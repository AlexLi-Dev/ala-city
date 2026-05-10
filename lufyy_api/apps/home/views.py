from email import message

from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

# Create your views here.

from rest_framework.views import APIView
from lufyy_api.utils.common_logger import logger


class HomeView(APIView):
    def get(self, request):
        logger.error(f"home view: {request.path}")
        logger.info(f'home {self.__class__.__name__}')
        return Response(status=status.HTTP_200_OK, data={'message': 'ok'})


# 跨域问题
from rest_framework.views import APIView


class CorsView(APIView):  # 继承APIView不需要处理csrf，view、viewset这些就需要处理
    def get(self, request):
        # return Response({'message': 'ok'}, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
        return Response({'message': 'ok'},)

    def post(self, request):
        print("post")
        # return Response({'message': ' post ok'}, headers={'Access-Control-Allow-Origin': '*',
        #                                                   })
        return Response({'message': ' post ok'},)
    # 简单请求 + 带凭证（Cookie/Token）时，Access-Control-Allow-Origin': '*' 不能用！
    def options(self, request):
        print("options")
        # return Response({'message': ' options ok'}, headers={'Access-Control-Allow-Origin': '*',
        #                                                      'Access-Control-Allow-Headers': '*',
        #                                                      'Access-Control-Allow-Methods': '*', })
        return Response({'message': ' options ok'}, )
    # 非简单请求总结：
    #     1. 第一次发送options请求通过后，后续就会一直发请求时的方法，例如post


# 首页轮播图接口
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .models import BannerModel
from .serializer import BannerSerializer
from utils.common_view import CommonListModelMixin


class BannerView(GenericViewSet, CommonListModelMixin):
    # 按优先级排序，只显示前三张
    queryset = BannerModel.objects.all().filter(is_deleted=False, is_showed=True).order_by('orders')[:3]
    serializer_class = BannerSerializer


def demo(request):
    return render(request,'demo.html')