from django.urls import path
from .views import HomeView,BannerView,CorsView
from rest_framework.routers import SimpleRouter

# 生成路由对象
router = SimpleRouter()
# 路由为http://127.0.0.1:8000/api/v1/home/banner/
router.register('banner', BannerView, basename='banner')
# basename='banner' 用于反向解析 URL 的名称前缀

# 总路由
urlpatterns = [
    path('', HomeView.as_view()),
    path('cors/', CorsView.as_view()),
]

# 汇总 路由
urlpatterns += router.urls