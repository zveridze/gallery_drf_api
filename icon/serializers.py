from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from icon.models import Picture, Comment, Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
        if 'author' not in validated_data:
            validated_data['author'] = self.context['request'].user
        return Like.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
        if 'author' not in validated_data:
            validated_data['author'] = self.context['request'].user
        return Comment.objects.create(**validated_data)


class PictureSerializer(serializers.ModelSerializer):

    total_comments = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, required=False)
    total_likes = serializers.SerializerMethodField()
    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['author', 'comments', 'likes']

    def create(self, validated_data):
        if 'author' not in validated_data:
            validated_data['author'] = self.context['request'].user
        return Picture.objects.create(**validated_data)

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_likes(self, obj):
        return obj.likes.count()


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

