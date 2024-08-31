from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Follow, Comment, Save

class UserSerializer(serializers.ModelSerializer): 
    followers = serializers.SerializerMethodField()
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta(): 
        model=User 
        fields = ['id', 'username', 'email', 'followers', 'password']

    def get_followers(self, obj): 
        return Follow.objects.filter(user=obj.id).count()
    
    def create(self, validated_data): 
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user 

    def validate_password(self, value):
        if len(value) <= 5: 
            raise serializers.ValidationError("Password Too Small")
        return value

class UsernameSerializer(serializers.ModelSerializer): 
    class Meta(): 
        model=User
        fields=['username', 'id']


class PostSerializer(serializers.ModelSerializer): 
    likes = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    author = UsernameSerializer(read_only=True)
    class Meta(): 
        model = Post
        fields = ['id','author', 'likes', 'title', 'img']
class CommentSerializer(serializers.ModelSerializer): 
    user = UsernameSerializer(read_only=True)
    class Meta(): 
        model = Comment
        fields = ['user', 'post', 'content']

class SinglePostSerializer(serializers.ModelSerializer): 
    likes = serializers.IntegerField(read_only=True)
    comments = serializers.SerializerMethodField()
    author = UsernameSerializer(read_only=True)
    class Meta(): 
        model = Post
        fields = [ 'author', 'likes', 'title', 'img', 'comments']
    def get_comments(self, obj): 
        items = Comment.objects.filter(post=obj.id)
        serialized_comments = CommentSerializer(items, many=True)
        return serialized_comments.data 

class SavedPostSerializer(serializers.ModelSerializer): 
    post = PostSerializer(read_only=True)
    post_id = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField(write_only=True)
    class Meta: 
        model = Save
        fields = ['post', 'user', 'post_id']

    