from rest_framework import serializers

from home.models import BannerModel


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        # fields = '__all__'
        fields = ['id','image','link']
        