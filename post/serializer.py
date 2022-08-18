from rest_framework import serializers
from .models import MyPost


class MyPostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = MyPost.objects.create(
                                post=validated_data['post'],
                                user=self.context['request'].user
                )
        return post

    class Meta:
        model = MyPost
        fields = ['id', 'post', 'user']
        read_only_fields = ('user',)
