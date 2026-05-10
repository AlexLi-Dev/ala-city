from django.db.models.expressions import result
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin

from home.models import BannerModel

from utils.common_response import APIResponse
class CommonListModelMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        res = super().list(request,*args, **kwargs)
        # 取出响应体的数据
        return APIResponse(result=res.data)