from django.contrib import admin
from django.shortcuts import render

# Register your models here.
from .models import BannerModel
# admin.site.register(BannerModel)

@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ['id', 'title','image_preview', 'link', 'info', 'created_time', 'updated_time']

    # 可编辑字段（直接在列表页修改）
    list_editable = ['title', 'link']

    # 搜索字段
    search_fields = ['title', 'info']

    # 筛选器
    list_filter = ['created_time',]

    # 每页显示数量
    list_per_page = 20

    actions = ['image_preview','batch_image_preview']
    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = '高级复制'

    # 图片预览方法
    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 80px; height: 50px; object-fit: cover;" />',
                obj.image.url
            )
        return '无图片'

    image_preview.short_description = '图片预览'

    def batch_image_preview(self, request, queryset):
        """批量预览选中的轮播图"""
        # 收集所有选中图片的信息
        banners = []
        for obj in queryset:
            banners.append({
                'id': obj.id,
                'title': obj.title,
                'image_url': obj.image.url if obj.image else None,
                'link': obj.link,
                'info': obj.info,
            })

        # 方法1：直接返回 HTML 页面
        return render(request, 'admin/batch_preview.html', {
            'banners': banners,
            'title': '批量图片预览',
        })

    batch_image_preview.short_description = '批量预览图片'




    # 字段分组（新增/编辑页面）
    fieldsets = (
        ('基础信息', {
            'fields': ('is_showed','is_deleted','orders','title', 'image', 'link', 'info'),
        }),
    )
