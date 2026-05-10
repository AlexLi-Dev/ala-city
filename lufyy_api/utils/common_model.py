# 封装的基类数据表
from django.db import models

class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='创建人')
    # updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='更新人')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    is_showed = models.BooleanField(default=True, verbose_name='是否上架')
    orders = models.IntegerField(verbose_name='优先级')

    class Meta:
        # 这个表模型，只用来继承，不在数据库中生成表
        abstract = True # 关键: 标记为抽象基本类
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'

    def soft_delete(self):
        """软删除方法"""
        self.is_deleted = True
        self.save()

    def restore(self):
        """恢复软删除"""
        self.is_deleted = False
        self.save()