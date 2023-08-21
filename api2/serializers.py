from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Category, Post, Comment, Tag

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'image', 'like', 'category']


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['create_dt'] # 얘만 제외하고 응답


# PostLikeAPIView를 GET 방식으로 바꿈에 따라 주석 처리
# class PostLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         # fields = '__all__'
#         fields = ['like']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'title', 'image', 'like', 'category']

    
#========================================================= 8.17    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


# 각각의 항목들이 딕셔너리 형태로 괄호가 쳐진채로 출력된다
# class CateTagSerializer(serializers.Serializer):
#     cateList = CategorySerializer(many=True)
#     tagList = TagSerializer(many=True)


# 각각의 항목들이 캐릭터 형태로 이름만 출력된다
class CateTagSerializer(serializers.Serializer):
    cateList = serializers.ListField(child=serializers.CharField())
    tagList = serializers.ListField(child=serializers.CharField())
    

# -------------------------------------------------- 8.18
class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class CommentSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'update_dt']


class PostSerializerDetail(serializers.Serializer):
    post = PostRetrieveSerializer()
    prevPost = PostSerializerSub()
    nextPost = PostSerializerSub()
    commentList = CommentSerializerSub(many=True)
# --------------------------------------------------

