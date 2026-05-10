from django.db import models

# Create your models here.
from lufyy_api.utils.common_model import BaseModel

class BannerModel(BaseModel):
    title = models.CharField(max_length=16,unique=True,verbose_name='名称')
    image = models.ImageField(upload_to='banner',verbose_name='图片')
    # web,小程序,app, 轮播图，可以点击 点击 跳转某个地址
    # 跳转有两种情况 1.外链，2.自己的页面
    # todo 可以考虑增加link-type（链接类型）
    link = models.CharField(max_length=64,verbose_name='跳转链接')
    info = models.TextField(verbose_name='详情')

    class Meta:
        db_table = 'luffy_banner'
        verbose_name = '轮播图'  # 单数形式
        # verbose_name_plural 是 Django 模型中用于指定模型复数名称的属性，主要影响 Django Admin 后台的显示。
        verbose_name_plural = verbose_name # 复数形式，这里代表单复数相同


    def __str__(self):
        return self.title
    __repr__ = __str__
